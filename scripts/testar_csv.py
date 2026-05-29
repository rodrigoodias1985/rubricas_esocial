import pandas as pd

arquivo = "../dados/Tabela 03 esocial.csv"

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="latin1",
    dtype=str
)

print(df.head())

print("\nColunas encontradas:")
print(df.columns.tolist())

print(f"\nTotal de registros: {len(df)}")