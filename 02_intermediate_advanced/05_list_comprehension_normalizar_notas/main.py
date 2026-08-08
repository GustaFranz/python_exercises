# ==============================================================================
# DEMANDA DE TRABALHO (TICKET)
# Empresa: Secretaria Municipal de Educação
# Setor: Gestão Pública Escolar / Dados
#
# CONTEXTO:
# As escolas enviaram um lote de notas para a base temporária (staging).
# Antes de publicar esses dados no dashboard da rede, você precisa sanitizar
# a lista e gerar um relatório de auditoria sobre a qualidade dos dados.
# ==============================================================================
# 1. DADOS DE ENTRADA (BASE STAGING)
# A lista abaixo contém erros propositais (strings, nulos e valores fora da escala).
# ------------------------------------------------------------------------------
# notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]
# ------------------------------------------------------------------------------
# 2. REGRAS DE NEGÓCIO E VALIDAÇÃO
# Uma nota só é considerada VÁLIDA se atender a TODAS as condições:
#   a) Tipo: Numérico (int ou float). 
#      *Atenção: Booleans (True/False) devem ser desconsiderados!
#   b) Intervalo: Estritamente de 0.0 até 10.0 .
# ------------------------------------------------------------------------------
# 3. O QUE VOCÊ DEVE DESENVOLVER (REQUISITOS)
# Utilize LIST COMPREHENSION para resolver as Etapas 1, 2 e 3:
# [ ] Etapa 1: notas_validas
#     Filtre a lista 'notas_brutas' mantendo apenas os elementos válidos.
# [ ] Etapa 2: notas_arredondadas
#     A partir de 'notas_validas', garanta que todas as notas estejam
#     arredondadas para 1 casa decimal (dica: use round(nota, 1)).
# [ ] Etapa 3: status_lote
#     Crie uma lista de dicionários mapeando a nota e a situação do aluno.
#     - Regra: nota >= 6.0 -> "aprovado" | nota < 6.0 -> "recuperacao"
#     - Formato do item: {"nota": 7.5, "status": "aprovado"}
# [ ] Etapa 4: Relatório de Auditoria
#     Calcule e exiba no terminal os seguintes indicadores:
#       1) Qtd total de notas recebidas
#       2) Qtd total de notas descartadas
#       3) Percentual de descarte (%)
#       4) Média geral das notas válidas
#       5) Qtd total de aprovados e de recuperações
#       6) A lista final formatada (status_lote)
# ------------------------------------------------------------------------------
# 4. DICAS TÉCNICAS E FÓRMULAS
# - Checagem de tipo exato (evita booleans):
#   isinstance(n, (int, float)) and not isinstance(n, bool)
# - Qtd de notas descartadas:
#   len(notas_brutas) - len(notas_validas)
# - If ternário no List Comprehension (Etapa 3):
#   "aprovado" if nota >= 6.0 else "recuperacao"
# ------------------------------------------------------------------------------
# 5. EXEMPLO DE SAÍDA ESPERADA NO TERMINAL:
# === RELATÓRIO DE AUDITORIA DO LOTE ===
# Total recebidas:  12
# Total descartadas: 5
# % Descartadas:     41.67%
# Média das válidas: 6.36
# Aprovados:         5
# Recuperação:       2
#
# --- DADOS FINAIS PARA O DASHBOARD ---
# [
#   {'nota': 7.5, 'status': 'aprovado'},
#   {'nota': 8.0, 'status': 'aprovado'},
#   {'nota': 6.5, 'status': 'aprovado'},
#   {'nota': 4.0, 'status': 'recuperacao'},
#   {'nota': 9.0, 'status': 'aprovado'},
#   {'nota': 0.0, 'status': 'recuperacao'},
#   {'nota': 10.0, 'status': 'aprovado'}
# ]
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()

notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]


def tratar_notas_brutas(nota):
    """Valida uma nota bruta e devolve float se estiver ok, senao None.

    Parametros:
        nota: valor bruto vindo do staging (int, float, str, None, bool...).

    Retorno:
        float da nota valida no intervalo [0, 10], ou None se invalida.
    """
    match nota:
        case bool():
            return None
        case int() | float() if 0 <= nota <= 10:
            return float(nota)
        case str():
            return None
        case _:
            return None


# Etapa 1 + 2: filtra validas e arredonda para 1 casa decimal
notas_validas = [
    round(tratar_notas_brutas(nota), 1)
    for nota in notas_brutas
    if tratar_notas_brutas(nota) is not None
]

# Etapa 3: mapeia nota -> status (aprovado / recuperacao)
status_lote = [
    {"nota": nota, "status": "aprovado" if nota >= 6.0 else "recuperacao"}
    for nota in notas_validas
]

quant_notas_brutas = len(notas_brutas)
quant_notas_validas = len(notas_validas)
soma_notas_validas = sum(notas_validas)
media_notas_validas = (
    soma_notas_validas / quant_notas_validas if quant_notas_validas > 0 else 0.0
)
quant_notas_descartadas = quant_notas_brutas - quant_notas_validas
porcentagem_descartadas = (
    (quant_notas_descartadas * 100) / quant_notas_brutas
    if quant_notas_brutas > 0
    else 0.0
)
quant_aprovados = sum(1 for aluno in status_lote if aluno["status"] == "aprovado")
quant_recuperacao = sum(1 for aluno in status_lote if aluno["status"] == "recuperacao")

print()
print("//magenta/================================================================================/magenta")
print("======================== RELATÓRIO DE AUDITORIA DE LOTE ========================")
print("//magenta/================================================================================/magenta")
print()
print(
    f'//green/{"Total de notas recebidas:":<30}/green //yellow/{quant_notas_brutas:>10}/yellow\n'
    f'//green/{"Total de notas descartadas:":<30}/green //yellow/{quant_notas_descartadas:>10}/yellow\n'
    f'//green/{"% de notas descartadas:":<30}/green //yellow/{porcentagem_descartadas:>9.2f}%/yellow\n'
    f'//green/{"Média das notas válidas:":<30}/green //yellow/{media_notas_validas:>10.2f}/yellow\n'
    f'//green/{"Quantidade - Aprovados:":<30}/green //yellow/{quant_aprovados:>10}/yellow\n'
    f'//green/{"Quantidade - Em Recuperação:":<30}/green //yellow/{quant_recuperacao:>10}/yellow\n'
)

print("//magenta/================================================================================/magenta")
print("======================== DADOS FINAIS PARA O DASHBOARD ========================")
print("//magenta/================================================================================/magenta")
print()
for item in status_lote:
    print(
        f'//green/{"nota:":<8} //yellow/{item["nota"]:<5}/yellow |  '
        f'//green/{"status:":<8} //yellow/{item["status"]}/yellow'
    )
print()
print("//magenta/================================================================================/magenta\n")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# List comprehension filtra e transforma o lote em uma unica passagem
# match/case + guarda (if 0 <= nota <= 10) valida tipo e intervalo juntos
# bool() vem antes de int() porque True/False sao subclasses de int em Python
# None e string ("7") sao descartados — so entra dado numerico limpo
# round(nota, 1) padroniza a escala para o dashboard
# If ternario no dict: "aprovado" se nota >= 6.0, senao "recuperacao"
# Relatorio de auditoria: recebidas, descartadas, % descarte, media, aprovados
# EasyAnsi: linhas === em magenta, textos da tabela em verde, dados em amarelo
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
