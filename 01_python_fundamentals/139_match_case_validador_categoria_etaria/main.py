# EXERCICIO 139 - Validador de categoria etaria com match/case (contexto educacional)
#
# OBJETIVO
# Usar match/case para validar categorias etarias em cadastros escolares.
#
# CONCEITO - MATCH/CASE COM CODIGOS NUMERICOS
## Quando os dados sao codigos numericos (1, 2, 3), o match compara o tipo exato.
## Se a entrada vem como texto do input(), converta antes ou compare strings:
##   case "1": ou case 1: (dependendo do tipo apos conversao)
## O operador | permite unir alternativas no mesmo bloco:
##   case "1" | "2": trata infantil e fundamental inicial no mesmo fluxo
## Guardas (if) validam intervalos quando o valor e numerico:
##   case n: if 6 <= n <= 10: valida faixa etaria
## SRP neste exercicio:
## - Funcao validar_categoria(): match/case + raise para codigo invalido
## - Bloco principal: try/except + loop de nova entrada
#
# PASSO A PASSO DETALHADO
## Passo 1: Crie CategoriaInvalidaError(Exception).
## Passo 2: Crie validar_categoria(codigo) com match/case:
##     def validar_categoria(codigo):
##         codigo_limpo = codigo.strip()
##         match codigo_limpo:
##             case "1":
##                 return "Educacao Infantil (4 a 5 anos)"
##             case "2":
##                 return "Ensino Fundamental (6 a 14 anos)"
##             case "3":
##                 return "Ensino Medio (15 a 17 anos)"
##             case _:
##                 raise CategoriaInvalidaError(
##                     "Codigo invalido. Use 1, 2 ou 3."
##                 )
## Explicacao:
## - case "1" compara o texto digitado apos strip()
## - cada case retorna a descricao da categoria etaria valida
## - case _ centraliza o tratamento de codigos fora do padrao
## Passo 3: Fora da funcao:
##     while True:
##         codigo = input("Digite o codigo da categoria (1, 2 ou 3): ")
##         try:
##             categoria = validar_categoria(codigo)
##             print(categoria)
##             break
##         except CategoriaInvalidaError as e:
##             print(f"Erro: {e}")
#
# ENUNCIADO
# Crie um validador de categoria etaria para matricula escolar.
# Codigos aceitos: 1 (Infantil), 2 (Fundamental), 3 (Medio).
# O sistema deve:
## solicitar o codigo da categoria;
## exibir a descricao da etapa correspondente;
## recusar codigos invalidos sem quebrar o programa.
#
# ORIENTACOES
## match/case dentro da funcao; try/except fora da funcao.
## Use case _ para codigos invalidos.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class CategoriaInvalidaError(Exception):
    """Lançada quando o ousuário digita uma categoria não presente em 1 (Infantil), 2 (Fundamental), 3 (Médio)."""

def validar_categoria(categoria_bruta):
    categoria = categoria_bruta.strip()
    match categoria:
        case "1":
            return "Infantil"
        case "2":
            return "Fundamental"
        case "3":
            return "Médio"
        case _:
            raise CategoriaInvalidaError("Digite uma dessas opções: 1 (Infantil), 2 (Fundamental), 3 (Médio).")

while True:
    entrada = input("Digite a categoria do aluno: ")
    try:
        categoria = validar_categoria(entrada)
        print(f'Categoria registrada com sucesso. {entrada}')
        break

    except CategoriaInvalidaError as e:
        print(f'Categoria inválida. {e}')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# match/case funciona bem com codigos numericos tratados como texto
# cases "1", "2" e "3" mapeiam categoria etaria de forma legivel
# CategoriaInvalidaError no case _ centraliza a rejeicao de entradas invalidas
# try/except fora da funcao mantem a separacao de responsabilidades
# Animado em aplicar match/case em cadastros com codigos simples
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
