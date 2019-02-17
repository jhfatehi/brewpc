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

    query = '''SELECT
                tGRStemp,
                tSTKtemp,
                tMSHvol,
                tMSHtemp,
                tMASHphLOW,
                tMASHphHI,
                tSPGvol,
                iWT1,
                iWT1lb,
                iWT2,
                iWT2lb,
                iWT3,
                iWT3lb,
                iWT4,
                iWT4lb,
                iWT5,
                iWT5lb,
                iGST1,
                iGST1sk,
                iGST1lb,
                iGST2,
                iGST2sk,
                iGST2lb,
                iGST3,
                iGST3sk,
                iGST3lb,
                iGST4,
                iGST4sk,
                iGST4lb,
                iGST5,
                iGST5sk,
                iGST5lb,
                iGST6,
                iGST6sk,
                iGST6lb,
                iGST7,
                iGST7sk,
                iGST7lb,
                iGSTtotlb
                from process 
            left join brews on 
            process.brand = brews.brand
            where brews.brew_num = %s'''
    cur.execute(query, (brew_num,))

    targets = {}
    rows = cur.fetchall()
    targets['tGRStemp'] = str(rows[0][0])
    targets['tSTKtemp'] = str(rows[0][1])
    targets['tMSHvol'] = str(rows[0][2])
    targets['tMSHtemp'] = str(rows[0][3])
    targets['tMASHphLOW'] = str(rows[0][4])
    targets['tMASHphHI'] = str(rows[0][5])
    targets['tSPGvol'] = str(rows[0][6])
    targets['iWT1'] = str(rows[0][7])
    targets['iWT1lb'] = str(rows[0][8])
    targets['iWT2'] = str(rows[0][9])
    targets['iWT2lb'] = str(rows[0][10])
    targets['iWT3'] = str(rows[0][11])
    targets['iWT3lb'] = str(rows[0][12])
    targets['iWT4'] = str(rows[0][13])
    targets['iWT4lb'] = str(rows[0][14])
    targets['iWT5'] = str(rows[0][15])
    targets['iWT5lb'] = str(rows[0][16])
    targets['iGST1'] = str(rows[0][17])
    targets['iGST1sk'] = str(rows[0][18])
    targets['iGST1lb'] = str(rows[0][19])
    targets['iGST2'] = str(rows[0][20])
    targets['iGST2sk'] = str(rows[0][21])
    targets['iGST2lb'] = str(rows[0][22])
    targets['iGST3'] = str(rows[0][23])
    targets['iGST3sk'] = str(rows[0][24])
    targets['iGST3lb'] = str(rows[0][25])
    targets['iGST4'] = str(rows[0][26])
    targets['iGST4sk'] = str(rows[0][27])
    targets['iGST4lb'] = str(rows[0][28])
    targets['iGST5'] = str(rows[0][29])
    targets['iGST5sk'] = str(rows[0][30])
    targets['iGST5lb'] = str(rows[0][31])
    targets['iGST6'] = str(rows[0][32])
    targets['iGST6sk'] = str(rows[0][33])
    targets['iGST6lb'] = str(rows[0][34])
    targets['iGST7'] = str(rows[0][35])
    targets['iGST7sk'] = str(rows[0][36])
    targets['iGST7lb'] = str(rows[0][37])
    targets['iGSTtotlb'] = str(rows[0][38])

    query = '''SELECT brand, batches, FV, strtDATE, finDATE from brews 
            where brews.brew_num = %s'''
    cur.execute(query, (brew_num,))

    brewfo = {}
    rows = cur.fetchall()
    brewfo['tbrand'] = str(rows[0][0])
    brewfo['tbatches'] = str(rows[0][1])
    brewfo['tFV'] = str(rows[0][2])
    brewfo['tstrtDATE'] = str(rows[0][3])
    brewfo['tfinDATE'] = str(rows[0][4])

    conn.close()
    #return dGRStemp, dSTKtemp, dMSHvol, dMSHtemp, dMSHtime, dBREWsig, dRNCvol, dVLFtime, dMASHph, d1RNvol, dSPGvol, dROFtime, dRACKcnt, dFILLtime, dFILLvol, tsize, tbrand, tGRStemp, tSTKtemp, tMSHvol, tMSHtemp, tMASHphLOW, tMASHphHI, tSPGvol
    return datas, targets, brewfo