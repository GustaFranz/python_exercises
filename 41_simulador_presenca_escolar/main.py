# EXERCICIO 41 - Simulador de presença escolar (contexto educacional)
#
# ENUNCIADO
# Uma turma teve 12 aulas. O sistema deve perguntar para cada aula se o aluno esteve presente (P) ou ausente (F).
# Ao final, o sistema deve exibir:
## total de presenças;
## total de faltas;
## percentual de frequência;
## situação final (aprovado se ≥ 75%).
#
# ORIENTACOES
## Use for de 1 a 12.
## Use contador para presença e falta.
## Calcule percentual no final.
## Utilize condições com if.
#
# **🔁 Exercícios com laço while**
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

from rich import print

cont_presenca = 0
cont_faltas = 0
total_aulas = 12
for a in range(1, 13):
    while True:
        aula = input(f'Você participou da aula {a}? [S]/[N]: ').upper()

        if aula not in ['S', 'N']:
            print('[bold red]Resposta inválida! Responda com [S] ou [N][/bold red]')

        else:
            if aula == "S":
                cont_presenca += 1
            else:
                cont_faltas += 1
            break

percentual_presenca = (cont_presenca * 100) / total_aulas

if percentual_presenca >= 75:
    print('=' * 75)
    print(f'ALUNO APROVADO COM [bold green]{percentual_presenca:.1f}%[/bold green] DE PRESENÇA')
    print('=' * 75)
else:
    print('=' * 75)
    print(f'ALUNO REPROVADO COM [bold red]{percentual_presenca:.1f}%[/bold red] DE PRESENÇA')
    print('=' * 75)
print(f'A quantidade total de presenças é [bold green]{cont_presenca}[/bold green]')
print('~'*75)
print(f'A quantidade total de faltas é [bold red]{cont_faltas}[/bold red]')
print('~'*75)






# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================

# Reforcei o uso de estruturas de repetição (for e while) com validação de entrada.
# Consolidei o uso de condicionais e operadores lógicos (if, not in).
# Apliquei contadores para controle de dados ao longo do programa.
# Trabalhei com cálculo de percentual e formatação de saída com f-strings.
# Utilizei a biblioteca Rich para melhorar a apresentação no terminal.
# Compreendi a importância da configuração do ambiente para exibição correta de recursos visuais.
#
#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
