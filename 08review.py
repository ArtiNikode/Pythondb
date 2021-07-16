import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='artinikode',database='bookstoredb')
curs=con.cursor()

try:
    bcode=int(input('Enter Book code : '))

    curs.execute("select * from books where bookcode=%d" %bcode)
    rec=curs.fetchone()

    if rec:

        reviews=input('Enter Reviews: ')
       
        curs.execute("update books set review='{a1}' where bookcode={a2}".format(a1=reviews,a2=bcode))
        
        con.commit()
        print('Reviwed Enter successfully......')

        con.close()

    else:
        print('Book does not exist......')
except:
    print('Invalid input...')