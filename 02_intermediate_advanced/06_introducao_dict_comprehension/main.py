# DEMANDA
# Empresa: Instituto Planalto Cursos
# Setor: Cursos tecnicos
# Solicitacao: Mapear carga horaria semanal por disciplina.

# EXERCICIO 06 - Introducao a dict comprehension (contexto corporativo)
#
# VISAO DO BLOCO — Dict comprehension (exercicios 06 a 10)
# Este bloco treina:
## 06 — Introducao: disciplina -> carga horaria
## 07 — Precos com desconto fixo
## 08 — Contagem de status em lista
## 09 — Indice aluno_id -> media
## 10 — Metas por turma com regras condicionais
#
# Conceitos basicos:
## Sintaxe: {chave: valor for item in iteravel}
## Com filtro: {k: v for item in iteravel if condicao}
## Util para transformar listas em dicionarios rapidamente
#
# disciplinas = ["Python", "Logica", "Banco de Dados", "Git"]
# cargas = [4, 3, 4, 2]
# Monte o dicionario disciplina_carga com dict comprehension pareando as duas listas.
# Exiba o dicionario formatado (uma disciplina por linha).
#
# ORIENTACOES
## Use zip dentro da comprehension: {d: c for d, c in zip(disciplinas, cargas)}
## Ou dict(zip(...)) como alternativa, mas pratique a forma com comprehension.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
disciplinas = ["Python", "Logica", "Banco de Dados", "Git"]
cargas = [4, 3, 4, 2]

disciplina_carga = {disciplina: carga for disciplina, carga in zip(disciplinas, cargas)}
print()
print(disciplina_carga)
print()
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Dict comprehension monta um dicionario em uma linha: {chave: valor for ...}
# zip(disciplinas, cargas) pareia cada disciplina com sua carga horaria
# Resultado: mapa disciplina -> horas semanais, pronto para consulta
# Alternativa: dict(zip(...)) — mesma ideia, sem a sintaxe de comprehension
# Util para transformar listas paralelas em indice chave-valor rapidamente
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
