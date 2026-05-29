import pandas as pd

df = pd.read_csv(
    "../dados/Tabela 03 esocial.csv",
    sep=";",
    encoding="latin1",
    dtype=str
)

codigos_erro = [
    "1001","1012","1015","1016","1017","1018","1019",
    "1216","1217","1411","1412","1619","1651","1652"
]

resultado = df[df["CODIGO"].isin(codigos_erro)]

print(
    resultado[
        ["CODIGO","NOME","DTINICIO","DTFIM"]
    ]
)