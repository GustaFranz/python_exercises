# DEMANDA
# Empresa: Secretaria Digital
# Setor: Educacao / secretaria
# Solicitacao: Padronizar relatorios de turma com cabecalho fixo e metricas (quantidade e media) para entrega ao coordenador.

# EXERCICIO 72 - Closure: fabrica de relatorio por turma (contexto corporativo)
#
# def criar_gerador_relatorio(turma, professor):
#     def gerar(lista_alunos):
#         # turma e professor vêm do escopo externo (closure)
#         # lista_alunos: [{"nome": "...", "nota": float}, ...]
#         # calcular qtd = len(lista_alunos)
#         # media = sum(notas)/qtd se qtd > 0 else 0.0
#         # return string multilinha com cabecalho + qtd + media
#     return gerar
#
# Teste:
# rel_7a = criar_gerador_relatorio("7A", "Prof. Ana")
# rel_8b = criar_gerador_relatorio("8B", "Prof. Bruno")
# print(rel_7a([{"nome": "Ana", "nota": 7.5}, {"nome": "Pedro", "nota": 6.0}]))
# print(rel_8b([{"nome": "Carla", "nota": 9.0}]))
#
# ORIENTACOES
## Closure: funcao interna usa turma/professor sem recebe-los de novo.
## Retorne string formatada; print fica no main apos chamar gerar(...).
## round(media, 1) na saida.
## Dois geradores provam que cada closure mantem seu proprio contexto.

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
