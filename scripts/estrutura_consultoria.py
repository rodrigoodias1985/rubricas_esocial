import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(rubricas_consultoria)")

for coluna in cursor.fetchall():
    print(coluna)

conn.close()