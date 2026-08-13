# DEMANDA
# Empresa: GestaoPro RH
# Setor: Recursos humanos
# Solicitacao: Cadastrar funcionarios e estagiarios compartilhando dados base de pessoa.

# EXERCICIO 109 - Heranca: usar super() (contexto corporativo)
#
# Classe Funcionario: __init__(self, nome, matricula); __str__ com ambos
# Classe Estagiario(Funcionario):
## super().__init__(nome, matricula)
## self.curso = curso
## __str__ inclui curso
# Crie estagiario e exiba.
#
# ORIENTACOES
## super().__init__(nome, matricula) evita duplicar codigo do pai.
## Estagiario e um Funcionario com campo extra.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class Funcionario:
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f'Funcionário {self.funcionario}  | Matrícula: {self.matricula}'

class Estagiario(Funcionario):
    def __init__(self, nome: str, matricula: str, curso: str):
        super().__init__(nome, matricula)
        self.curso = curso

    def __str__(self):
        return (f'Estagiário: {self.nome}  | '
                f'Matrícula: {self.matricula}  | Curso: {self.curso}')

estagiario1 = Estagiario("Rodrigo", "CC-23", "Ciência da Computação")
estagiario2 = Estagiario("Pedro", "MT-45", "Matemática")

print(f'\n{estagiario1}\n'
      f'{estagiario2}\n')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# super().__init__(...) chama o construtor da classe pai sem duplicar codigo
# Funcionario guarda o comum: nome e matricula
# Estagiario e um Funcionario com campo extra (self.curso)
# Na filha: primeiro super().__init__(nome, matricula), depois self.curso = curso
# Assim nome e matricula ficam prontos antes de acrescentar o atributo especifico
# __str__ na filha pode usar self.nome e self.matricula herdados + o curso proprio
# Evitar copiar o __init__ do pai na filha: muda a base, atualiza um so lugar
# Padrao tipico de heranca: reutilizar o pai e estender so o necessario
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
