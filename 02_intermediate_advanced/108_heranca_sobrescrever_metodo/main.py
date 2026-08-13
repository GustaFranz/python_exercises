# DEMANDA
# Empresa: Secretaria Digital
# Setor: Educacao / secretaria
# Solicitacao: Personalizar mensagem de boas-vindas por tipo de usuario no portal.

# EXERCICIO 108 - Heranca: sobrescrever metodo (contexto corporativo)
#
# Classe Usuario: __init__(self, nome); apresentar() -> "Ola, {nome}"
# Classe Aluno(Usuario): apresentar() -> "Aluno {nome}, bem-vindo ao portal!"
# Classe Responsavel(Usuario): apresentar() -> "Responsavel {nome}, acompanhe o boletim."
# Teste apresentar() em cada tipo.
#
# ORIENTACOES
## Sobrescrever = redefinir metodo na subclasse com mesmo nome.
## Nao precisa chamar super().apresentar() neste exercicio.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return f"Olá {self.nome}"

class Aluno(Usuario):
    def apresentar(self):
        return f'Olá {self.nome}, bem vindo ao portal!'

class Responsavel(Usuario):
    def apresentar(self):
        return f'Responsável {self.nome}, acompanhe o boletim escolar.'


aluno = Aluno("Guilherme")
responsavel = Responsavel("Patricia")
print(aluno.apresentar())
print()
print(responsavel.apresentar())
print()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Sobrescrever = redefinir na subclasse um metodo com o mesmo nome da pai
# Usuario define apresentar() generico; Aluno e Responsavel personalizam a mensagem
# A versao da filha substitui a da pai naquele tipo (polimorfismo simples)
# aluno.apresentar() chama o metodo de Aluno, nao o de Usuario
# Neste exercicio nao e preciso chamar super().apresentar() — a mensagem e toda nova
# Heranca + override permite mesmo "contrato" (apresentar) com comportamentos diferentes
# Util em portais: mesma acao, texto adequado ao papel do usuario
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
