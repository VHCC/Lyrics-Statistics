import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'F0973138343f', 'lyrics', charset='utf8')
cursor = db.cursor()

# execute SQL
cursor.execute("SELECT content FROM lyricsdb;")

# fetch result
results = cursor.fetchall()

# print
for record in results:
  col1 = record[0]
  print "%s" % (col1)

# close connection
db.close()