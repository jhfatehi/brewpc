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