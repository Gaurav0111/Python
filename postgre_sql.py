import psycopg2


def table():
    con = psycopg2.connect(" dbname='data1' user='postgres' password='postgres1234' host='localhost' port='5432' ")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS general_store (item  TEXT , quantity  INTEGER , price  REAL)")
    con.commit()
    con.close()

def insert(item,quantity,price):
    con = psycopg2.connect(" dbname='data1' user='postgres' password='postgres1234' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("INSERT INTO general_store VALUES(%s,%s,%s)",(item,quantity,price))
    con.commit()
    con.close()

def delete(item):
    con = psycopg2.connect(" dbname='data1' user='postgres' password='postgres1234' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("DELETE FROM general_store WHERE item=%s ",(item,))
    con.commit()
    con.close()

def update(item,price):
    con = psycopg2.connect(" dbname='data1' user='postgres' password='postgres1234' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("UPDATE general_store SET price=%s WHERE ITEM=%s ",(price,item))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect(" dbname='data1' user='postgres' password='postgres1234' host='localhost' port='5432'")
    cur = con.cursor()
    cur.execute("SELECT * FROM general_store")
    rows = cur.fetchall()
    con.close()
    print(rows)


table()
insert("Apple",10,50)
insert("biscuit",10,50)
delete("biscuit")
update("Apple",20)
view()