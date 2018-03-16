import sqlite3

def test(db_path, brew_num, batch_num, data1, data2, data3):
	conn = sqlite3.connect(db_path)
	c = conn.cursor()
	c.execute('''UPDATE brew
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
        brew_data.append((brew_num, ii+1, brew_size, brand, n,n,n)) #for test sheet.  remmove latter
        mash_data.append((brew_num, ii+1, brew_size, brand, n,n,n,n,n,n,n,n,n,n,n,n,n,n,n))
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.executemany('insert into brew values (?,?,?,?,?,?,?)', brew_data) #for test sheet.  remmove latter
    c.executemany('insert into mash values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', mash_data)
    conn.commit()
    conn.close()