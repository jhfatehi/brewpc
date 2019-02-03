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
    
    datas = {}
    rows = cur.fetchall()
    datas['dGRStemp'] = xstr(rows[0][0])
    datas['dSTKtemp'] = xstr(rows[0][1])
    datas['dMSHvol'] = xstr(rows[0][2])
    datas['dMSHtemp'] = xstr(rows[0][3])
    datas['dMSHtime'] = xtime(rows[0][4])
    datas['dBREWsig'] = xstr(rows[0][5])
    datas['dRNCvol'] = xstr(rows[0][6])
    datas['dVLFtime'] = xtime(rows[0][7])
    datas['dMASHph'] = xstr(rows[0][8])
    datas['d1RNvol'] = xstr(rows[0][9])
    datas['dSPGvol'] = xstr(rows[0][10])
    datas['dROFtime'] = xtime(rows[0][11])
    datas['dRACKcnt'] = xstr(rows[0][12])
    datas['dFILLtime'] = xtime(rows[0][13])
    datas['dFILLvol'] = xstr(rows[0][14])

    query = '''SELECT process.* from process 
            left join brews on 
            process.brand = brews.brand
            where brews.brew_num = %s'''
    cur.execute(query, (brew_num,))

    targets = {}
    rows = cur.fetchall()
    targets['tbrand'] = str(rows[0][0])
    targets['tGRStemp'] = str(rows[0][1])
    targets['tSTKtemp'] = str(rows[0][2])
    targets['tMSHvol'] = str(rows[0][3])
    targets['tMSHtemp'] = str(rows[0][4])
    targets['tMASHphLOW'] = str(rows[0][5])
    targets['tMASHphHI'] = str(rows[0][6])
    targets['tSPGvol'] = str(rows[0][7])

    query = '''SELECT batches from brews 
            where brews.brew_num = %s'''
    cur.execute(query, (brew_num,))

    rows = cur.fetchall()
    batches = str(rows[0][0])

    conn.close()
    #return dGRStemp, dSTKtemp, dMSHvol, dMSHtemp, dMSHtime, dBREWsig, dRNCvol, dVLFtime, dMASHph, d1RNvol, dSPGvol, dROFtime, dRACKcnt, dFILLtime, dFILLvol, tsize, tbrand, tGRStemp, tSTKtemp, tMSHvol, tMSHtemp, tMASHphLOW, tMASHphHI, tSPGvol
    return datas, targets, batches