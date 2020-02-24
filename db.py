import pymysql

class DBConnection:
	def __init__(self,host,user,password,database,charset,port):
		self.connection = pymysql.connect(
			host=host,
			user=user,
			password=password,
			db=database,
			charset=charset,
			port=port,
			cursorclass=pymysql.cursors.DictCursor)

	def exec_select_rnd(self,seq):
		with self.connection.cursor() as cursor:
			query = Query().get_select_rnd(seq)
			cursor.execute(query)
			for row in cursor:
				data = row.get('cnt')
		return data	

	def exec_insert_rnd(self,seq,kind,title,period,goverment,posted,summary,support,papers,point,question): 
		query = Query().get_insert_rnd(seq,kind,title,period,goverment,posted,summary,support,papers,point,question) 
		with self.connection as cur:
			cur.execute(query)

	def close(self):
		self.connection.close()

	def commit(self):
		self.connection.commit()

class Query:
	def get_select_rnd(self,seq):
		query = 'select \
		count(*) as cnt \
		from rnd \
		where seq=\'{}\''.format(seq)

		return query

	def get_insert_rnd(self,seq,kind,title,period,goverment,posted,summary,support,papers,point,question):
		query = 'insert into rnd (seq,kind,title,period,goverment,posted,summary,support,papers,point,question) \
		values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(seq,kind,title,period,goverment,posted,summary,support,papers,point,question)

		return query		