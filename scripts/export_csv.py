import MySQLdb
mydb = MySQLdb.connect(host = 'localhost',
		    user = 'root',
		    passwd = 'mysql',
		    db = 'cat_irk_1')
cur = mydb.cursor()
export = """SELECT name INTO OUTFILE '/tmp/suggest.csv' FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n' FROM catalog_goods WHERE 1"""
cur.execute(export)
