import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='artinikode',database='bookstoredb')
curs=con.cursor()

at=input('Enter Author: ')
curs.execute("select * from books where author='%s'" %at)
rec=curs.fetchone()

pb=input('Enter Publication: ')
curs.execute("select * from books where publication='%s'" %pb)
rec=curs.fetchone()
    
if rec:
    print(rec[1])
else:
    print("Book not Found.....")    

con.close()    