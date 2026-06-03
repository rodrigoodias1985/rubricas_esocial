import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM vw_rubricas_consolidadas
""")

print("Total registros:", cursor.fetchone()[0])

cursor.execute("""
SELECT
    codigo,
    nome,
    irrf_classificacao,
    exige_analise_irrf
FROM vw_rubricas_consolidadas
WHERE exige_analise_irrf = 'SIM'
LIMIT 20
""")

print("\nExemplos com IRRF 00:\n")

for linha in cursor.fetchall():
    print(linha)

conn.close()