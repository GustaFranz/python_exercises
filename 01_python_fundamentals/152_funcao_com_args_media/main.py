# EXERCICIO 152 - Funcao com *args: media de notas (contexto educacional)
#
# ENUNCIADO
# Crie uma funcao chamada analisar_notas que recebe *args com as notas de um aluno.
# A funcao deve:
## calcular a media das notas recebidas;
## exibir a media com uma casa decimal;
## informar "Aprovado" se media >= 6, senao "Recuperacao".
# Teste com:
## analisar_notas(7.0, 8.5, 6.0)
## analisar_notas(4.0, 5.5, 3.0, 6.0)
#
# ORIENTACOES
## Trate *args como uma colecao de notas.
## Evite dividir por zero: se nao houver notas, exiba mensagem de aviso.
## Reutilize a media para decidir a situacao do aluno.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

def analyze_grades(*args: float):
    notes = (args)
    number_grades = len(notes)
    sum_grades = sum(notes)
    average_grades = sum_grades / number_grades
    situation = "Recuperação"
    data = average_grades, situation
    if average_grades >=6:
        situation = "Aprovado"
    return data

analyze = analyze_grades(7.0, 8.5, 6.0)
print(f'\n========================= ANALYSE GRADES =========================\n')
print(f'Average: {analyze[0]:.1f}\n'
      f'Situation: {analyze[1]}')
print("\n")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# *args vira tupla de notas; len e sum bastam para a media
# A mesma funcao aceita 3 ou 4 notas sem mudar a assinatura
# Media reutilizada para decidir Aprovado (>= 6) ou Recuperacao
# Vale proteger divisao por zero se args vier vazio
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
