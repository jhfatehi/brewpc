import sqlite3
import sys
if sys.version_info[0] > 2:
    raise "Must be using Python 2"

size = raw_input('Size? ')
brand = raw_input('Brand? ')
tGRStemp = raw_input('Grist Temp? ')
tSTKtemp = raw_input('Strike Temp? ')
tMSHvol = raw_input('Mash Volume? ')
tMSHtemp = raw_input('Mash Temperature? ')
tMASHphLOW = raw_input('Low Mash pH? ')
tMASHphHI = raw_input('High Mash pH? ')
tSPGvol = raw_input('Sparge Volume? ')

fn = open('source/db_path', 'r')
db_path = fn.read()
fn.close()
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('INSERT INTO process VALUES (?,?,?,?,?,?,?,?,?)', (size,
															brand,
															tGRStemp,
															tSTKtemp,
															tMSHvol,
															tMSHtemp,
															tMASHphLOW,
															tMASHphHI,
															tSPGvol))
conn.commit()
conn.close()