import sqlite3
con = sqlite3.connect("mdsbalance.db")

rows = con.execute("select plantid, PlantName FROM Plants")

for row in rows:
  print (row)

