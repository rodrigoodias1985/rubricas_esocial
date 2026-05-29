import sqlite3
import pandas as pd
import requests
import time

# ======================================
# CONFIGURAÇÕES
# ======================================

ARQUIVO_CSV = "../dados/Tabela 03 esocial.csv"

API_URL = "https://www.lefisc.com.br/api/rubricas/api/pegaRubrica/{}"

TEMPO_ESPERA = 1.5

# ======================================
# CONEXÃO COM BANCO
# ======================================

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

# ======================================
# LEITURA DO CSV
# ======================================

df = pd.read_csv(
    ARQUIVO_CSV,
    sep=";",
    encoding="latin1",
    dtype=str
)

total = len(df)

print(f"\nTotal de registros encontrados: {total}\n")

sucesso = 0
erros = 0

# ======================================
# IMPORTAÇÃO
# ======================================

for indice, linha in df.iterrows():

    codigo = str(linha["CODIGO"]).strip()

    print(f"[{indice + 1}/{total}] Importando código {codigo}...")

    try:

        response = requests.get(
            API_URL.format(codigo),
            timeout=15
        )

        if response.status_code != 200:

            cursor.execute("""
            INSERT INTO log_importacao
            (codigo, status, mensagem)
            VALUES (?, ?, ?)
            """, (
                codigo,
                "ERRO",
                f"HTTP {response.status_code}"
            ))

            conn.commit()

            erros += 1
            continue

        dados = response.json()

        if not dados:

            cursor.execute("""
            INSERT INTO log_importacao
            (codigo, status, mensagem)
            VALUES (?, ?, ?)
            """, (
                codigo,
                "ERRO",
                "Sem retorno da API"
            ))

            conn.commit()

            erros += 1
            continue

        rubrica = dados[0]

        cursor.execute("""
        INSERT OR REPLACE INTO rubricas (

            codigo,
            nome,
            descricao,
            tipo,

            dt_inicio,
            dt_fim,
            incidencia_exclusiva_empregado,

            inss_incidencia,
            inss_classificacao,
            inss_base_legal,

            irrf_incidencia,
            irrf_classificacao,
            irrf_base_legal,

            fgts_incidencia,
            fgts_classificacao,
            fgts_base_legal,

            sindical_incidencia,
            sindical_classificacao,
            sindical_base_legal,

            dsr,
            ferias,
            aviso_previo,
            decimo_terceiro,
            afastamento

        )
        VALUES (
            ?, ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?,
            ?, ?, ?, ?, ?
        )
        """, (

            rubrica.get("codigo"),
            rubrica.get("nome"),
            rubrica.get("descricao"),
            rubrica.get("tipo"),

            linha.get("DTINICIO"),
            linha.get("DTFIM"),
            linha.get("INCIDENCIAEXCLUSIVAEMPREGADO"),

            rubrica.get("insSincidencia"),
            rubrica.get("insSclassificacao"),
            rubrica.get("insSbaselegal"),

            rubrica.get("iRincidencia"),
            rubrica.get("iRclassificacao"),
            rubrica.get("iRbaselegal"),

            rubrica.get("fgtSincidencia"),
            rubrica.get("fgtSclassificacao"),
            rubrica.get("fgtSbaselegal"),

            rubrica.get("cSincidencia"),
            rubrica.get("cSclassificacao"),
            rubrica.get("cSbaselegal"),

            int(rubrica.get("dsr", False)),
            int(rubrica.get("ferias", False)),
            int(rubrica.get("avisO_PREVIO", False)),
            int(rubrica.get("decimoterceirosalario", False)),
            int(rubrica.get("afastamento", False))

        ))

        cursor.execute("""
        INSERT INTO log_importacao
        (codigo, status, mensagem)
        VALUES (?, ?, ?)
        """, (
            codigo,
            "SUCESSO",
            "Importado com sucesso"
        ))

        conn.commit()

        sucesso += 1

        time.sleep(TEMPO_ESPERA)

    except Exception as erro:

        cursor.execute("""
        INSERT INTO log_importacao
        (codigo, status, mensagem)
        VALUES (?, ?, ?)
        """, (
            codigo,
            "ERRO",
            str(erro)
        ))

        conn.commit()

        erros += 1

# ======================================
# RESUMO FINAL
# ======================================

print("\n--------------------------------")
print("IMPORTAÇÃO FINALIZADA")
print("--------------------------------")
print(f"Sucesso: {sucesso}")
print(f"Erros: {erros}")
print("--------------------------------")

conn.close()