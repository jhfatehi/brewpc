'''
print to Status / Error message as follows:
self.stat.text = 'Status or Error Message'
'''

import dbwrite
import dbread
import inval

import ConfigParser
import sshtunnel
import time

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import NoTransition

class Brew(TabbedPanel):
    scn1 = 'blank_screen1'
    scn2 = 'blank_screen2'
    scn3 = 'blank_screen3'

    def switch_to(self, header):
        # source of this switch_to logic is
        # https://github.com/kivy/kivy/wiki/Linking-ScreenManager-to-a-different-Widget
        if header.name == 'tab1':
            self.manager.current = self.scn1
        elif header.name == 'tab2':
            self.manager.current = self.scn2
        elif header.name == 'tab3':
            self.manager.current = self.scn3
        elif header.name == 'tab4':
            self.manager.current = 'add_brew'
        elif header.name == 'tab5':
            self.manager.current = 'add_process'
        header.state = 'down' # makes tab 1 start in the down position
        self._current_tab = header
        self.manager.transition = NoTransition() # prevents tabs from sliding left on transition

    # notes:
    # current_tab -- TabbedPanel
    # current_screen -- Screen manager  -- BlankScreen containing spinner
    # self.current_tab.name -- e.g., 'tab1'
    # self.manager.current_screen.screen.text -- e.g., blank_screen2
    # set self.manager.current equal to some self.manager.current_screen.screen.text
    # so self.manager.current should be something like 'blank_screen2'

    def change_screen(self):
        self.db_path = ConfigParser.RawConfigParser()
        self.db_path.read('conn.cfg')
        if inval.check_brew_batch(self.db_path, self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text):
            self.stat.text = 'Status: change_screen'
            if self.current_tab.name == 'tab1':
                self.scn1 = self.manager.current_screen.screen.text+'1'
                r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
                self.manager.current = self.scn1
                self.manager.current_screen.screen.text = self.scn1[0:-1]
                self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
            elif self.current_tab.name == 'tab2':
                self.scn2 = self.manager.current_screen.screen.text+'2'
                r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
                self.manager.current = self.scn2
                self.manager.current_screen.screen.text = self.scn2[0:-1]
                self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
            elif self.current_tab.name == 'tab3':
                self.scn3 = self.manager.current_screen.screen.text+'3'
                r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
                self.manager.current = self.scn3
                self.manager.current_screen.screen.text = self.scn3[0:-1]
                self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
        else: self.stat.text = 'Error - Brew and Batch do not exist.'

    def create_process(self):
        self.db_path = ConfigParser.RawConfigParser()
        self.db_path.read('conn.cfg')

        try:
            self.stat.text = 'Status - Working'
            tGRStemp = float(self.ap.tGRStemp.text)
            tSTKtemp = float(self.ap.tSTKtemp.text)
            tMSHvol = float(self.ap.tMSHvol.text)
            tMSHtemp = float(self.ap.tMSHtemp.text)
            tMASHphLOW = float(self.ap.tMASHphLOW.text)
            tMASHphHI = float(self.ap.tMASHphHI.text)
            tSPGvol = float(self.ap.tSPGvol.text)

            try:
                dbwrite.add_process(self.db_path,
                    self.ap.brand.text,
                    tGRStemp,
                    tSTKtemp,
                    tMSHvol,
                    tMSHtemp,
                    tMASHphLOW,
                    tMASHphHI,
                    tSPGvol)
                self.stat.text = 'Status: Process Created'
            except:
                self.stat.text = 'Error - The Brand Size Combination Already Exists.'
                
        except:
            self.stat.text = 'Error - A non-number was entered.'

    def create_brew(self):
        self.db_path = ConfigParser.RawConfigParser()
        self.db_path.read('conn.cfg')
        if not inval.check_brew(self.db_path, self.ab.brew_num.text):
            if inval.check_int(self.ab.batches.text):
                if inval.check_brand(self.db_path, self.ab.brand.text):
                    self.stat.text = 'Status - Working'
                    dbwrite.add_brew(self.db_path, self.ab.batches.text, self.ab.brew_num.text, self.ab.brand.text)
                    self.stat.text = 'Status - Brew number ' + self.ab.brew_num.text + ' has been added.'
                else: self.stat.text = 'Error - No process for brand.'
            else: self.stat.text = 'Error - Number of bacthes must be an integer.'
        else: self.stat.text = 'Error - Brew number aready exists.'


    def db_read(self):
        self.db_path = ConfigParser.RawConfigParser()
        self.db_path.read('conn.cfg')
        if inval.check_brew_batch(self.db_path, self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text):
            ############# db read from mash table ###############
            if self.manager.current_screen.screen.text == 'mash_screen':
                ms = {'mash_screen1':self.ms1, 'mash_screen2':self.ms2, 'mash_screen3':self.ms3}
                x = self.manager.current
                self.stat.text = 'Status - Working'
                #ms[x].dGRStemp.text, ms[x].dSTKtemp.text, ms[x].dMSHvol.text, ms[x].dMSHtemp.text, ms[x].dMSHtime.text, ms[x].dBREWsig.text, ms[x].dRNCvol.text, ms[x].dVLFtime.text, ms[x].dMASHph.text, ms[x].d1RNvol.text, ms[x].dSPGvol.text, ms[x].dROFtime.text, ms[x].dRACKcnt.text, ms[x].dFILLtime.text, ms[x].dFILLvol.text, ms[x].tsize.text, ms[x].tbrand.text , ms[x].tGRStemp.text , ms[x].tSTKtemp.text , ms[x].tMSHvol.text , ms[x].tMSHtemp.text , ms[x].tMASHphLOW.text , ms[x].tMASHphHI.text , ms[x].tSPGvol.text  = dbread.mash(self.db_path, ms[x].brew_num.text, ms[x].batch_num.text)
                datas, targets, batches = dbread.mash(self.db_path, ms[x].brew_num.text, ms[x].batch_num.text)
                ms[x].dGRStemp.text   = datas['dGRStemp']
                ms[x].dSTKtemp.text   = datas['dSTKtemp']
                ms[x].dMSHvol.text    = datas['dMSHvol']
                ms[x].dMSHtemp.text   = datas['dMSHtemp']
                ms[x].dMSHtime.text   = datas['dMSHtime']
                ms[x].dBREWsig.text   = datas['dBREWsig']
                ms[x].dRNCvol.text    = datas['dRNCvol']
                ms[x].dVLFtime.text   = datas['dVLFtime']
                ms[x].dMASHph.text    = datas['dMASHph']
                ms[x].d1RNvol.text    = datas['d1RNvol']
                ms[x].dSPGvol.text    = datas['dSPGvol']
                ms[x].dROFtime.text   = datas['dROFtime']
                ms[x].dRACKcnt.text   = datas['dRACKcnt']
                ms[x].dFILLtime.text  = datas['dFILLtime']
                ms[x].dFILLvol.text   = datas['dFILLvol']
                ms[x].tbrand.text     = targets['tbrand']
                ms[x].tGRStemp.text   = targets['tGRStemp']
                ms[x].tSTKtemp.text   = targets['tSTKtemp']
                ms[x].tMSHvol.text    = targets['tMSHvol']
                ms[x].tMSHtemp.text   = targets['tMSHtemp']
                ms[x].tMASHphLOW.text = targets['tMASHphLOW']
                ms[x].tMASHphHI.text  = targets['tMASHphHI']
                ms[x].tSPGvol.text    = targets['tSPGvol']
                ms[x].tbatches.text   = batches
                self.stat.text = 'Status: Load Complete'
            #####################################################
        else: self.stat.text = 'Error - Brew and Batch do not exist.'

    def db_write(self):
        def xfloat(s):
            if s == '':
                return ''
            return float(s)

        def xtime(s):
            if s == '':
                return ''
            try:
                x = time.strptime(s, '%H%M')
                return (s+'00')
            except:
                pass

        self.db_path = ConfigParser.RawConfigParser()
        self.db_path.read('conn.cfg')
        if inval.check_brew_batch(self.db_path, self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text):
            self.stat.text = 'Status: Save in progress'

            ############# db write from mash table ###############
            if self.manager.current_screen.screen.text == 'mash_screen':
                ms = {'mash_screen1':self.ms1, 'mash_screen2':self.ms2, 'mash_screen3':self.ms3}
                x = self.manager.current
                try:
                    self.stat.text = 'Status - Working'
                    dbwrite.mash(self.db_path,
                        xfloat(ms[x].brew_num.text),
                        xfloat(ms[x].batch_num.text),
                        xfloat(ms[x].dGRStemp.text),
                        xfloat(ms[x].dSTKtemp.text),
                        xfloat(ms[x].dMSHvol.text),
                        xfloat(ms[x].dMSHtemp.text),
                        xtime(ms[x].dMSHtime.text),
                        ms[x].dBREWsig.text,
                        xfloat(ms[x].dRNCvol.text),
                        xtime(ms[x].dVLFtime.text),
                        xfloat(ms[x].dMASHph.text),
                        xfloat(ms[x].d1RNvol.text),
                        xfloat(ms[x].dSPGvol.text),
                        xtime(ms[x].dROFtime.text),
                        xfloat(ms[x].dRACKcnt.text),
                        xtime(ms[x].dFILLtime.text),
                        xfloat(ms[x].dFILLvol.text))
                    self.stat.text = 'Status: Save complete'
                except:
                    self.stat.text = 'Error - A non-number or bad time was entered.'
            #####################################################



        else: self.stat.text = 'Error - Brew and Batch do not exist.'

class BrewApp(App):
    def on_start(self):
        config = ConfigParser.RawConfigParser()
        config.read('conn.cfg')

        self.tunnel = sshtunnel.SSHTunnelForwarder(
                (config.get('ssh', 'host'), 22),
                ssh_username=config.get('ssh', 'usr'),
                ssh_password=config.get('ssh', 'pw'),
                remote_bind_address=('127.0.0.1', 3306))    

        self.tunnel.start()
        config.set('mysql', 'local_bind_port', str(self.tunnel.local_bind_port))
        
        with open('conn.cfg', 'wb') as configfile:
            config.write(configfile)

        print('ssh tunnel opened')

    def on_stop(self):
        self.tunnel.stop()
        print('ssh tunnel closed')

    def build(self):
        return Brew()

if __name__ == '__main__':
    BrewApp().run()