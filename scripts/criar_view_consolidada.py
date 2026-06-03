import sqlite3

conn = sqlite3.connect("../database/rubricas_esocial.db")
cursor = conn.cursor()

cursor.execute("""
DROP VIEW IF EXISTS vw_rubricas_consolidadas
""")

cursor.execute("""
CREATE VIEW vw_rubricas_consolidadas AS

-- REGISTROS DA API (com prioridade para CONSULTORIA)

SELECT

    r.codigo,

    COALESCE(c.nome, r.nome) AS nome,
    COALESCE(c.descricao, r.descricao) AS descricao,

    COALESCE(c.dt_inicio, r.dt_inicio) AS dt_inicio,
    COALESCE(c.dt_fim, r.dt_fim) AS dt_fim,

    COALESCE(
        c.incidencia_exclusiva_empregado,
        r.incidencia_exclusiva_empregado
    ) AS incidencia_exclusiva_empregado,

    COALESCE(c.inss_incidencia, r.inss_incidencia) AS inss_incidencia,
    COALESCE(c.inss_classificacao, r.inss_classificacao) AS inss_classificacao,
    COALESCE(c.base_legal_inss, r.inss_base_legal) AS inss_base_legal,

    COALESCE(c.irrf_incidencia, r.irrf_incidencia) AS irrf_incidencia,
    COALESCE(c.irrf_classificacao, r.irrf_classificacao) AS irrf_classificacao,
    COALESCE(c.base_legal_irrf, r.irrf_base_legal) AS irrf_base_legal,

    COALESCE(c.fgts_incidencia, r.fgts_incidencia) AS fgts_incidencia,
    COALESCE(c.fgts_classificacao, r.fgts_classificacao) AS fgts_classificacao,
    COALESCE(c.base_legal_fgts, r.fgts_base_legal) AS fgts_base_legal,

    r.sindical_incidencia,
    r.sindical_classificacao,
    r.sindical_base_legal,

    r.dsr,
    r.ferias,
    r.aviso_previo,
    r.decimo_terceiro,
    r.afastamento,

    c.observacoes,
c.tipo_registro,

CASE
    WHEN SUBSTR(
        COALESCE(c.irrf_classificacao, r.irrf_classificacao),
        1,
        2
    ) = '00'
    THEN 'SIM'
    ELSE 'NAO'
END AS exige_analise_irrf,

CASE
    WHEN SUBSTR(
        COALESCE(c.irrf_classificacao, r.irrf_classificacao),
        1,
        2
    ) = '00'
    THEN 'ATENÇÃO: Esta natureza possui classificação IRRF iniciada pelo código 00. A definição entre os códigos 09 ou 79 deverá ser realizada pelo usuário conforme a finalidade da verba e seus reflexos no Informe de Rendimentos.'
    ELSE NULL
END AS alerta_irrf,

'IMPORTANTE: As informações apresentadas neste sistema possuem caráter orientativo e foram elaboradas com base na Tabela 03 do eSocial, legislação vigente e entendimento técnico da consultoria. A definição final da incidência tributária, previdenciária e fundiária de cada verba deve ser realizada pelo usuário, considerando as particularidades da rubrica cadastrada.' AS aviso_sistema,

CASE
    WHEN c.codigo IS NOT NULL THEN 'CONSULTORIA'
    ELSE 'API'
END AS origem

FROM rubricas r

LEFT JOIN rubricas_consultoria c
    ON r.codigo = c.codigo

UNION ALL

-- REGISTROS EXCLUSIVOS DA CONSULTORIA

SELECT

    c.codigo,
    c.nome,
    c.descricao,
    c.dt_inicio,
    c.dt_fim,

    c.incidencia_exclusiva_empregado,

    c.inss_incidencia,
    c.inss_classificacao,
    c.base_legal_inss,

    c.irrf_incidencia,
    c.irrf_classificacao,
    c.base_legal_irrf,

    c.fgts_incidencia,
    c.fgts_classificacao,
    c.base_legal_fgts,

    NULL,
    NULL,
    NULL,

    NULL,
    NULL,
    NULL,
    NULL,
    NULL,

    c.observacoes,
    c.tipo_registro,

    CASE
        WHEN SUBSTR(c.irrf_classificacao,1,2) = '00'
        THEN 'SIM'
        ELSE 'NAO'
    END,

    CASE
        WHEN SUBSTR(c.irrf_classificacao,1,2) = '00'
        THEN 'ATENÇÃO: Esta natureza está classificada como 00 - Rendimento não tributável. A definição entre os códigos 09 ou 79 deverá ser realizada pelo usuário conforme a finalidade da verba e seus reflexos no Informe de Rendimentos.'
        ELSE NULL
    END,

    'IMPORTANTE: As informações apresentadas neste sistema possuem caráter orientativo e foram elaboradas com base na Tabela 03 do eSocial, legislação vigente e entendimento técnico da consultoria. A definição final da incidência tributária, previdenciária e fundiária de cada verba deve ser realizada pelo usuário, considerando as particularidades da rubrica cadastrada.',

    'CONSULTORIA'

FROM rubricas_consultoria c

WHERE NOT EXISTS (
    SELECT 1
    FROM rubricas r
    WHERE r.codigo = c.codigo
)
""")

conn.commit()

print("VIEW vw_rubricas_consolidadas atualizada com sucesso.")

conn.close()