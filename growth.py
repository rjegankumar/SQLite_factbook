import sqlite3
import pandas as pd
import math

def population_2050(facts_df_row):
	init_popl = facts_df_row['population']
	popl_growth = facts_df_row['population_growth']/100
	return init_popl*(math.e**(popl_growth*35))

if __name__ == "__main__":
	
	conn = sqlite3.connect('factbook.db')

	facts_df = pd.read_sql_query('select * from facts', conn)
	facts_df = facts_df.dropna(axis = 0)

	facts_df['population_2050'] = facts_df.apply(population_2050, axis=1)
	facts_df = facts_df.sort_values('population_2050', ascending=False)
	print(facts_df.loc[:,['name','population','population_growth','population_2050']].head(10))

	conn.close()