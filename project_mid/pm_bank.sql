BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS history(
	"key"	INTEGER NOT NULL UNIQUE,
	"id_account"	INTEGER NOT NULL,
	"amount"	NUMERIC NOT NULL,
	"date_time"	TEXT NOT NULL,
	"from_name"	TEXT,
	"type"	TEXT,
	"ip"	TEXT,
	FOREIGN KEY("id_account") REFERENCES "pm_bank"("id_account"),
	PRIMARY KEY("key" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "user" (
	"id_account"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"first_name"	TEXT NOT NULL,
	"last_name"	TEXT NOT NULL,
	"phone"	TEXT NOT NULL,
	"balance"	NUMERIC NOT NULL DEFAULT 0.00,
	PRIMARY KEY("id_account")
);
COMMIT;
