import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")

cursor = conn.cursor()

cursor.execute("""
DELETE FROM rubricas_consultoria
""")

conn.commit()

print("Tabela rubricas_consultoria limpa com sucesso.")

conn.close()