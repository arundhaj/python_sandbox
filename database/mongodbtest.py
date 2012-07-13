from pymongo.connection import Connection
connection = Connection()

db = connection.test

cursor = db.test.find()
for d in cursor:
 print d
