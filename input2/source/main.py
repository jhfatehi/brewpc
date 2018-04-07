'''
print to Status / Error message as follows:
self.stat.text = 'Status or Error Message'
'''

import dbwrite
import dbread
import inval

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import NoTransition

class Brew(TabbedPanel):
    fn = open('db_path', 'r')
    db_path = fn.read()
    fn.close()

    scn1 = 'blank_screen1'
    scn2 = 'blank_screen2'
    scn3 = 'blank_screen3'

    # kjs_180313: experimental

    # def switch_to(self, header):
    #     pass

    # def change_screen(self): # self is TabbedPanel
    #     tlist = self.tab_list
    #     self.switch_to(tlist[tlist.index(self.current_tab) - 1])

    # jhf production code

    def switch_to(self, header):
        # set the Screen manager to load the appropriate screen
        # linked to the tab head instead of loading content
        if header.name == 'tab1':
            self.manager.current = self.scn1
        elif header.name == 'tab2':
            self.manager.current = self.scn2
        elif header.name == 'tab3':
            self.manager.current = self.scn3
        elif header.name == 'tab4':
            self.manager.current = 'add_brew'
        # we have to replace the functionality of the original switch_to
        # kjs_180313: what does the above comment mean? i see that...
        # it was scraped from the web...
        # maybe it has something to do with the built-in "switch_to" function in...
        # https://kivy.org/docs/_modules/kivy/uix/tabbedpanel.html???
        # self.current_tab.state = 'normal'
        # kjs_180313: i believe the above line is redundant and can be removed because...
        # it is the default setting as opposed to 'down'
        header.state = 'down' # makes tab 1 start in the down position upon opening app since...
        # the default option is 'normal'
        self._current_tab = header
        # kjs_180315 based on jhf_180313 observations:
        # need the above line because otherwise...
        # if you enter data into the test screen and then...
        # load the test screen in a different tab, the data from...
        # the previous tab appears, and...
        # if you call up the test screen on a tab, go to a second tab, and...
        # return to the first tab, the first tab now shows the blank screen
        self.manager.transition = NoTransition() # prevents tabs from sliding left on transition

    # notes:
    # current_tab -- TabbedPanel
    # current_screen -- Screen manager  -- BlankScreen containing spinner
    # self.current_tab.name -- e.g., 'tab1'
    # self.manager.current_screen.screen.text -- e.g., blank_screen2
    # set self.manager.current equal to some self.manager.current_screen.screen.text
    # so self.manager.current should be something like 'blank_screen2'

    def change_screen(self):
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

    def create_brew(self):
        if not inval.check_brew(self.db_path, self.ab.brew_num.text):
            if inval.check_int(self.ab.batches.text):
                if inval.check_brand_size(self.db_path, self.ab.brand.text, self.ab.brew_size.text):
                    dbwrite.add_brew(self.db_path, self.ab.batches.text, self.ab.brew_num.text, self.ab.brew_size.text, self.ab.brand.text)
                    self.stat.text = 'Status - Brew number ' + self.ab.brew_num.text + ' has been added.'
                else: self.stat.text = 'Error - No process for brand and size.'
            else: self.stat.text = 'Error - Number of bacthes must be an integer.'
        else: self.stat.text = 'Error - Brew number aready exists.'


    def db_read(self):
        if inval.check_brew_batch(self.db_path, self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text):
            self.stat.text = 'Status: db_read'
            ############# db read from test table ###############
            if self.manager.current_screen.screen.text == 'test_screen':
                ts = {'test_screen1':self.ts1, 'test_screen2':self.ts2, 'test_screen3':self.ts3}
                x = self.manager.current
                ts[x].data1.text, ts[x].data2.text, ts[x].data3.text, error_duplicate = dbread.test(self.db_path, ts[x].brew_num.text, ts[x].batch_num.text)
                # relavent data is writent to the fields when page loads 
                # input is checked at begining of function
                # if everything works, remove code below.  jhf-184016
                # ts[x].data1.text = ''
                # ts[x].data2.text = ''
                # ts[x].data3.text = ''
                # if (ts[x].brew_num.text == '' or
                #     ts[x].batch_num.text ==''):
                #     error_inputs = '''A necessary input is missing.
                #     Please recheck inputs.'''
                #     self.stat.text = error_inputs
                # else:
                #     ts[x].data1.text, ts[x].data2.text, ts[x].data3.text, error_duplicate = dbread.test(self.db_path, ts[x].brew_num.text, ts[x].batch_num.text)
                #     if error_duplicate != []:
                #         self.stat.text = error_duplicate

            if self.manager.current_screen.screen.text == 'mash_screen':
                ms = {'mash_screen1':self.ms1, 'mash_screen2':self.ms2, 'mash_screen3':self.ms3}
                x = self.manager.current
                ms[x].dGRStemp.text, ms[x].dSTKtemp.text, ms[x].dMSHvol.text, ms[x].dMSHtemp.text, ms[x].dMSHtime.text, ms[x].dBREWsig.text, ms[x].dRNCvol.text, ms[x].dVLFtime.text, ms[x].dMASHph.text, ms[x].d1RNvol.text, ms[x].dSPGvol.text, ms[x].dROFtime.text, ms[x].dRACKcnt.text, ms[x].dFILLtime.text, ms[x].dFILLvol.text, ms[x].tsize.text, ms[x].tbrand.text , ms[x].tGRStemp.text , ms[x].tSTKtemp.text , ms[x].tMSHvol.text , ms[x].tMSHtemp.text , ms[x].tMASHphLOW.text , ms[x].tMASHphHI.text , ms[x].tSPGvol.text  = dbread.mash(self.db_path, ms[x].brew_num.text, ms[x].batch_num.text)
        #####################################################

    def db_write(self):
        if inval.check_brew_batch(self.db_path, self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text):
            self.stat.text = 'Status: db_write'
            ############# db write from test table ###############
            if self.manager.current_screen.screen.text == 'test_screen':
                ts = {'test_screen1':self.ts1, 'test_screen2':self.ts2, 'test_screen3':self.ts3}
                x = self.manager.current
                dbwrite.test(self.db_path, ts[x].brew_num.text, ts[x].batch_num.text, ts[x].data1.text, ts[x].data2.text, ts[x].data3.text)
            #####################################################

            ############# db write from mash table ###############
            if self.manager.current_screen.screen.text == 'mash_screen':
                ms = {'mash_screen1':self.ms1, 'mash_screen2':self.ms2, 'mash_screen3':self.ms3}
                x = self.manager.current
                dbwrite.mash(self.db_path,
                    ms[x].brew_num.text,
                    ms[x].batch_num.text,
                    ms[x].dGRStemp.text,
                    ms[x].dSTKtemp.text,
                    ms[x].dMSHvol.text,
                    ms[x].dMSHtemp.text,
                    ms[x].dMSHtime.text,
                    ms[x].dBREWsig.text,
                    ms[x].dRNCvol.text,
                    ms[x].dVLFtime.text,
                    ms[x].dMASHph.text,
                    ms[x].d1RNvol.text,
                    ms[x].dSPGvol.text,
                    ms[x].dROFtime.text,
                    ms[x].dRACKcnt.text,
                    ms[x].dFILLtime.text,
                    ms[x].dFILLvol.text)
            #####################################################

class BrewApp(App):
    def build(self):
        return Brew()

if __name__ == '__main__':
    BrewApp().run()