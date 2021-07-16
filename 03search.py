import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='artinikode',database='bookstoredb')
curs=con.cursor()

bc=int(input('Enter bookcode: '))

curs.execute("select bookname,category,author,publication,edition,price from books where bookcode=%d" %bc)
rec=curs.fetchone()


try:
    print("Book Name : %s" %rec[1])
    print("Category : %s" %rec[2])
    print("Author : %s" %rec[3])
    print("Publication : %s" %rec[4])
    print("Edition : %d" %rec[5])
    print("Price : %.2f" %rec[6])
    
except:
    print('Book Not found......')

con.close()