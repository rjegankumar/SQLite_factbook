import sqlite3

def query(s):
	global c
	return c.execute(s).fetchall()

if __name__ == "__main__":
	conn = sqlite3.connect('factbook.db')
	c = conn.cursor()

	total_land_area = query('select sum(area_land) from facts where area_land !="" and area_water !="";')
	total_water_area = query('select sum(area_water) from facts where area_land !="" and area_water !="";')
	print(total_land_area[0][0]/total_water_area[0][0])

	conn.close()