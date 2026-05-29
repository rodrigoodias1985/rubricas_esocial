import sqlite3
import pandas as pd

# ======================================
# CONEXÃO
# ======================================

conn = sqlite3.connect(
    "../database/rubricas_esocial.db"
)

# ======================================
# LEITURA DO CSV OFICIAL
# ======================================

df_csv = pd.read_csv(
    "../dados/Tabela 03 esocial.csv",
    sep=";",
    encoding="latin1",
    dtype=str
)

# ======================================
# BUSCA OS CÓDIGOS COM ERRO
# ======================================

query = """
SELECT DISTINCT codigo
FROM log_importacao
WHERE status = 'ERRO'
"""

df_erros = pd.read_sql_query(query, conn)

# ======================================
# FILTRA NO CSV
# ======================================

df_final = df_csv[
    df_csv["CODIGO"].isin(df_erros["codigo"])
].copy()

# ======================================
# RENOMEIA COLUNAS
# ======================================

df_final.rename(columns={

    "CODIGO": "codigo",
    "NOME": "nome",
    "DTINICIO": "dt_inicio",
    "DTFIM": "dt_fim"

}, inplace=True)

# ======================================
# CRIA COLUNAS PARA CONSULTORIA
# ======================================

df_final["inss_incidencia"] = ""
df_final["inss_classificacao"] = ""

df_final["irrf_incidencia"] = ""
df_final["irrf_classificacao"] = ""

df_final["fgts_incidencia"] = ""
df_final["fgts_classificacao"] = ""

df_final["observacoes"] = ""

# ======================================
# EXPORTA PARA EXCEL
# ======================================

arquivo_saida = "../dados/rubricas_consultoria.xlsx"

df_final.to_excel(
    arquivo_saida,
    index=False
)

conn.close()

# ======================================
# FINALIZAÇÃO
# ======================================

print("\n--------------------------------")
print("PLANILHA GERADA COM SUCESSO")
print("--------------------------------")
print(f"Total registros: {len(df_final)}")
print(f"Arquivo: {arquivo_saida}")
print("--------------------------------")