import sqlite3
import pandas as pd

# ======================================
# CONEXÃO COM BANCO
# ======================================

conn = sqlite3.connect(
    "../database/rubricas_esocial.db"
)

# ======================================
# CONSULTA DOS ERROS
# ======================================

query = """
SELECT DISTINCT

    r.codigo,
    r.nome,
    r.dt_inicio,
    r.dt_fim,

    l.status,
    l.mensagem

FROM rubricas r

INNER JOIN log_importacao l
    ON r.codigo = l.codigo

WHERE l.status = 'ERRO'

ORDER BY r.codigo
"""

# ======================================
# CARREGA NO DATAFRAME
# ======================================

df = pd.read_sql_query(query, conn)

# ======================================
# EXPORTA PARA EXCEL
# ======================================

arquivo_saida = "../dados/rubricas_pendentes.xlsx"

df.to_excel(
    arquivo_saida,
    index=False
)

conn.close()

# ======================================
# MENSAGEM FINAL
# ======================================

print("\n--------------------------------")
print("ARQUIVO EXPORTADO COM SUCESSO")
print("--------------------------------")
print(f"Total pendências: {len(df)}")
print(f"Arquivo: {arquivo_saida}")
print("--------------------------------")