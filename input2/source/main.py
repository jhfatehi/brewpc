'''
print to Status / Error message as follows:
self.stat.text = 'Status or Error Message'
'''

import dbwrite
import dbread

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
# kjs_180313: let's try leaving it commented and see if anything breaks
# from kivy.properties import ObjectProperty
# Builder also appears to be unused
# from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition
#from kivy.config import Config
#Config.set('graphics', 'window_state', 'maximized')
#Config.write()


class Brew(TabbedPanel):
    fn = open('db_path', 'r')
    db_path = fn.read()
    fn.close()

    #jhf 180307 i think some of these ObjectProperty declatations might not be required
    #because they are inherited from the class through brew.kv.
    #not sure.  need to test. seems to work with stat
    # kjs_180313: let's try leaving them commented and see if anything breaks and...
    # if not we can delete them later
    # manager = ObjectProperty(None)
    # ts1 = ObjectProperty()
    # ts2 = ObjectProperty()
    # ts3 = ObjectProperty()

    # ab = ObjectProperty()
    # blk1 = ObjectProperty()
    # blk2 = ObjectProperty()
    # blk3 = ObjectProperty()

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

    def test_write(self):
        ts = {'test_screen1':self.ts1, 'test_screen2':self.ts2, 'test_screen3':self.ts3}
        x = self.manager.current
        dbwrite.test(self.db_path, ts[x].brew_num.text, ts[x].batch_num.text, ts[x].data1.text, ts[x].data2.text, ts[x].data3.text)

    def mash_write(self):
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

    def create_brew(self):
        print(self.ab.batches.text)
        print(type(self.ab.batches.text))
        if (self.ab.brew_num.text == '' or
            self.ab.brew_size.text =='' or
            self.ab.brand.text == '' or
            self.ab.batches.text == ''):
            error_inputs = '''A necessary input is missing.
            Please recheck inputs.'''
            self.stat.text = error_inputs
        else:
            dbwrite.add_brew(self.db_path, self.ab.batches.text, self.ab.brew_num.text, self.ab.brew_size.text, self.ab.brand.text)
            # n = 'none'
            # data = []
            # for ii in range(int(self.ab.batches.text)):
            #     data.append((str(self.ab.brew_num.text), str(ii+1), str(self.ab.brew_size.text), self.ab.brand.text, n,n,n))
            # conn = sqlite3.connect(self.db_path)
            # c = conn.cursor()
            # c.executemany('insert into brew values (?,?,?,?,?,?,?)', data)
            # conn.commit()
            # conn.close()

    def db_read(self):
        #db read from test table
        if self.manager.current_screen.screen.text == 'test_screen':
            ts = {'test_screen1':self.ts1, 'test_screen2':self.ts2, 'test_screen3':self.ts3}
            x = self.manager.current
            ts[x].data1.text = ''
            ts[x].data2.text = ''
            ts[x].data3.text = ''
            if (ts[x].brew_num.text == '' or
                ts[x].batch_num.text ==''):
                error_inputs = '''A necessary input is missing.
                Please recheck inputs.'''
                self.stat.text = error_inputs
            else:
                ts[x].data1.text, ts[x].data2.text, ts[x].data3.text, error_duplicate = dbread.test(self.db_path, ts[x].brew_num.text, ts[x].batch_num.text)
                if error_duplicate != []:
                    self.stat.text = error_duplicate


class BrewApp(App):
    def build(self):
        return Brew()


if __name__ == '__main__':
    BrewApp().run()