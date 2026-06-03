import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")

cursor = conn.cursor()

cursor.execute("""
ALTER TABLE rubricas_consultoria
ADD COLUMN exige_analise_irrf TEXT
""")

conn.commit()

print("Coluna exige_analise_irrf criada com sucesso.")

conn.close()