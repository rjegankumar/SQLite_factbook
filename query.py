import sqlite3

def query(s):
	global c
	return c.execute(s).fetchall()

if __name__ == "__main__":
	conn = sqlite3.connect('factbook.db')
	c = conn.cursor()

	print(query('select name from facts order by population asc limit 10;'))

	conn.close()