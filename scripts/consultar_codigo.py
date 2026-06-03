import sqlite3
import sys

if len(sys.argv) != 2:
    print("Uso:")
    print("python consultar_codigo.py <codigo>")
    sys.exit()

codigo = sys.argv[1]

conn = sqlite3.connect("../database/rubricas_esocial.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM vw_rubricas_consolidadas
WHERE codigo = ?
""", (codigo,))

registro = cursor.fetchone()

if not registro:
    print(f"Código {codigo} não encontrado.")
    conn.close()
    sys.exit()

print("\n" + "=" * 60)
print(f"CÓDIGO: {registro['codigo']}")
print("=" * 60)

print(f"\nNome:")
print(registro["nome"])

print(f"\nDescrição:")
print(registro["descricao"])

print(f"\nOrigem:")
print(registro["origem"])

print("\n" + "-" * 60)
print("INSS")
print("-" * 60)

print("Incidência:", registro["inss_incidencia"])
print("Classificação:", registro["inss_classificacao"])
print("Base legal:", registro["inss_base_legal"])

print("\n" + "-" * 60)
print("IRRF")
print("-" * 60)

print("Incidência:", registro["irrf_incidencia"])
print("Classificação:", registro["irrf_classificacao"])
print("Base legal:", registro["irrf_base_legal"])

print("\n" + "-" * 60)
print("FGTS")
print("-" * 60)

print("Incidência:", registro["fgts_incidencia"])
print("Classificação:", registro["fgts_classificacao"])
print("Base legal:", registro["fgts_base_legal"])

if registro["exige_analise_irrf"] == "SIM":

    print("\n" + "⚠" * 20)
    print("ALERTA IRRF")
    print("⚠" * 20)

    print(registro["alerta_irrf"])

print("\n" + "-" * 60)
print("AVISO IMPORTANTE")
print("-" * 60)

print(registro["aviso_sistema"])

conn.close()