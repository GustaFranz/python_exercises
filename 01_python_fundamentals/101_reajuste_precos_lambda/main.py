# EXERCICIO 101 - Reajuste de precos com lambda (contexto de comercio)
#
# ENUNCIADO
# Considere a lista de precos de uma loja:
# precos = [10.0, 25.5, 8.0, 100.0, 4.9]
# Gere uma nova lista aplicando um reajuste de 10% em cada preco.
# Exiba a lista original e a lista reajustada.
#
# ORIENTACOES
## Use map() com uma lambda que multiplica cada preco por 1.10.
## Converta o resultado de map() para list().
## Nao altere a lista original.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

precos = [10.0, 25.5, 8.0, 100.0, 4.9]
precos_com_reajuste = list(map(lambda x: round(x * 1.1, 1), precos))

print(f'//green/Os preços originais são/green //yellow/{precos}/yellow')
print(f'//green/Os preços com reajuste são/green //yellow/{precos_com_reajuste}/yellow')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro contato com map() para transformar lista
# Lambda aplica reajuste de 10% em cada preco
# list(map(...)) gera nova lista sem alterar original
# round() dentro da lambda deixa valor legivel
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
