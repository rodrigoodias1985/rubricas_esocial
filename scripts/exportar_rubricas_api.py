import sqlite3
import pandas as pd

conn = sqlite3.connect("../database/rubricas_esocial.db")

query = """
SELECT
    codigo,
    nome,
    descricao,

    inss_incidencia,
    inss_classificacao,
    inss_base_legal,

    irrf_incidencia,
    irrf_classificacao,
    irrf_base_legal,

    fgts_incidencia,
    fgts_classificacao,
    fgts_base_legal,

    sindical_incidencia,
    sindical_classificacao,
    sindical_base_legal,

    dsr,
    ferias,
    aviso_previo,
    decimo_terceiro,
    afastamento
FROM rubricas
ORDER BY codigo
"""

df = pd.read_sql(query, conn)

arquivo_saida = "../dados/rubricas_api.xlsx"

df.to_excel(arquivo_saida, index=False)

print(f"Arquivo gerado: {arquivo_saida}")

conn.close()