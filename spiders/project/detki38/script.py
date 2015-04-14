import MySQLdb
mydb = MySQLdb.connect(host = 'localhost',
		    user = 'root',
		    passwd = 'mysql',
		    db = 'irkdb')
cur = mydb.cursor()
delete1 = "DELETE FROM search_goods WHERE id BETWEEN 1040001 AND 1050000"
cur.execute(delete1)
