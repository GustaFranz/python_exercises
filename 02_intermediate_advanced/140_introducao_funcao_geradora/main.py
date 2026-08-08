# DEMANDA
# Empresa: StreamData Escolar
# Setor: Tecnologia / dados
# Solicitacao: Gerar sequencia de eventos de acesso sem carregar tudo na memoria.

# EXERCICIO 140 - Introducao a funcao geradora (contexto corporativo)
#
# VISAO DO BLOCO — Funcoes geradoras (exercicios 140 a 143)
# Este bloco treina:
## 140 — Introducao: yield e iteracao
## 141 — Gerador de lotes (chunks)
## 142 — Filtrar registros com gerador
## 143 — Pipeline de relatorio com geradores
#
# Conceitos basicos:
## yield pausa a funcao e devolve um valor por vez
## A funcao retorna um objeto generator (iteravel)
## Nao monta lista inteira na memoria de uma vez
## for item in gerador: consome sob demanda
#
# Implemente gerar_eventos(quantidade):
## yield f"evento_{i}" para i de 1 ate quantidade
# 1) loop for nos 5 primeiros eventos
# 2) list(gerar_eventos(3)) para comparar
# 3) exibir quantidades consumidas
#
# ORIENTACOES
## def gerar_eventos(quantidade):
##     for i in range(1, quantidade + 1):
##         yield f"evento_{i}"
## Nao use append + return lista neste exercicio

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
