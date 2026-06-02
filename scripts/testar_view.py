import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM vw_rubricas_consolidadas
""")

print("Total de códigos oficiais:", cursor.fetchone()[0])

conn.close()