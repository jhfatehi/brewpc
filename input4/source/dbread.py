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
    dFILLvol,
    dMASHnote
     FROM mash WHERE brew_num = %s AND batch_num = %s'''
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
    datas['dMASHnote'] = xstr(rows[0][15])

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

def boil(db_path, brew_num, batch_num):
    conn = mysql.connector.connect(
            user=db_path.get('mysql', 'usr'),
            password=db_path.get('mysql', 'pw'),
            host='127.0.0.1',
            database=db_path.get('mysql', 'db'),
            port=db_path.get('mysql', 'local_bind_port'))
    cur = conn.cursor()

    query = '''SELECT 
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
        dBOILnote
     FROM boil WHERE brew_num = %s AND batch_num = %s'''
    cur.execute(query, (brew_num, batch_num))
    
    datas = {}
    rows = cur.fetchall()
    datas['dBOILtime'] = xtime(rows[0][0])
    datas['dHOP1time'] = xtime(rows[0][1])
    datas['dIGp'] = xstr(rows[0][2])
    datas['dIPH'] = xstr(rows[0][3])
    datas['dLIQ1gal'] = xstr(rows[0][4])
    datas['dHOP2time'] = xtime(rows[0][5])
    datas['dZINCtime'] = xtime(rows[0][6])
    datas['dKICKtime'] = xtime(rows[0][7])
    datas['dHOP3time'] = xtime(rows[0][8])
    datas['dMESLVLbbl'] = xstr(rows[0][9])
    datas['dMESGp'] = xstr(rows[0][10])
    datas['dLIQ2gal'] = xstr(rows[0][11])
    datas['dFNLLVLbbl'] = xstr(rows[0][12])
    datas['dFNLGp'] = xstr(rows[0][13])
    datas['dFNLPH'] = xstr(rows[0][14])
    datas['dBOILnote'] = xstr(rows[0][15])

    query = '''SELECT
                tFG,
                tBOILphLO,
                tBOILphHI,
                iZNg,
                iKICKoz,
                iHOP1,
                iHOP1kg,
                iHOP1min,
                iHOP2,
                iHOP2kg,
                iHOP2min,
                iHOP3,
                iHOP3kg,
                iHOP3min,
                iHOP4,
                iHOP4kg,
                iHOP4min,
                iHOP5,
                iHOP5kg,
                iHOP5min,
                iHOP6,
                iHOP6kg,
                iHOP6min,
                iHOP7,
                iHOP7kg,
                iHOP7min
                from process 
            left join brews on 
            process.brand = brews.brand
            where brews.brew_num = %s'''
    cur.execute(query, (brew_num,))

    targets = {}
    rows = cur.fetchall()
    targets['tFG'] = str(rows[0][0])
    targets['tBOILphLO'] = str(rows[0][1])
    targets['tBOILphHI'] = str(rows[0][2])
    targets['iZNg'] = str(rows[0][3])
    targets['iKICKoz'] = str(rows[0][4])
    targets['iHOP1'] = str(rows[0][5])
    targets['iHOP1kg'] = str(rows[0][6])
    targets['iHOP1min'] = str(rows[0][7])
    targets['iHOP2'] = str(rows[0][8])
    targets['iHOP2kg'] = str(rows[0][9])
    targets['iHOP2min'] = str(rows[0][10])
    targets['iHOP3'] = str(rows[0][11])
    targets['iHOP3kg'] = str(rows[0][12])
    targets['iHOP3min'] = str(rows[0][13])
    targets['iHOP4'] = str(rows[0][14])
    targets['iHOP4kg'] = str(rows[0][15])
    targets['iHOP4min'] = str(rows[0][16])
    targets['iHOP5'] = str(rows[0][17])
    targets['iHOP5kg'] = str(rows[0][18])
    targets['iHOP5min'] = str(rows[0][19])
    targets['iHOP6'] = str(rows[0][20])
    targets['iHOP6kg'] = str(rows[0][21])
    targets['iHOP6min'] = str(rows[0][22])
    targets['iHOP7'] = str(rows[0][23])
    targets['iHOP7kg'] = str(rows[0][24])
    targets['iHOP7min'] = str(rows[0][25])


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