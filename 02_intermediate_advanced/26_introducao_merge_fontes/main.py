# DEMANDA
# Empresa: DataEdu Analytics
# Setor: Dados educacionais
# Solicitacao: Unificar lista de nomes com dicionario de notas para boletim.

# EXERCICIO 26 - Introducao a merge de fontes (contexto corporativo)
#
# VISAO DO BLOCO — Merge de duas fontes (exercicios 26 a 30)
# Este bloco treina:
## 26 — Introducao: nomes + dict de notas
## 27 — Left join simples
## 28 — Tratar registros ausentes
## 29 — Mesclar provas + simulados
## 30 — Relatorio unificado com inconsistencias
#
# Conceitos basicos:
## Cruzar dados de estruturas diferentes (lista, dict, lista de dicts)
## Tratar chaves ausentes com .get() ou verificacao
## Relatorio unificado para tomada de decisao
#
# nomes = ["Ana", "Bruno", "Carla", "Daniel"]
# notas_por_nome = {"Ana": 8.0, "Bruno": 6.5, "Carla": 9.0}
# Gere boletim unificado: lista de dicts {"nome": ..., "nota": ...}
# Para nomes sem nota, use nota = None.
# Exiba boletim e quantos ficaram sem nota.
#
# ORIENTACOES
## Loop for nome in nomes: notas_por_nome.get(nome) retorna None se ausente.
## Append dict na lista resultado.
## Conte None com sum(1 for b in boletim if b["nota"] is None).

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
