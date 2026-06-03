import sqlite3
import sys
import unicodedata


def remover_acentos(texto):
    if texto is None:
        return ""

    return "".join(
        c for c in unicodedata.normalize("NFD", str(texto))
        if unicodedata.category(c) != "Mn"
    ).upper()


if len(sys.argv) < 2:
    print("Uso:")
    print("python consultar_descricao.py <texto>")
    sys.exit()

texto_busca = " ".join(sys.argv[1:])
texto_busca_normalizado = remover_acentos(texto_busca)

conn = sqlite3.connect("../database/rubricas_esocial.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("""
SELECT
    codigo,
    nome,
    descricao,
    origem,
    exige_analise_irrf
FROM vw_rubricas_consolidadas
ORDER BY codigo
""")

resultados_nome = []
resultados_descricao = []

for registro in cursor.fetchall():

    nome = remover_acentos(registro["nome"])
    descricao = remover_acentos(registro["descricao"])

    encontrou_nome = texto_busca_normalizado in nome
    encontrou_descricao = texto_busca_normalizado in descricao

    if encontrou_nome:
        resultados_nome.append(registro)

    elif encontrou_descricao:
        resultados_descricao.append(registro)

print("\n" + "=" * 70)
print(f"RESULTADOS PARA: {texto_busca}")
print("=" * 70)

if not resultados_nome and not resultados_descricao:
    print("\nNenhuma rubrica encontrada.")
    conn.close()
    sys.exit()

if resultados_nome:

    print("\n" + "=" * 70)
    print("ENCONTRADO NO NOME")
    print("=" * 70)

    for registro in resultados_nome:

        alerta = ""

        if registro["exige_analise_irrf"] == "SIM":
            alerta = " ⚠ IRRF"

        print(
            f"{registro['codigo']} | "
            f"{registro['nome']}"
            f"{alerta}"
        )

if resultados_descricao:

    print("\n" + "=" * 70)
    print("ENCONTRADO APENAS NA DESCRIÇÃO")
    print("=" * 70)

    for registro in resultados_descricao:

        alerta = ""

        if registro["exige_analise_irrf"] == "SIM":
            alerta = " ⚠ IRRF"

        print(
            f"{registro['codigo']} | "
            f"{registro['nome']}"
            f"{alerta}"
        )

print(
    f"\nTotal encontrado: "
    f"{len(resultados_nome) + len(resultados_descricao)}"
)

conn.close()