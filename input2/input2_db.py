
import sqlite3

conn = sqlite3.connect('input2_test.db')
c = conn.cursor()
c.execute('''CREATE TABLE brew
             (brew_num, batch, size, brand, data1, data2, data3)''')
conn.commit()
conn.close()