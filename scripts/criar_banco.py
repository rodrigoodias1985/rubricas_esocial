import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")

cursor = conn.cursor()

# ======================================
# TABELA PRINCIPAL DE RUBRICAS
# ======================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS rubricas (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    codigo TEXT UNIQUE,
    nome TEXT,
    descricao TEXT,
    tipo TEXT,

    dt_inicio TEXT,
    dt_fim TEXT,
    incidencia_exclusiva_empregado TEXT,

    inss_incidencia TEXT,
    inss_classificacao TEXT,
    inss_base_legal TEXT,

    irrf_incidencia TEXT,
    irrf_classificacao TEXT,
    irrf_base_legal TEXT,

    fgts_incidencia TEXT,
    fgts_classificacao TEXT,
    fgts_base_legal TEXT,

    sindical_incidencia TEXT,
    sindical_classificacao TEXT,
    sindical_base_legal TEXT,

    dsr INTEGER,
    ferias INTEGER,
    aviso_previo INTEGER,
    decimo_terceiro INTEGER,
    afastamento INTEGER,

    data_importacao DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# ======================================
# TABELA DE LOG DE IMPORTAÇÃO
# ======================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS log_importacao (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    codigo TEXT,
    status TEXT,
    mensagem TEXT,

    data_execucao DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")