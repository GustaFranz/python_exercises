# DEMANDA
# Empresa: DevEscola Labs
# Setor: Educacao / formacao dev
# Solicitacao: Reorganizar script legado de notas antes de integrar ao sistema novo.

# EXERCICIO 111 - Introducao a refatoracao (contexto corporativo)
#
# VISAO DO BLOCO — Refatoracao (exercicios 111 a 115)
# Este bloco treina:
## 111 — Introducao: ler codigo monolitico e listar problemas
## 112 — Extrair funcoes com responsabilidade unica
## 113 — Renomear variaveis para nomes claros
## 114 — Separar I/O, regra de negocio e apresentacao
## 115 — Refatorar script longo em estrutura organizada
#
# Conceitos basicos:
## Refatorar = melhorar codigo sem alterar resultado final
## Funcoes pequenas com um proposito cada
## Nomes claros valem mais que comentarios longos
## Separar entrada, processamento e saida
#
# CODIGO MONOLITICO FORNECIDO (nao executar — estudar e refatorar):
# notas = [7, 8, 5, 9, 6]
# s = 0
# for n in notas:
#     s = s + n
# m = s / len(notas)
# if m >= 7:
#     print("Turma aprovada com media", m)
# else:
#     print("Turma reprovada com media", m)
# for n in notas:
#     if n < 7:
#         print("Recuperacao:", n)
#
# Tarefa NESTE exercicio (planejamento — sem codigo completo ainda):
## 1) Liste 3 problemas do codigo monolitico acima (comentarios)
## 2) Esboce nomes de 3 funcoes que separariam responsabilidades:
### calcular_media(notas)
### turma_aprovada(media, corte=7)
### listar_recuperacao(notas, corte=7)
## 3) Implemente as 3 funcoes e um main() limpo que reproduz o mesmo resultado.
#
# ORIENTACOES
## Primeiro analise o monolito nos comentarios da VISAO DO BLOCO.
## Depois implemente abaixo com funcoes pequenas e nomes claros.
## O resultado final deve ser identico ao script original.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
