import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM rubricas r
INNER JOIN rubricas_consultoria c
    ON r.codigo = c.codigo
""")

print("Códigos presentes nas duas tabelas:", cursor.fetchone()[0])

conn.close()