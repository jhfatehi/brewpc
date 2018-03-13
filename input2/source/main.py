'''
print to Status / Error message as follows:
self.stat.text = 'Status or Error Message'
'''

import dbwrite
import sqlite3

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.lang import Builder
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
    manager = ObjectProperty(None)
    ts1 = ObjectProperty()
    ts2 = ObjectProperty()
    ts3 = ObjectProperty()

    ab = ObjectProperty()
    blk1 = ObjectProperty()
    blk2 = ObjectProperty()
    blk3 = ObjectProperty()

    tab1 = 'blank_screen1'
    tab2 = 'test_screen2'
    tab3 = 'test_screen3'

    def switch_to(self, header):
        # set the Screen manager to load  the appropriate screen
        # linked to the tab head instead of loading content
        if header.name == 'tab1':
            self.manager.current = self.tab1
        elif header.name == 'tab2':
            self.manager.current = self.tab2
        elif header.name == 'tab3':
            self.manager.current = self.tab3
        elif header.name == 'tab4':
            self.manager.current = 'add_brew'
        # we have to replace the functionality of the original switch_to
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header
        self.manager.transition = NoTransition()
    
    def change_screen(self):
        if self.current_tab.name == 'tab1':
            self.tab1 = self.manager.current_screen.screen.text+'1'
            r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
            self.manager.current = self.tab1
            self.manager.current_screen.screen.text = self.tab1[0:-1]
            self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
        elif self.current_tab.name == 'tab2':
            self.tab2 = self.manager.current_screen.screen.text+'2'
            r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
            self.manager.current = self.tab2
            self.manager.current_screen.screen.text = self.tab2[0:-1]
            self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
        elif self.current_tab.name == 'tab3':
            self.tab3 = self.manager.current_screen.screen.text+'3'
            r,a = self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text
            self.manager.current = self.tab3
            self.manager.current_screen.screen.text = self.tab3[0:-1]
            self.manager.current_screen.brew_num.text, self.manager.current_screen.batch_num.text = r,a
            
    def test_write(self):
        ts = {'test_screen1':self.ts1, 'test_screen2':self.ts2, 'test_screen3':self.ts3}
        x = self.manager.current
        dbwrite.test(self.db_path, ts[x].brew_num.text, ts[x].batch_num.text, ts[x].data1.text, ts[x].data2.text, ts[x].data3.text)

    def create_brew(self):
        n = 'none'
        data = []
        for ii in range(int(self.ab.batches.text)):
            data.append((str(self.ab.brew_num.text), str(ii+1), str(self.ab.brew_size.text), self.ab.brand.text, n,n,n))
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.executemany('insert into brew values (?,?,?,?,?,?,?)', data)
        conn.commit()
        conn.close()
    
    # kjs 180313 -- in progress / incomplete
    def test_read(self):
        import sqlite3
        brew_num = '1'
        batch = '1'
        query = 'select data1, data2, data3 from brew where brew_num=' + brew_num + ' and batch=' + batch
        con = sqlite3.connect('input2_test.db')
        cursor = con.execute(query)
        rows = cursor.fetchall()
        print(rows)

class BrewApp(App):
    def build(self):
        return Brew()

if __name__ == '__main__':
    BrewApp().run()