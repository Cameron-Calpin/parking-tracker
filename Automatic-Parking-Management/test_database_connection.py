import mysql.connector
from mysql.connector import Error

try:
	mySQLconnection = mysql.connector.connect(user='root', password='Eaglescout#14',
		host='127.0.0.1',
		database='parking_tracker')

	cursor = mySQLconnection.cursor()
	val = "INSERT IGNORE INTO parking_tracker.indicator VALUES ('4'), ('5');"
	cursor.execute(val)

	sql_select_Query = "select * from parking_tracker.indicator"
	cursor.execute(sql_select_Query)
	records = cursor.fetchall()
	print("Total number of rows in python_developers is - ", cursor.rowcount)
	print ("Printing each row's column values i.e.  developer record")
	for row in records:
		print("park_id = ", row[0])
	cursor.close()

	mySQLconnection.commit()

except Error as e :
	print ("Error while connecting to MySQL", e)
finally:
	#closing database connection.
	if(mySQLconnection.is_connected()):
		mySQLconnection.close()
		print("MySQL connection is closed")
