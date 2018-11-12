import mysql.connector
import time

def xstr(s):
    if s is None:
        return ''
    return str(s)

def xtime(s):
    if s is None:
        return ''
    s = str(s)
    x = time.strptime(s, '%H:%M:%S')
    return time.strftime('%H%M', x)


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
    dFILLvol FROM mash WHERE brew_num = %s AND batch_num = %s'''
    cur.execute(query, (brew_num, batch_num))
    rows = cur.fetchall()
    dGRStemp = xstr(rows[0][0])
    dSTKtemp = xstr(rows[0][1])
    dMSHvol = xstr(rows[0][2])
    dMSHtemp = xstr(rows[0][3])
    dMSHtime = xtime(rows[0][4])
    dBREWsig = xstr(rows[0][5])
    dRNCvol = xstr(rows[0][6])
    dVLFtime = xtime(rows[0][7])
    dMASHph = xstr(rows[0][8])
    d1RNvol = xstr(rows[0][9])
    dSPGvol = xstr(rows[0][10])
    dROFtime = xtime(rows[0][11])
    dRACKcnt = xstr(rows[0][12])
    dFILLtime = xtime(rows[0][13])
    dFILLvol = xstr(rows[0][14])

    # query = '''SELECT process.* from process 
    #         left join mash on 
    #         process.size = mash.size and process.brand = mash.brand
    #         where mash.brew_num = %s and mash.batch_num = %s'''
    query = '''SELECT process.* from process 
            left join brews on 
            process.size = brews.size and process.brand = brews.brand
            where brews.brew_num = %s'''
    cur.execute(query, (brew_num,))
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