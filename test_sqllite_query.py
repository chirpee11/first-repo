import sqlite3
con = sqlite3.connect("mdsbalance.db")

cur = con.cursor()

res = cur.execute("select plantid, PlantName FROM Plants")

print (res.fetchone())

