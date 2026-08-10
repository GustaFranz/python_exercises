# EXERCICIO 155 - Funcao com **kwargs: mensagem personalizada (contexto de comunicacao)
#
# ENUNCIADO
# Crie uma funcao chamada montar_mensagem que recebe:
## titulo (parametro obrigatorio)
## **opcoes (informacoes extras nomeadas)
# A funcao deve exibir:
## o titulo em destaque;
## cada opcao recebida em linhas separadas.
# Teste com:
## montar_mensagem("Aviso da turma", autor="Prof. Gustavo", prazo="sexta-feira")
## montar_mensagem("Lembrete", atividade="entrega do projeto", valor=10, unidade="pontos")
#
# ORIENTACOES
## Parametro fixo vem antes de **kwargs.
## Use kwargs.get() apenas se precisar de valor padrao.
## Capitalize ou adapte os nomes das chaves na exibicao, se quiser melhorar a leitura.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

def montar_mensagem(titulo: str, **opcoes: str) -> str: 
    print()
    print(f'=========================== {titulo.upper()} =========================== \n')
    for chave, valor in opcoes.items():
        print(f"{chave}: {valor}")
    print()

titulo = "Aviso para o 8º ano A"
autor = "Prof. Gustavo Franz"
local_da_aula = "A próxima aula será no laboratório"
horario = "3º horário"
lembrete = "Não esquecer de trazer os materiais para os experimentos"
montar_mensagem(titulo, 
                mensagem1=autor,
                mensagem2=local_da_aula,
                mensagem3=horario,
                mensagem4=lembrete
                )







# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Parametro fixo (titulo) vem antes de **kwargs (opcoes)
# **kwargs recebe argumentos nomeados extras e chega como dicionario
# for chave, valor in opcoes.items() percorre cada opcao recebida
# Cada chamada pode ter quantidade diferente de opcoes (autor, prazo, etc.)
# f-string com .upper() destaca o titulo na saida
# **kwargs torna a funcao flexivel sem criar um parametro para cada campo
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
