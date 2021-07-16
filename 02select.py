import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='artinikode',database='bookstoredb')
curs=con.cursor()

curs.execute("select * from books")
data=curs.fetchall()

for rec in data:
    print(rec)
    
con.close()