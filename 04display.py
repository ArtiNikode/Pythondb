import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='artinikode',database='bookstoredb')
curs=con.cursor()

ct=input('Enter book category: ')
curs.execute("select * from books where category='%s'"%ct)

rec=curs.fetchall()

for rec in rec:
    print(rec[1])

con.close()    