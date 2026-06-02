import pandas as pd
import sqlite3

ARQUIVO = "../dados/rubricas_consultoria_preenchida e Validada.xlsx"

df = pd.read_excel(ARQUIVO)

df = df.rename(columns={
    "DESCRICAO": "descricao",
    "INCIDENCIAEXCLUSIVAEMPREGADO": "incidencia_exclusiva_empregado"
})

conn = sqlite3.connect("../database/rubricas_esocial.db")

df.to_sql(
    "rubricas_consultoria",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print(f"{len(df)} registros importados com sucesso.")