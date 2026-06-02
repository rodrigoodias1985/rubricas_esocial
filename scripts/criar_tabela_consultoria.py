import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS rubricas_consultoria (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    codigo TEXT NOT NULL,

    nome TEXT,
    dt_inicio TEXT,
    dt_fim TEXT,

    descricao TEXT,
    incidencia_exclusiva_empregado TEXT,

    inss_incidencia TEXT,
    inss_classificacao TEXT,
    base_legal_inss TEXT,

    irrf_incidencia TEXT,
    irrf_classificacao TEXT,
    base_legal_irrf TEXT,

    fgts_incidencia TEXT,
    fgts_classificacao TEXT,
    base_legal_fgts TEXT,

    observacoes TEXT,
    tipo_registro TEXT,

    data_importacao DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

print("Tabela rubricas_consultoria criada com sucesso.")

conn.close()