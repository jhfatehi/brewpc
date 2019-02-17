import mysql.connector

def xNone(s):
    if s == '':
        return None
    return str(s)

def add_process(db_path,
	brand,
	tGRStemp,
	tSTKtemp,
	tMSHvol,
	tMSHtemp,
	tMASHphLOW,
	tMASHphHI,
	tSPGvol):
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=int(db_path.get('mysql', 'local_bind_port')))
	c = conn.cursor()
	c.execute('''INSERT INTO process (brand,
		tGRStemp,
		tSTKtemp,
		tMSHvol,
		tMSHtemp,
		tMASHphLOW,
		tMASHphHI,
		tSPGvol) values (%s, %s, %s, %s, %s, %s, %s, %s)''',
		(xNone(brand),
		tGRStemp,
		tSTKtemp,
		tMSHvol,
		tMSHtemp,
		tMASHphLOW,
		tMASHphHI,
		tSPGvol))
	conn.commit()
	conn.close()

def add_brew(db_path, batches, brew_num, brand):
	new_data = []
	for ii in range(int(batches)):
		new_data.append((brew_num, str(ii+1)))
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=int(db_path.get('mysql', 'local_bind_port')))
	c = conn.cursor()
	c.execute('INSERT into brews (brew_num, batches, brand) values (%s,%s,%s)', [brew_num, batches, brand])
	c.executemany('INSERT into mash (brew_num, batch_num) values (%s,%s)', new_data)
	c.executemany('INSERT into boil (brew_num, batch_num) values (%s,%s)', new_data)
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
	d1RNp,
	dSPGvol,
	dROFtime,
	dRACKcnt,
	dFILLtime,
	dFILLvol,
	dMASHnote):
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
			d1RNp = %s,
			dSPGvol = %s,
			dROFtime = %s,
			dRACKcnt = %s,
			dFILLtime = %s,
			dFILLvol = %s,
			dMASHnote = %s
			WHERE brew_num = %s AND batch_num = %s''',
			(xNone(dGRStemp),
			xNone(dSTKtemp),
			xNone(dMSHvol),
			xNone(dMSHtemp),
			xNone(dMSHtime),
			xNone(dBREWsig),
			xNone(dRNCvol),
			xNone(dVLFtime),
			xNone(dMASHph),
			xNone(d1RNp),
			xNone(dSPGvol),
			xNone(dROFtime),
			xNone(dRACKcnt),
			xNone(dFILLtime),
			xNone(dFILLvol),
			xNone(dMASHnote),
			xNone(brew_num),
			xNone(batch_num)))
	conn.commit()
	conn.close()

def boil(db_path,
	brew_num,
	batch_num,
	dBOILtime,
	dHOP1time,
	dIGp,
	dIPH,
	dLIQ1gal,
	dHOP2time,
	dZINCtime,
	dKICKtime,
	dHOP3time,
	dMESLVLbbl,
	dMESGp,
	dLIQ2gal,
	dFNLLVLbbl,
	dFNLGp,
	dFNLPH,
	dBOILnote):
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=int(db_path.get('mysql', 'local_bind_port')))
	c = conn.cursor()
	c.execute('''UPDATE boil SET
			dBOILtime = %s,
			dHOP1time = %s,
			dIGp = %s,
			dIPH = %s,
			dLIQ1gal = %s,
			dHOP2time = %s,
			dZINCtime = %s,
			dKICKtime = %s,
			dHOP3time = %s,
			dMESLVLbbl = %s,
			dMESGp = %s,
			dLIQ2gal = %s,
			dFNLLVLbbl = %s,
			dFNLGp = %s,
			dFNLPH = %s,
			dBOILnote = %s
			WHERE brew_num = %s AND batch_num = %s''',
			(xNone(dBOILtime),
			xNone(dHOP1time),
			xNone(dIGp),
			xNone(dIPH),
			xNone(dLIQ1gal),
			xNone(dHOP2time),
			xNone(dZINCtime),
			xNone(dKICKtime),
			xNone(dHOP3time),
			xNone(dMESLVLbbl),
			xNone(dMESGp),
			xNone(dLIQ2gal),
			xNone(dFNLLVLbbl),
			xNone(dFNLGp),
			xNone(dFNLPH),
			xNone(dBOILnote),
			xNone(brew_num),
			xNone(batch_num)))
	conn.commit()
	conn.close()