import mysql.connector

print('starting..')

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Dennis@2017.'
)


#prepare a cursor object
#cursorObject = dataBase.cursor()

#create a database
#cursorObject.execute('CREATE DATABASE hermanos_db')

print('All Done!')

dataBase.close()