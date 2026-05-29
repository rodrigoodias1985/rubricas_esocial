import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    codigo,
    nome,
    inss_classificacao,
    irrf_classificacao,
    fgts_classificacao
FROM rubricas
""")

dados = cursor.fetchall()

for linha in dados:
    print(linha)

conn.close()