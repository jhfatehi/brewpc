import mysql.connector

def test(db_path, brew_num, batch_num):
    query = 'SELECT data1, data2, data3 FROM test WHERE brew_num = %s AND batch = %s'
    conn = mysql.connector.connect(
            user=db_path.get('mysql', 'usr'),
            password=db_path.get('mysql', 'pw'),
            host='127.0.0.1',
            database=db_path.get('mysql', 'db'),
            port=db_path.get('mysql', 'local_bind_port'))
    cur = conn.cursor()
    cur.execute(query, (brew_num, batch_num))
    rows = cur.fetchall()
    if len(rows) > 1:
        error_duplicate = '''You have duplicate database entries!
        Only values from the 1st row are used.'''
    else:
        error_duplicate = []
    data1 = rows[0][0]
    data2 = rows[0][1]
    data3 = rows[0][2]
    conn.close()
    return data1, data2, data3, error_duplicate

def mash(db_path, brew_num, batch_num):
    conn = mysql.connector.connect(
            user=db_path.get('mysql', 'usr'),
            password=db_path.get('mysql', 'pw'),
            host='127.0.0.1',
            database=db_path.get('mysql', 'db'),
            port=db_path.get('mysql', 'local_bind_port'))
    cur = conn.cursor()

    query = '''SELECT dGRStemp,
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
    dFILLvol FROM mash WHERE brew_num = %s AND batch = %s'''
    cur.execute(query, (brew_num, batch_num))
    rows = cur.fetchall()
    dGRStemp = str(rows[0][0])
    dSTKtemp = str(rows[0][1])
    dMSHvol = str(rows[0][2])
    dMSHtemp = str(rows[0][3])
    dMSHtime = str(rows[0][4])
    dBREWsig = str(rows[0][5])
    dRNCvol = str(rows[0][6])
    dVLFtime = str(rows[0][7])
    dMASHph = str(rows[0][8])
    d1RNvol = str(rows[0][9])
    dSPGvol = str(rows[0][10])
    dROFtime = str(rows[0][11])
    dRACKcnt = str(rows[0][12])
    dFILLtime = str(rows[0][13])
    dFILLvol = str(rows[0][14])

    query = '''SELECT process.* from process 
            left join mash on 
            process.size = mash.size and process.brand = mash.brand
            where mash.brew_num = %s and mash.batch = %s'''
    cur.execute(query, (brew_num, batch_num))
    rows = cur.fetchall()
    tsize = str(rows[0][0])
    tbrand = str(rows[0][1])
    tGRStemp = str(rows[0][2])
    tSTKtemp = str(rows[0][3])
    tMSHvol = str(rows[0][4])
    tMSHtemp = str(rows[0][5])
    tMASHphLOW = str(rows[0][6])
    tMASHphHI = str(rows[0][7])
    tSPGvol = str(rows[0][8])

    conn.close()
    return dGRStemp, dSTKtemp, dMSHvol, dMSHtemp, dMSHtime, dBREWsig, dRNCvol, dVLFtime, dMASHph, d1RNvol, dSPGvol, dROFtime, dRACKcnt, dFILLtime, dFILLvol, tsize, tbrand, tGRStemp, tSTKtemp, tMSHvol, tMSHtemp, tMASHphLOW, tMASHphHI, tSPGvol