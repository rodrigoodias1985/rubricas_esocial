import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    codigo,
    COUNT(*)
FROM rubricas_consultoria
GROUP BY codigo
HAVING COUNT(*) > 1
""")

duplicados = cursor.fetchall()

if duplicados:
    print("Códigos duplicados:")
    for codigo in duplicados:
        print(codigo)
else:
    print("Nenhum código duplicado encontrado.")

conn.close()