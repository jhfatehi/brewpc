import sqlite3

def test(db_path, brew_num, batch_num):
    query = 'select data1, data2, data3 from test where brew_num=' + '"' + brew_num + '"' + ' and batch=' + '"' + batch_num + '"'
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
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