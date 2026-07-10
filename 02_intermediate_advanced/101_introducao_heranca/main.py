# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / cadastro
# Solicitacao: Unificar cadastro de pessoas com tipos especificos aluno e professor.

# EXERCICIO 101 - Introducao a heranca (contexto corporativo)
#
# VISAO DO BLOCO — Heranca simples (exercicios 101 a 105)
# Este bloco treina:
## 101 — Introducao: Pessoa -> Aluno / Professor
## 102 — Sobrescrever metodo da classe pai
## 103 — super() para reutilizar __init__ da pai
## 104 — Hierarquia de descontos por tipo
## 105 — Sistema RH com 3 classes relacionadas
#
# Conceitos basicos:
## class Filho(Pai): herda atributos e metodos
## super().__init__(...) chama construtor da classe pai
## Sobrescrever metodo: definir mesmo nome na filha
## "E um" (Aluno e uma Pessoa) — reutilizacao de codigo
#
# Classe Pessoa: __init__(self, nome, cpf); __str__ com nome e cpf
# Classe Aluno(Pessoa): adiciona turma; __str__ inclui turma
# Classe Professor(Pessoa): adiciona disciplina; __str__ inclui disciplina
# Crie 1 aluno e 1 professor e exiba com print().
#
# ORIENTACOES
## class Aluno(Pessoa): chame super().__init__(nome, cpf) no __init__
## Atributos especificos: self.turma, self.disciplina

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
