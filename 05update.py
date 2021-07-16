import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='artinikode',database='bookstoredb')
curs=con.cursor()
try:
    bcode=int(input('Enter Book code : '))

    curs.execute("select * from books where bookcode=%d" %bcode)
    rec=curs.fetchone()

    if rec:
        tr=input('Enter price (increase/decrease) : ')
        price=float(input('Enter New Price : '))

        if tr.lower().startswith('i'):
            curs.execute("update books set price=price+%.2f where bookcode=%d" %(price,bcode))
        else:
            curs.execute("update books set price=price-%.2f where bookcode=%d" %(price,bcode))

        con.commit()
        print('Price updated Successfully.....')

        con.close()
    else:
        print('Bookcode does not exist......')
except:
    print('Invalid input...')