import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    codigo,
    status,
    mensagem
FROM log_importacao
WHERE status = 'ERRO'
ORDER BY codigo
""")

erros = cursor.fetchall()

print(f"\nTotal de erros: {len(erros)}\n")

for erro in erros:
    print(erro)

conn.close()