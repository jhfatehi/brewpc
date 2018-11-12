import mysql.connector

def check_brew_batch(db_path, brew_num, batch):
	query = '''SELECT count(1)
				from mash
				where brew_num = %s and batch_num = %s'''
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=db_path.get('mysql', 'local_bind_port'))
	cur = conn.cursor()
	cur.execute(query, (brew_num, batch))
	rows = cur.fetchall()
	return rows[0][0]	

def check_brew(db_path, brew_num):
	query = '''SELECT count(1)
				from brews
				where brew_num = %s'''
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=db_path.get('mysql', 'local_bind_port'))
	cur = conn.cursor()
	cur.execute(query, (brew_num,))
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
			where brand = %s and size = %s'''
	conn = mysql.connector.connect(
			user=db_path.get('mysql', 'usr'),
			password=db_path.get('mysql', 'pw'),
			host='127.0.0.1',
			database=db_path.get('mysql', 'db'),
			port=db_path.get('mysql', 'local_bind_port'))
	cur = conn.cursor()
	cur.execute(query, (brand, size))
	rows = cur.fetchall()
	return rows[0][0]