import sqlite3
import pandas as pd

conn = sqlite3.connect("../database/rubricas_esocial.db")

query = """
SELECT
    r.codigo,
    r.nome,
    r.descricao,
    r.dt_inicio,
    r.dt_fim
FROM rubricas r
LEFT JOIN log_importacao l
    ON r.codigo = l.codigo
WHERE l.status = 'ERRO'
"""

df = pd.read_sql_query(query, conn)

df.to_excel(
    "../dados/rubricas_pendentes.xlsx",
    index=False
)

conn.close()

print("Arquivo gerado com sucesso!")