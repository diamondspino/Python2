import sqlite3
conn = sqlite3.connect (r"D:\Patrick_python\final\project_mid\bankkk.db")
c = conn.cursor() #crate a cusor object
c.execute ('''CREATE TABLE history(
	"key"	INTEGER NOT NULL UNIQUE,
	"id_account"	INTEGER NOT NULL,
	"amount"	NUMERIC NOT NULL,
	"date_time"	TEXT NOT NULL,
	"from_name"	TEXT,
	"type"	TEXT,
	"ip"	TEXT,
	FOREIGN KEY("id_account") REFERENCES "pm_bank"("id_account"),
	PRIMARY KEY("key" AUTOINCREMENT))''')
c.execute ('''CREATE TABLE "user" (
	"id_account"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"phone"	TEXT NOT NULL,
	"balance"	NUMERIC NOT NULL DEFAULT 0.00,
	PRIMARY KEY("id_account"))''')
conn.commit()
conn.close()

# for delete table
# DROP TABLE history;


#The TRUNCATE TABLE statement is used to delete the data inside a table, but not the table itself.
# TRUNCATE TABLE history;

