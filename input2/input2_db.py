import sqlite3

db_path = 'brewpc_database_v1.db'

conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('''CREATE TABLE test
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
				dFILLvol
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


#secton below is for initializing database with some recepies.
#comment out this section if you don't want to initialize

conn = sqlite3.connect(db_path)
c = conn.cursor()

size = '60'
brand = 'evil_twin'
tGRStemp = '69'
tSTKtemp = '164'
tMSHvol = '700'
tMSHtemp = '151'
tMASHphLOW = '5.0'
tMASHphHI = '5.4'
tSPGvol = '725'
c.execute('INSERT INTO process VALUES (?,?,?,?,?,?,?,?,?)', (size,
															brand,
															tGRStemp,
															tSTKtemp,
															tMSHvol,
															tMSHtemp,
															tMASHphLOW,
															tMASHphHI,
															tSPGvol))

# size = '11'
# brand = '11111111111'
# tGRStemp = '11'
# tSTKtemp = '111'
# tMSHvol = '111'
# tMSHtemp = '111'
# tMASHphLOW = '1.1'
# tMASHphHI = '1.1'
# tSPGvol = '1'
# c.execute('INSERT INTO process VALUES (?,?,?,?,?,?,?,?,?)', (size,
# 															brand,
# 															tGRStemp,
# 															tSTKtemp,
# 															tMSHvol,
# 															tMSHtemp,
# 															tMASHphLOW,
# 															tMASHphHI,
# 															tSPGvol))

# size = '22'
# brand = '222222222222'
# tGRStemp = '22'
# tSTKtemp = '222'
# tMSHvol = '222'	
# tMSHtemp = '222'
# tMASHphLOW = '2.2'
# tMASHphHI = '2.2'
# tSPGvol = '222'
# c.execute('INSERT INTO process VALUES (?,?,?,?,?,?,?,?,?)', (size,
# 															brand,
# 															tGRStemp,
# 															tSTKtemp,
# 															tMSHvol,
# 															tMSHtemp,
# 															tMASHphLOW,
# 															tMASHphHI,
# 															tSPGvol))
	
conn.commit()
conn.close()