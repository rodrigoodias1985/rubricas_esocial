import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

for codigo in ['1016', '1017', '1800']:

    print("\n" + "="*80)
    print(f"CÓDIGO: {codigo}")
    print("="*80)

    cursor.execute("""
    SELECT
        codigo,
        nome,
        tipo_registro,
        observacoes
    FROM rubricas_consultoria
    WHERE codigo = ?
    """, (codigo,))

    for linha in cursor.fetchall():
        print(linha)

conn.close()