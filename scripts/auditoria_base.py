import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

print("\n=== API ===")

cursor.execute("""
SELECT COUNT(*)
FROM rubricas
""")
print("Total registros:", cursor.fetchone()[0])

cursor.execute("""
SELECT COUNT(DISTINCT codigo)
FROM rubricas
""")
print("Códigos únicos:", cursor.fetchone()[0])

print("\n=== CONSULTORIA ===")

cursor.execute("""
SELECT COUNT(*)
FROM rubricas_consultoria
""")
print("Total registros:", cursor.fetchone()[0])

cursor.execute("""
SELECT COUNT(DISTINCT codigo)
FROM rubricas_consultoria
""")
print("Códigos únicos:", cursor.fetchone()[0])

conn.close()