import sqlite3

con = sqlite3.connect("db.sqlite3")


con.execute("delete from pianoroom_admin_reserve")

con.commit()

con.close()
