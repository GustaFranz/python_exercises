# EXERCICIO 51 - Catalogo de produtos fixos (contexto de comercio)
#
# ENUNCIADO
# Um sistema de loja deseja manter um catalogo de produtos que nao pode ser alterado facilmente.
# Cada produto possui codigo, nome e preco.
# O programa deve armazenar produtos como tuplas, exibir o catalogo completo e permitir apenas consulta.
#
# ORIENTACOES
## Use tuplas no formato (codigo, nome, preco).
## Armazene em lista.
## Percorra com for.
## Nao implemente alteracoes no catalogo.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

#como o catálogo não é dinâmico, supomos que a lista de materiais já está pré-estabelecida:

catalogo = [
    (1, "Caderno 10 matérias", 24.90),
    (2, "Caneta esferográfica azul", 2.50),
    (3, "Lápis grafite HB", 1.50),
    (4, "Borracha branca", 1.00),
    (5, "Apontador com depósito", 3.75),
    (6, "Marca-texto amarelo", 4.90),
    (7, "Régua 30cm", 5.25),
    (8, "Estojo escolar", 19.90)
] 

for (codigo, nome, preco) in catalogo:
    print(f'//green/Código:/green  '
          f'//yellow/{codigo:03}/yellow  | '
          f'//green/Produto:/green '
          f'//yellow/{nome:.<35}/yellow  | '
          f'//green/Preço:/green '
          f'//yellow/R$ {preco}/yellow'
          )

print("//magenta/" + "-" * 105 + "/magenta")
print("GF PAPELARIA             //bold-blue/CONSULTA DE PRODUTOS/bold-blue             GF PAPELARIA")
print("//magenta/" + "-" * 105 + "/magenta")

codigo_busca = int(input("Digite o código do produto: "))

for produto in catalogo:
    if produto[0] == codigo_busca:
        print("//magenta/" + "-" * 105 + "/magenta")
        print(f"//green/Código:/green //yellow/{produto[0]:03}/yellow | "
              f"//green/Produto:/green //yellow/{produto[1]:.<35}/yellow | "
              f"//green/Preço:/green //yellow/R$ {produto[2]:.2f}/yellow "
              )
        print("//magenta/" + "-" * 105 + "/magenta")

        break

else:
    print("Produto não encontrado.")
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
# 
# Aplicação prática do conceito de tuplas como estruturas imutáveis
# Organização de dados em lista de tuplas para simular um catálogo
# Implementação de sistema de consulta sem alteração dos dados
# Uso de estrutura de repetição para busca de informações
# Consolidação da diferença entre exibição e consulta de dados
# Utilização da biblioteca EasyAnsi para melhoria visual do sistema

# Link do repositório da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# 
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
