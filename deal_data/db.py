#coding:utf-8
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

#获取当日成交量
def get_day_volumn_33_66(day):
	db_host = 'localhost'
	db_user = 'root'
	db_password = ''
	db_name = 'securities_master'
	con = mdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

	with con:
		cur = con.cursor()
		cur.execute('SELECT volume from daily_price where (price_date="%s")' % day)
		day_volume = cur.fetchall()
		day_volume = [int(day_volume[i][0]) for i in range(len(day_volume))]
 		return day_volume


#get data by tickerId
def get_10_50_by_id(ticker_id):
	db_host = 'localhost'
	db_user = 'root'
	db_password = ''
	db_name = 'securities_master'
	con = mdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

	with con:
		cur = con.cursor()
		cur.execute('SELECT price_date,open_price,high_price,low_price,close_price,volume from daily_price where (symbol_id = %s) and (price_date BETWEEN "20150101" AND "20151231") and (high_price BETWEEN 10 and 50)' % ticker_id)	
		daily_data = cur.fetchall()
		return daily_data


