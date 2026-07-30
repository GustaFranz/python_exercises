# DEMANDA
# Empresa: GrowLeads Hub
# Setor: Marketing / operacoes comerciais
# Solicitacao: Importar lote de leads do staging sem derrubar o job; auditar falhas.

# DESAFIO - Importacao robusta de leads
# Conteudos: CSV/JSON, excecao customizada, try/except/finally
#
# 1) class LeadInvalidoError(Exception)
# 2) validar_lead -> raise se email sem @ ou idade fora 18..100
# 3) ler CSV; try/except por linha -> importados / rejeitados
# 4) finally registra em importacao.log
# 5) gravar leads_ok.json + resumo com taxa de sucesso
#
# ORIENTACOES
## Nao use bare except
## finally roda sempre (sucesso ou falha)
## json.dump(importados, f, ensure_ascii=False, indent=2)

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
