# # Exercício 42 — Sistema de Frequência com Validação e Relatório
#
# ENUNCIADO

# Crie um programa que simule um sistema de controle de frequência escolar.
# Uma turma teve 12 aulas. Para cada aula, o sistema deve perguntar se o aluno esteve presente ou faltou.
# O usuário deve responder:
# - `P` para presente
# - `F` para falta
# O sistema deve validar a resposta, não aceitando valores diferentes de `P` ou `F`.
#
# ## 🔹 Etapa 1 — Coleta de dados
# - Percorra as 12 aulas utilizando `for`
# - Valide cada entrada com `while`
# - Armazene cada resposta em uma lista
#
# ## 🔹 Etapa 2 — Processamento
# Ao final das entradas:
# - Calcule:
#   - total de presenças
#   - total de faltas
#   - percentual de frequência
# - Identifique:
#   - maior sequência consecutiva de presenças
#   - maior sequência consecutiva de faltas
#
# ## 🔹 Etapa 3 — Relatório final
# Exibir:
# - Lista completa das aulas (ex: `['P', 'F', 'P', ...]`)
# - Totais de presença e falta
# - Percentual formatado com 1 casa decimal
# - Situação:
#   - aprovado se ≥ 75%
#   - reprovado se < 75%
# - Maior sequência de presenças
# - Maior sequência de faltas
#
# ## 🔹 Etapa 4 — Repetição do sistema
# Após o relatório:
# Perguntar:
# Deseja analisar outro aluno? [S/N]
#
# - Se `S` → reinicia o sistema
# - Se `N` → encerra
#
# ## Regras
# - Use `for` para percorrer as aulas
# - Use `while` para validação
# - Use lista para armazenar dados
# - Utilize contadores
# - Utilize lógica para identificar sequências consecutivas
# - Utilize `f-string` para formatação (`:.1f`)
# - Opcional: usar a biblioteca Rich para estilização
#
# ## Conceitos treinados
#
# - Laço `for`
# - Laço `while`
# - Validação de entrada
# - Listas
# - Contadores
# - Condicionais
# - Cálculo de percentual
# - Lógica de sequência (nível intermediário)
# - Repetição de sistema

# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

import easyansi
easyansi.activate()


while True:
    lista = []
    quant_presenca = 0
    quant_falta = 0
    total_aulas = 12


    print("="*90)
    print('//bold-magenta/SISTEMA DE CONTROLE DE FREQUÊNCIA ESCOLAR/bold-magenta')
    print("="*90)

    for p in range (1, 13):
        while True:
            presenca = input(f'Registre sua presença //bold-blue/[P]/bold-blue ou ausência //bold-blue/[F]/bold-blue na aula {p}? ').upper()
            if presenca not in ['P', "F"]:
                print('//red/Resposta inválida./redd Confirme com //bold-blue/[P]/bold-blue ou //bold-blue/[F]/bold-blue')
            else:
                lista.append(presenca)
                if presenca == "P":
                    quant_presenca += 1

                if presenca == "F":
                    quant_falta += 1
                break

    percentual_frequencia = (quant_presenca * 100) / total_aulas
    percentual_falta = (quant_falta * 100) / total_aulas

    max_p = 0
    max_f = 0

    atual_p = 0
    atual_f = 0

    for item in lista:
        if item == 'P':
            atual_p += 1
            atual_f = 0
        else:
            atual_f += 1
            atual_p = 0

        if atual_p > max_p:
            max_p = atual_p

        if atual_f > max_f:
            max_f = atual_f

    if percentual_frequencia >= 75:
        print("=" * 90)
        print(f'//bold-green/PARABÉNS! ALUNO APROVADO COM {percentual_frequencia:.1f}% DE FREQUÊNCIA/bold-green')
        print("=" * 90)
    else:
        print("=" * 90)
        print(f'//bold-red/ALUNO REPROVADO COM {percentual_frequencia:.1f}% DE FREQUÊNCIA/bold-red')
        print("=" * 90)

    print(f'Lista das presenças e faltas nas aulas: //bold-green/{lista}/bold-green')
    print('~'*90)
    print(f' Quantidade de presença: //bold-green/{quant_presenca}/bold-green' )
    print('~'*90)
    print(f' Quantidade de faltas: //bold-green/{quant_falta}/bold-green' )

    print('~'*90)
    print(f'A maior sequência de presenças do aluno foi //bold-green/{max_p}/bold-green')
    print('~'*90)
    print(f'A maior sequência de faltas do aluno foi //bold-green/{max_f}/bold-green')

    repetir = input('Deseja analisar outro aluno? [S/N] ').upper()

    if repetir == 'N':
        print('Sistema encerrado.')
        break




# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================

# * Aplicação de estruturas de repetição (`for` e `while`) para controle de fluxo e validação de entrada
# * Manipulação de listas para armazenamento e análise de dados
# * Implementação de regras condicionais para cálculo de frequência e status do aluno
# * Lógica de identificação de sequências consecutivas (presenças e faltas)
# * Estruturação de sistema com execução contínua (loop externo)
# * Uso de biblioteca externa para estilização de saída no terminal (**EasyANSI**)

## 🔗 Referências

# * https://github.com/easyansi/easyansi

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
