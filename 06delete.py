import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='artinikode',database='bookstoredb')
curs=con.cursor()

bc=int(input('Enter bookcode : '))

curs.execute("select * from books where bookcode=%d" %bc)
rec=curs.fetchone()

try:
    print("Book Code:%d" %rec[0])
    print("Book Name : %s" %rec[1])
    print("Category : %s" %rec[2])
    print("Author : %s" %rec[3])
    print("Publication : %s" %rec[4])
    print("Edition : %d" %rec[5])
    print("Price : %.2f" %rec[6])

    curs.execute("delete from books where bookcode=%d" %bc)
    bcode=input('Do you want to delete?(yes/no)')
    while bcode.upper()=='YES':
        print('Book Deleted Successfully......')
        con.commit()

except:
    print('Book Not found......')

con.close()