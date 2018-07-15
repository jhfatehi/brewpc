#import mysql.connector
import mysql.connector

def xNone(s):
    if s == '':
        return None
    return str(s)

def test(db_path, brew_num, batch_num, data1, data2, data3):
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=int(db_path.get('mysql', 'local_bind_port')))
	c = conn.cursor()
	c.execute('''UPDATE test
			SET data1 = %s, data2 = %s, data3 = %s
			WHERE brew_num = %s AND batch = %s''', 
			(data1, data2, data3, brew_num, batch_num))
	conn.commit()
	conn.close()

def add_brew(db_path, batches, brew_num, brew_size, brand):
	n = 'none'
	brew_data = []
	mash_data = []
	for ii in range(int(batches)):
		brew_data.append((brew_num, str(ii+1), brew_size, brand)) #for test sheet.  remmove latter
		mash_data.append((brew_num, str(ii+1), brew_size, brand))
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=int(db_path.get('mysql', 'local_bind_port')))
	c = conn.cursor()
	c.executemany('INSERT into test (brew_num, batch, size, brand) values (%s,%s,%s,%s)', brew_data) #for test sheet.  remmove latter
	c.executemany('INSERT into mash (brew_num, batch, size, brand) values (%s,%s,%s,%s)', mash_data)
	conn.commit()
	conn.close()

def mash(db_path,
	brew_num,
	batch_num,
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
	dFILLvol):
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=int(db_path.get('mysql', 'local_bind_port')))
	c = conn.cursor()
	c.execute('''UPDATE mash
			SET dGRStemp = %s,
			dSTKtemp = %s,
			dMSHvol = %s,
			dMSHtemp = %s,
			dMSHtime = %s,
			dBREWsig = %s,
			dRNCvol = %s,
			dVLFtime = %s,
			dMASHph = %s,
			d1RNvol = %s,
			dSPGvol = %s,
			dROFtime = %s,
			dRACKcnt = %s,
			dFILLtime = %s,
			dFILLvol = %s
			WHERE brew_num = %s AND batch = %s''',
			(xNone(dGRStemp),
			xNone(dSTKtemp),
			xNone(dMSHvol),
			xNone(dMSHtemp),
			xNone(dMSHtime),
			xNone(dBREWsig),
			xNone(dRNCvol),
			xNone(dVLFtime),
			xNone(dMASHph),
			xNone(d1RNvol),
			xNone(dSPGvol),
			xNone(dROFtime),
			xNone(dRACKcnt),
			xNone(dFILLtime),
			xNone(dFILLvol),
			xNone(brew_num),
			xNone(batch_num)))
	conn.commit()
	conn.close()