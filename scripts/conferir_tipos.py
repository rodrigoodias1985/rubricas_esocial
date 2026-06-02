import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    tipo_registro,
    COUNT(*)
FROM rubricas_consultoria
GROUP BY tipo_registro
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()