import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM rubricas_consultoria
""")

total = cursor.fetchone()[0]

print(f"Total de registros: {total}")

conn.close()