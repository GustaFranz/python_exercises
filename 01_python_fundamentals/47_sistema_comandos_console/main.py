# EXERCICIO 47 - Sistema de leitura de comandos (modo console) com saída por comando (com break)
#
# ENUNCIADO
# Crie um sistema que simula um menu de comandos simples.
# O usuário pode digitar comandos como:
## "status"
## "ajuda"
## "calcular"
## "sair"
# O sistema deve:
## responder a cada comando;
## continuar rodando indefinidamente;
## encerrar apenas quando o usuário digitar "sair".
#
# ORIENTACOES
## Use while True
## Use if / elif para comandos
## Use break para encerrar
## Estruture como mini sistema de console
#
# **# Exercícios de Python Intermediário – Tuplas**
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

# Observação: fiz um acrescimo no nível da atividade

import easyansi

easyansi.activate()

print("=" * 70)
print("//bold-cyan/SISTEMA DE COMANDOS - MODO CONSOLE/bold-cyan")
print("=" * 70)

while True:

    comando = input("\nDigite um comando: ").lower()

    if comando == "status":

        print("\n" + "=" * 70)
        print("//bold-green/STATUS DO SISTEMA/bold-green")
        print("=" * 70)
        print("✓ Banco de dados: Online")
        print("✓ Servidor: Funcionando")
        print("✓ Conexão: Estável")
        print("✓ Temperatura: 42 ºC")
        print("✓ Uso da CPU: 18%")
        print("✓ Memória RAM: 43%")
        print("=" * 70)

    elif comando == "ajuda":

        print("\n" + "=" * 70)
        print("//bold-yellow/CENTRAL DE AJUDA/bold-yellow")
        print("=" * 70)
        print("Comandos disponíveis:")
        print()
        print("status     → Exibe informações do sistema.")
        print("ajuda      → Mostra este menu.")
        print("calcular   → Abre a calculadora.")
        print("sair       → Encerra o programa.")
        print("=" * 70)

    elif comando == "calcular":

        print("\n" + "=" * 70)
        print("//bold-blue/CALCULADORA/bold-blue")
        print("=" * 70)
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print()
        print("//cyan/Função em desenvolvimento.../cyan")
        print("=" * 70)

    elif comando == "sair":

        print("//bold-red/Encerrando o sistema.../bold-red")
        break

    else:

        print("//bold-red/Comando inválido!/bold-red")
        print("Digite //yellow/ajuda//yellow para visualizar os comandos disponíveis.")


# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================
# 
# Durante o desenvolvimento deste exercício, tive a oportunidade de:
# 
# Relembrar a utilização do while True para criar um sistema de execução contínua.
# Consolidar a comparação de strings para identificar comandos digitados pelo usuário.
# Reforçar a construção de menus utilizando if, elif e else.
# Relembrar o uso do comando break para encerrar o programa de forma controlada.
# Consolidar a organização de um menu interativo em modo console, separando funcionalidades por comandos.
# Reforçar a utilização da biblioteca EasyANSI para tornar a interface do terminal mais organizada e intuitiva.

# 🔗 Link do repositório da biblioteca EasyAnsi:
# https://github.com/GustaFranz/easyansi

# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
