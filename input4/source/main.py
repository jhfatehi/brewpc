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
    scn4 = 'blank_screen4'

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
            self.manager.current = self.scn4
        elif header.name == 'tab5':
            self.manager.current = 'add_brew'
        elif header.name == 'tab6':
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
                self.t1id.text = str(r) + ' - ' + str(a) + ' - ' + self.scn1[0].upper()
            elif self.current_tab.name == 'tab2':
                self.scn2 = self.manager.current_screen.screen.text+'2'
                r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
                self.manager.current = self.scn2
                self.manager.current_screen.screen.text = self.scn2[0:-1]
                self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
                self.t2id.text = str(r) + ' - ' + str(a) + ' - ' + self.scn2[0].upper()
            elif self.current_tab.name == 'tab3':
                self.scn3 = self.manager.current_screen.screen.text+'3'
                r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
                self.manager.current = self.scn3
                self.manager.current_screen.screen.text = self.scn3[0:-1]
                self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
                self.t3id.text = str(r) + ' - ' + str(a) + ' - ' + self.scn3[0].upper()
            elif self.current_tab.name == 'tab4':
                self.scn4 = self.manager.current_screen.screen.text+'4'
                r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
                self.manager.current = self.scn4
                self.manager.current_screen.screen.text = self.scn4[0:-1]
                self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
                self.t4id.text = str(r) + ' - ' + str(a) + ' - ' + self.scn4[0].upper()
        else: self.stat.text = 'Error - Brew and Batch do not exist.'

    def previous_screen(self):
        if self.manager.current_screen.name[0:-1] == 'mash_screen':
            self.manager.current_screen.screen.text = 'knock_out_screen'
            self.change_screen()
        elif self.manager.current_screen.name[0:-1] == 'boil_screen':
            self.manager.current_screen.screen.text = 'mash_screen'
            self.change_screen()
        elif self.manager.current_screen.name[0:-1] == 'knock_out_screen':
            self.manager.current_screen.screen.text = 'boil_screen'
            self.change_screen()

    def next_screen(self):
        if self.manager.current_screen.name[0:-1] == 'mash_screen':
            self.manager.current_screen.screen.text = 'boil_screen'
            self.change_screen()
        elif self.manager.current_screen.name[0:-1] == 'boil_screen':
            self.manager.current_screen.screen.text = 'knock_out_screen'
            self.change_screen()
        elif self.manager.current_screen.name[0:-1] == 'knock_out_screen':
            self.manager.current_screen.screen.text = 'mash_screen'
            self.change_screen()

    def create_brew(self):
        self.db_path = ConfigParser.RawConfigParser()
        self.db_path.read('conn.cfg')
        if not inval.check_brew(self.db_path, self.ab.brew_num.text):
            if inval.check_int(self.ab.batches.text):
                if inval.check_brand(self.db_path, self.ab.brand.text):
                    try:
                        x = time.strptime(self.ab.strtDATE.text, '%Y%m%d')
                        x = time.strptime(self.ab.finDATE.text, '%Y%m%d')
                        self.stat.text = 'Status - Working'
                        dbwrite.add_brew(self.db_path, self.ab.batches.text, self.ab.brew_num.text, self.ab.brand.text, self.ab.fV.text, self.ab.strtDATE.text, self.ab.finDATE.text)
                        self.stat.text = 'Status - Brew number ' + self.ab.brew_num.text + ' has been added.'
                    except:
                        self.stat.text = 'Error - Invalid date entered.'
                else: self.stat.text = 'Error - No process for brand.'
            else: self.stat.text = 'Error - Number of bacthes must be an integer.'
        else: self.stat.text = 'Error - Brew number aready exists.'

    def db_read(self):
        self.db_path = ConfigParser.RawConfigParser()
        self.db_path.read('conn.cfg')
        if inval.check_brew_batch(self.db_path, self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text):
            ############# db read from mash table ###############
            if self.manager.current_screen.screen.text == 'mash_screen':
                ms = {'mash_screen1':self.ms1, 'mash_screen2':self.ms2, 'mash_screen3':self.ms3, 'mash_screen4':self.ms4}
                x = self.manager.current
                self.stat.text = 'Status - Working'
                datas, targets, brewfo = dbread.mash(self.db_path, ms[x].brew_num.text, ms[x].batch_num.text)
                ms[x].dGRStemp.text   = datas['dGRStemp']
                ms[x].dSTKtemp.text   = datas['dSTKtemp']
                ms[x].dMSHvol.text    = datas['dMSHvol']
                ms[x].dMSHtemp.text   = datas['dMSHtemp']
                ms[x].dMSHtime.text   = datas['dMSHtime']
                ms[x].dBREWsig.text   = datas['dBREWsig']
                ms[x].dRNCvol.text    = datas['dRNCvol']
                ms[x].dVLFtime.text   = datas['dVLFtime']
                ms[x].dMASHph.text    = datas['dMASHph']
                ms[x].d1RNp.text      = datas['d1RNp']
                ms[x].dSPGvol.text    = datas['dSPGvol']
                ms[x].dROFtime.text   = datas['dROFtime']
                ms[x].dRACKcnt.text   = datas['dRACKcnt']
                ms[x].dFILLtime.text  = datas['dFILLtime']
                ms[x].dFILLvol.text   = datas['dFILLvol']
                ms[x].dMASHnote.text  = datas['dMASHnote']
                ms[x].tGRStemp.text   = targets['tGRStemp']
                ms[x].tSTKtemp.text   = targets['tSTKtemp']
                ms[x].tMSHvol.text    = targets['tMSHvol']
                ms[x].tMSHtemp.text   = targets['tMSHtemp']
                ms[x].tMASHphLOW.text = targets['tMASHphLOW']
                ms[x].tMASHphHI.text  = targets['tMASHphHI']
                ms[x].tSPGvol.text    = targets['tSPGvol']  
                ms[x].iWT1.text       = targets['iWT1']
                ms[x].iWT1lb.text     = targets['iWT1lb']
                ms[x].iWT2.text       = targets['iWT2']
                ms[x].iWT2lb.text     = targets['iWT2lb']
                ms[x].iWT3.text       = targets['iWT3']
                ms[x].iWT3lb.text     = targets['iWT3lb']
                ms[x].iWT4.text       = targets['iWT4']
                ms[x].iWT4lb.text     = targets['iWT4lb']
                ms[x].iWT5.text       = targets['iWT5']
                ms[x].iWT5lb.text     = targets['iWT5lb']
                ms[x].iGST1.text      = targets['iGST1']
                ms[x].iGST1sk.text    = targets['iGST1sk']
                ms[x].iGST1lb.text    = targets['iGST1lb']
                ms[x].iGST2.text      = targets['iGST2']
                ms[x].iGST2sk.text    = targets['iGST2sk']
                ms[x].iGST2lb.text    = targets['iGST2lb']
                ms[x].iGST3.text      = targets['iGST3']
                ms[x].iGST3sk.text    = targets['iGST3sk']
                ms[x].iGST3lb.text    = targets['iGST3lb']
                ms[x].iGST4.text      = targets['iGST4']
                ms[x].iGST4sk.text    = targets['iGST4sk']
                ms[x].iGST4lb.text    = targets['iGST4lb']
                ms[x].iGST5.text      = targets['iGST5']
                ms[x].iGST5sk.text    = targets['iGST5sk']
                ms[x].iGST5lb.text    = targets['iGST5lb']
                ms[x].iGST6.text      = targets['iGST6']
                ms[x].iGST6sk.text    = targets['iGST6sk']
                ms[x].iGST6lb.text    = targets['iGST6lb']
                ms[x].iGST7.text      = targets['iGST7']
                ms[x].iGST7sk.text    = targets['iGST7sk']
                ms[x].iGST7lb.text    = targets['iGST7lb']
                ms[x].iGSTtotlb.text  = targets['iGSTtotlb']
                ms[x].tbrand.text     = brewfo['tbrand']
                ms[x].tbatches.text   = brewfo['tbatches']
                ms[x].tFV.text        = brewfo['tFV']
                ms[x].tstrtDATE.text  = brewfo['tstrtDATE']
                ms[x].tfinDATE.text   = brewfo['tfinDATE']

                self.stat.text = 'Status: Load Complete'
            #####################################################
            ############# db read from boil table ###############
            if self.manager.current_screen.screen.text == 'boil_screen':
                ms = {'boil_screen1':self.bs1, 'boil_screen2':self.bs2, 'boil_screen3':self.bs3, 'boil_screen4':self.bs4}
                x = self.manager.current
                self.stat.text = 'Status - Working'
                datas, targets, brewfo = dbread.boil(self.db_path, ms[x].brew_num.text, ms[x].batch_num.text)
                ms[x].dBOILtime.text   = datas['dBOILtime']
                ms[x].dHOP1time.text   = datas['dHOP1time']
                ms[x].dIGp.text    = datas['dIGp']
                ms[x].dIPH.text   = datas['dIPH']
                ms[x].dLIQ1gal.text   = datas['dLIQ1gal']
                ms[x].dHOP2time.text   = datas['dHOP2time']
                ms[x].dZINCtime.text    = datas['dZINCtime']
                ms[x].dKICKtime.text   = datas['dKICKtime']
                ms[x].dHOP3time.text    = datas['dHOP3time']
                ms[x].dMESLVLbbl.text    = datas['dMESLVLbbl']
                ms[x].dMESGp.text    = datas['dMESGp']
                ms[x].dLIQ2gal.text   = datas['dLIQ2gal']
                ms[x].dFNLLVLbbl.text   = datas['dFNLLVLbbl']
                ms[x].dFNLGp.text  = datas['dFNLGp']
                ms[x].dFNLPH.text   = datas['dFNLPH']
                ms[x].dBOILnote.text   = datas['dBOILnote']
                ms[x].tFG.text        = targets['tFG']
                ms[x].tBOILphLO.text  = targets['tBOILphLO']
                ms[x].tBOILphHI.text  = targets['tBOILphHI']
                ms[x].iZNg.text       = targets['iZNg']
                ms[x].iKICKoz.text    = targets['iKICKoz']
                ms[x].iHOP1.text      = targets['iHOP1']
                ms[x].iHOP1kg.text    = targets['iHOP1kg']  
                ms[x].iHOP1min.text   = targets['iHOP1min']
                ms[x].iHOP2.text      = targets['iHOP2']
                ms[x].iHOP2kg.text    = targets['iHOP2kg']
                ms[x].iHOP2min.text   = targets['iHOP2min']
                ms[x].iHOP3.text      = targets['iHOP3']
                ms[x].iHOP3kg.text    = targets['iHOP3kg']
                ms[x].iHOP3min.text   = targets['iHOP3min']
                ms[x].iHOP4.text      = targets['iHOP4']
                ms[x].iHOP4kg.text    = targets['iHOP4kg']
                ms[x].iHOP4min.text   = targets['iHOP4min']
                ms[x].iHOP5.text      = targets['iHOP5']
                ms[x].iHOP5kg.text    = targets['iHOP5kg']
                ms[x].iHOP5min.text   = targets['iHOP5min']
                ms[x].iHOP6.text      = targets['iHOP6']
                ms[x].iHOP6kg.text    = targets['iHOP6kg']
                ms[x].iHOP6min.text   = targets['iHOP6min']
                ms[x].iHOP7.text      = targets['iHOP7']
                ms[x].iHOP7kg.text    = targets['iHOP7kg']
                ms[x].iHOP7min.text   = targets['iHOP7min']
                ms[x].tbrand.text     = brewfo['tbrand']
                ms[x].tbatches.text   = brewfo['tbatches']
                ms[x].tFV.text        = brewfo['tFV']
                ms[x].tstrtDATE.text  = brewfo['tstrtDATE']
                ms[x].tfinDATE.text   = brewfo['tfinDATE']

                self.stat.text = 'Status: Load Complete'
            #####################################################
            ############# db read from knock_out table ###############
            if self.manager.current_screen.screen.text == 'knock_out_screen':
                ms = {'knock_out_screen1':self.ks1, 'knock_out_screen2':self.ks2, 'knock_out_screen3':self.ks3, 'knock_out_screen4':self.ks4}
                x = self.manager.current
                self.stat.text = 'Status - Working'
                datas, targets, brewfo  = dbread.knock_out(self.db_path, ms[x].brew_num.text, ms[x].batch_num.text)              
                ms[x].dKOSRTtime.text   = datas['dKOSRTtime']
                ms[x].dKOsig.text       = datas['dKOsig']
                ms[x].dKOtemp.text      = datas['dKOtemp']
                ms[x].dO2lpm.text       = datas['dO2lpm']
                ms[x].dO2ppm.text       = datas['dO2ppm']
                ms[x].dKOENDtime.text   = datas['dKOENDtime']
                ms[x].dFMVOLbbl.text    = datas['dFMVOLbbl']
                ms[x].dCLDFVbbl.text    = datas['dCLDFVbbl']
                ms[x].dBD600sig.text    = datas['dBD600sig']
                ms[x].dBD900sig.text    = datas['dBD900sig']
                ms[x].dBD1200sig.text   = datas['dBD1200sig']
                ms[x].dBD1500sig.text   = datas['dBD1500sig']
                ms[x].dOGp.text         = datas['dOGp']
                ms[x].dYSTGEN.text      = datas['dYSTGEN']
                ms[x].dSRCFV.text       = datas['dSRCFV']
                ms[x].dSRCNUM.text      = datas['dSRCNUM']
                ms[x].dAMTPTCHmin.text  = datas['dAMTPTCHmin']
                ms[x].dAMTPTCHsec.text  = datas['dAMTPTCHsec']
                ms[x].dFRMTEMPsig.text  = datas['dFRMTEMPsig']
                ms[x].dAFOoz.text       = datas['dAFOoz']
                ms[x].dAFOsig.text      = datas['dAFOsig']
                ms[x].dKOnote.text      = datas['dKOnote']
                ms[x].tWASTEbbl.text    = targets['tWASTEbbl']
                ms[x].tFERMf.text       = targets['tFERMf']
                ms[x].tYEASTtype.text   = targets['tYEASTtype']
                ms[x].tbrand.text       = brewfo['tbrand']
                ms[x].tbatches.text     = brewfo['tbatches']
                ms[x].tFV.text          = brewfo['tFV']
                ms[x].tstrtDATE.text    = brewfo['tstrtDATE']
                ms[x].tfinDATE.text     = brewfo['tfinDATE']

                self.stat.text = 'Status: Load Complete'
                
        else: self.stat.text = 'Error - Brew and Batch do not exist.'

    def db_write(self):
        def xfloat(s):
            if s == '':
                return ''
            return float(s)

        def xtime(s):
            if s == '':
                return ''
            if len(s)!=4:
                raise Exception('Time is not 4 digits')
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
                ms = {'mash_screen1':self.ms1, 'mash_screen2':self.ms2, 'mash_screen3':self.ms3, 'mash_screen4':self.ms4}
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
                        xfloat(ms[x].d1RNp.text),
                        xfloat(ms[x].dSPGvol.text),
                        xtime(ms[x].dROFtime.text),
                        xfloat(ms[x].dRACKcnt.text),
                        xtime(ms[x].dFILLtime.text),
                        xfloat(ms[x].dFILLvol.text),
                        ms[x].dMASHnote.text)
                    self.stat.text = 'Status: Save complete'
                except Exception as e:
                    print(e)
                    self.stat.text = 'Error - A incorrectly formatted time was entered.'
            #####################################################
            ############# db write from boil table ###############
            if self.manager.current_screen.screen.text == 'boil_screen':
                ms = {'boil_screen1':self.bs1, 'boil_screen2':self.bs2, 'boil_screen3':self.bs3, 'boil_screen4':self.bs4}
                x = self.manager.current
                try:
                    self.stat.text = 'Status - Working'
                    dbwrite.boil(self.db_path,
                        xfloat(ms[x].brew_num.text),
                        xfloat(ms[x].batch_num.text),
                        xtime(ms[x].dBOILtime.text),
                        xtime(ms[x].dHOP1time.text),
                        xfloat(ms[x].dIGp.text),
                        xfloat(ms[x].dIPH.text),
                        xfloat(ms[x].dLIQ1gal.text),
                        xtime(ms[x].dHOP2time.text),
                        xtime(ms[x].dZINCtime.text),
                        xtime(ms[x].dKICKtime.text),
                        xtime(ms[x].dHOP3time.text),
                        xfloat(ms[x].dMESLVLbbl.text),
                        xfloat(ms[x].dMESGp.text),
                        xfloat(ms[x].dLIQ2gal.text),
                        xfloat(ms[x].dFNLLVLbbl.text),
                        xfloat(ms[x].dFNLGp.text),
                        xfloat(ms[x].dFNLPH.text),
                        ms[x].dBOILnote.text)
                    self.stat.text = 'Status: Save complete'
                except Exception as e:
                    print(e)
                    self.stat.text = 'Error - A incorrectly formatted time was entered.'
            #####################################################
            ############# db write from knock out table ###############
            if self.manager.current_screen.screen.text == 'knock_out_screen':
                ms = {'knock_out_screen1':self.ks1, 'knock_out_screen2':self.ks2, 'knock_out_screen3':self.ks3, 'knock_out_screen4':self.ks4}
                x = self.manager.current
                try:
                    self.stat.text = 'Status - Working'
                    dbwrite.knock_out(self.db_path,
                        xfloat(ms[x].brew_num.text),
                        xfloat(ms[x].batch_num.text),
                        xtime(ms[x].dKOSRTtime.text),
                        ms[x].dKOsig.text,
                        xfloat(ms[x].dKOtemp.text),
                        xfloat(ms[x].dO2lpm.text),
                        xfloat(ms[x].dO2ppm.text),
                        xtime(ms[x].dKOENDtime.text),
                        xfloat(ms[x].dFMVOLbbl.text),
                        xfloat(ms[x].dCLDFVbbl.text),
                        ms[x].dBD600sig.text,
                        ms[x].dBD900sig.text,
                        ms[x].dBD1200sig.text,
                        ms[x].dBD1500sig.text,
                        xfloat(ms[x].dOGp.text),
                        xfloat(ms[x].dYSTGEN.text),
                        xfloat(ms[x].dSRCFV.text),
                        xfloat(ms[x].dSRCNUM.text),
                        xfloat(ms[x].dAMTPTCHmin.text),
                        xfloat(ms[x].dAMTPTCHsec.text),
                        ms[x].dFRMTEMPsig.text,
                        xfloat(ms[x].dAFOoz.text),
                        ms[x].dAFOsig.text,
                        ms[x].dKOnote.text)
                    self.stat.text = 'Status: Save complete'
                except Exception as e:
                    print(e)
                    self.stat.text = 'Error - A incorrectly formatted time was entered.'
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