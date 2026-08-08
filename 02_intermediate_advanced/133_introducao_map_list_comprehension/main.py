# DEMANDA
# Empresa: DataClean Escolar
# Setor: Educacao / qualidade de dados
# Solicitacao: Normalizar notas recebidas como texto e listar apenas valores validos.

# EXERCICIO 133 - Introducao a map com list comprehension (contexto corporativo)
#
# VISAO DO BLOCO — map() + comprehensions (exercicios 133 a 136)
# Este bloco treina:
## 133 — Introducao: map + list comprehension
## 134 — map com lambda + filtro em list comprehension
## 135 — map + dict comprehension
## 136 — Relatorio comercial com map e comprehensions
#
# Conceitos basicos:
## map(funcao, iteravel) aplica funcao a cada item (retorna iterador)
## list(map(...)) materializa o resultado em lista
## List comprehension filtra ou transforma apos o map
## Combinacao util quando a transformacao e padronizada (float, str, int)
#
# notas_texto = ["7.5", "8", "abc", "6.0", "-1", "9.5", "5.5"]
# 1) Converta com map(float, ...) tratando erros item a item
# 2) Filtre notas entre 0 e 10 com list comprehension
# 3) Exiba original, validas e qtd aprovada (>= 6)
#
# ORIENTACOES
## def converter_seguro(valor): try return float(valor) except return None
## notas = [n for n in map(converter_seguro, notas_texto) if n is not None]
## validas = [n for n in notas if 0 <= n <= 10]

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
