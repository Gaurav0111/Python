import sqlite3


def table():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS general_store (item  TEXT , quantity  INTEGER , price  REAL)")
    con.commit()
    con.close()

def insert(item,quantity,price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO general_store VALUES(?,?,?)",(item,quantity,price))
    con.commit()
    con.close()

def delete(item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM general_store WHERE item=? ",(item,))
    con.commit()
    con.close()

def update(item,price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("UPDATE general_store SET price=? WHERE ITEM=? ",(price,item))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM general_store")
    rows = cur.fetchall()
    con.close()
    print(rows)



insert("biscuit",10,50)
delete("biscuit")
update("Glass",20)
view()