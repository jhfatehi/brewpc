import sqlite3

def test(db_path, brew_num, batch_num):
    query = 'SELECT data1, data2, data3 FROM test WHERE brew_num = ? AND batch = ?'
    conn = sqlite3.connect(db_path)
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
    return data1, data2, data3, error_duplicate

def mash(db_path, brew_num, batch_num):
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
    dFILLvol FROM mash WHERE brew_num = ? AND batch = ?'''
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query, (brew_num, batch_num))
    rows = cur.fetchall()

    dGRStemp = rows[0][0]
    dSTKtemp = rows[0][1]
    dMSHvol = rows[0][2]
    dMSHtemp = rows[0][3]
    dMSHtime = rows[0][4]
    dBREWsig = rows[0][5]
    dRNCvol = rows[0][6]
    dVLFtime = rows[0][7]
    dMASHph = rows[0][8]
    d1RNvol = rows[0][9]
    dSPGvol = rows[0][10]
    dROFtime = rows[0][11]
    dRACKcnt = rows[0][12]
    dFILLtime = rows[0][13]
    dFILLvol = rows[0][14]

    return dGRStemp, dSTKtemp, dMSHvol, dMSHtemp, dMSHtime, dBREWsig, dRNCvol, dVLFtime, dMASHph, d1RNvol, dSPGvol, dROFtime, dRACKcnt, dFILLtime, dFILLvol