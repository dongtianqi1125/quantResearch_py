import MySQLdb as mdb




#get name
def get_tickers_from_db():
	db_host = 'localhost'
	db_user = 'root'
	db_password = ''
	db_name = 'securities_master'
	con = mdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

	#get name form symbol;
	with con:
		cur = con.cursor()
		cur.execute('SELECT ticker,name FROM symbol')
		data = cur.fetchall()
		return data

#get data by tickerId
def get_10_50_by_id(ticker_id):
	db_host = 'localhost'
	db_user = 'root'
	db_password = ''
	db_name = 'securities_master'
	con = mdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

	with con:
		cur = con.cursor()
		cur.execute('SELECT price_date,close_price from daily_price where (symbol_id = %s) and (price_date BETWEEN "20100101" AND "20151231")' % ticker_id)	
		# cur.execute('SELECT all from daily_price where (symbol_id = %s) and (price_date BETWEEN "20100101" and "20151231")' % ticker_id)
		daily_data = cur.fetchall()
		return daily_data


