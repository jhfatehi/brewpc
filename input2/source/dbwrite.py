import sqlite3

def test(db_path, brew_num, batch_num, data1, data2, data3):
	conn = sqlite3.connect(db_path)
	c = conn.cursor()
	c.execute('''UPDATE test
           SET data1 = ?, data2 = ?, data3 = ?
           WHERE brew_num = ? AND batch = ?''', 
           (data1, data2, data3, brew_num, batch_num))
	conn.commit()
	conn.close()

def add_brew(db_path, batches, brew_num, brew_size, brand):
    n = 'none'
    brew_data = []
    mash_data = []
    for ii in range(int(batches)):
        brew_data.append((brew_num, str(ii+1), brew_size, brand, n,n,n)) #for test sheet.  remmove latter
        mash_data.append((brew_num, str(ii+1), brew_size, brand, n,n,n,n,n,n,n,n,n,n,n,n,n,n,n))
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.executemany('insert into test values (?,?,?,?,?,?,?)', brew_data) #for test sheet.  remmove latter
    c.executemany('insert into mash values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', mash_data)
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
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''UPDATE mash
           SET dGRStemp = ?,
           dSTKtemp = ?,
           dMSHvol = ?,
           dMSHtemp = ?,
           dMSHtime = ?,
           dBREWsig = ?,
           dRNCvol = ?,
           dVLFtime = ?,
           dMASHph = ?,
           d1RNvol = ?,
           dSPGvol = ?,
           dROFtime = ?,
           dRACKcnt = ?,
           dFILLtime = ?,
           dFILLvol = ?
           WHERE brew_num = ? AND batch = ?''',
           (dGRStemp,
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
            brew_num,
            batch_num))
    conn.commit()
    conn.close()