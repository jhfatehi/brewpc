import sqlite3

def check_brew_batch(db_path, brew_num, batch):
	query = '''SELECT count(1)
				from mash
				where brew_num = ? and batch = ?'''
	conn = sqlite3.connect(db_path)
	cur = conn.cursor()
	cur.execute(query, (brew_num, batch))
	rows = cur.fetchall()
	return rows[0][0]	

def check_brew(db_path, brew_num):
	query = '''SELECT count(1)
				from mash
				where brew_num = ?'''
	conn = sqlite3.connect(db_path)
	cur = conn.cursor()
	cur.execute(query, (brew_num))
	rows = cur.fetchall()
	return rows[0][0]

def check_int(x):
	try:
		int(x)
	except:
		return 0
	return 1

def check_brand_size(db_path, brand, size):
	query = '''SELECT count(1)
			from process
			where brand = ? and size = ?'''
	conn = sqlite3.connect(db_path)
	cur = conn.cursor()
	cur.execute(query, (brand, size))
	rows = cur.fetchall()
	return rows[0][0]