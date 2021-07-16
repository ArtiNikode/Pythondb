import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='artinikode',database='bookstoredb')
curs=con.cursor()

try:
    bc=int(input('Enter bookcode: '))
    bm=input('Enter bookname: ')
    ct=input('Enter category: ')
    at=input('Enter author name: ')
    pb=input('Enter publication: ')
    ed=int(input('Enter edition: '))
    pr=int(input('Enter price: '))

    curs.execute("insert into books values(%d,'%s','%s','%s','%s','%d',%.2f)" %(bc,bm,ct,at,pb,ed,pr))
    con.commit()

    print('Book inserted Successfully.......')

except:
    print('Error inserting data.....')

con.close()