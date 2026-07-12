# EXERCICIO 110 - Calculadora modular (contexto educacional)
#
# ENUNCIADO
# Crie um programa dividido em modulos para operacoes matematicas basicas.
# O sistema deve permitir somar, subtrair, multiplicar e dividir dois numeros.
# O programa principal deve importar funcoes de um modulo chamado "operacoes.py".
#
# ORIENTACOES
## Crie um arquivo operacoes.py com as funcoes.
## Importe o modulo no main.py.
## Cada operacao deve ser uma funcao separada.
## O main.py deve apenas controlar o fluxo.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()
import operacoes

print(f'//green/A soma de 5 e 3 é:/green //yellow/{operacoes.somar(5, 3)}/yellow')

print(f'//green/A subtracao de 10 e 4 é:/green //yellow/{operacoes.subtrair(10, 4)}/yellow')

print(f'//green/A multiplicacao de 6 e 7 é:/green //yellow/{operacoes.multiplicar(6, 7)}/yellow')

print(f'//green/A divisao de 20 e 5 é:/green //yellow/{operacoes.dividir(20, 5)}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro projeto com modulo separado operacoes.py
# import operacoes chama funcoes de outro arquivo
# main.py so orquestra; calculo fica no modulo
# Animado em dividir a calculadora em partes reutilizaveis
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
