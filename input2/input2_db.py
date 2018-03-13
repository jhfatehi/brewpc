import sqlite3

conn = sqlite3.connect('input2_test2.db')
c = conn.cursor()
c.execute('''CREATE TABLE brew
             (brew_num, batch, size, brand, data1, data2, data3)''')

c.execute('''CREATE TABLE mash (
				brew_num,
				batch,
				size,
				brand,
				dGRStemp,
				dSTKtemp,
				dMSHvol,
				dMSHtemp,
				dMSHtime,
				dBREWsig,
				dRNCvol,
				dVLFtime,
				dMASHph,
				d1RNvol,
				dSPGvol,
				dROFtime,
				dRACKcnt,
				dFILLtime,
				dFILLvol,
				tGRStemp,
				tSTKtemp,
				tMSHvol,
				tMSHtemp,
				tMASHphLOW,
				tMASHphHI,
				tSPGvol
				)''')

c.execute('''CREATE TABLE process (
				size,
				brand,
				tGRStemp,
				tSTKtemp,
				tMSHvol,
				tMSHtemp,
				tMASHphLOW,
				tMASHphHI,
				tSPGvol
				)''')
conn.commit()
conn.close()