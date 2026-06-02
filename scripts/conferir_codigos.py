import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM rubricas
""")

total_api = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(DISTINCT codigo)
FROM rubricas_consultoria
""")

total_consultoria = cursor.fetchone()[0]

print(f"Registros API: {total_api}")
print(f"Registros Consultoria: {total_consultoria}")

conn.close()