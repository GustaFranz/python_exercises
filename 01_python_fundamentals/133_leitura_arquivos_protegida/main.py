# EXERCICIO 133 - Leitura de arquivos protegida (contexto de dados)
#
# ENUNCIADO
# Crie um programa que tente abrir e ler um arquivo de texto informado pelo usuario.
# O sistema deve:
## solicitar o nome do arquivo;
## tentar abrir e exibir o conteudo;
## informar erro caso o arquivo nao exista.
#
# ORIENTACOES
## Use try/except.
## Trate FileNotFoundError.
## Permita nova tentativa caso falhe.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import os

caminho_pasta = r"C:\GUSTAVO\PROGRAMAÇAO\carreira"

while True:
    nome_arquivo = input("Digite o nome do arquivo: ")


    if nome_arquivo.lower() == 'sair':
        print("Programa encerrado.")
        break

     caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

    try:
        with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            
        print("\n--- Conteúdo do Arquivo ---")
        print(conteudo)
        print("---------------------------\n")
        break

    except FileNotFoundError:
        print(f"\nErro: O arquivo não foi encontrado em '{caminho_completo}'. Tente novamente.\n")

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Tive certa dificuldade em montar o caminho completo do arquivo sem confundir pasta e nome
# os.path.join() junta pasta e arquivo de forma segura, sem depender de barra manual
# with open() fecha o arquivo automaticamente e evita vazamento de recurso
# encoding='utf-8' ajuda a ler textos com acentos e caracteres especiais
# FileNotFoundError trata quando o arquivo informado nao existe no caminho montado
# try/except impede que o programa encerre com erro inesperado ao abrir arquivos
# while True com break permite tentar de novo ate encontrar um arquivo valido ou digitar sair
# arquivo.read() le o conteudo inteiro de uma vez, util para arquivos pequenos de texto
# Animado em aplicar tratamento de erros na leitura de arquivos sem quebrar o fluxo do programa
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
