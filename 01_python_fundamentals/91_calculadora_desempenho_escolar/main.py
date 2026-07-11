# EXERCICIO 91 - Calculadora de desempenho escolar (contexto educacional)
#
# ENUNCIADO
# Crie um sistema baseado em funcoes que receba uma lista de notas de um aluno e retorne:
## media;
## situacao (aprovado, recuperacao ou reprovado);
## maior e menor nota.
# notas = [7.5, 3.2, 8.0, 6.5, 4.0]
# O programa deve ser modularizado em funcoes separadas para cada calculo.
#
# ORIENTACOES
## Crie funcoes como calcular_media(), situacao_aluno(), maior_nota(), menor_nota().
## Cada funcao deve ter responsabilidade unica.
## Retorne valores e reutilize funcoes dentro de outras.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

notas = [7.5, 3.2, 8.0, 6.5, 4.0]

def obter_media (notas):
    return sum(notas) / len(notas)

def obter_maior_nota (notas):
    return max(notas)

def obter_menor_nota (notas):
    return min(notas)

def verificar_situacao_aluno(notas):
    media_final = obter_media(notas)
    if media_final >= 7:
        return "Situação: APROVADO"
    elif 5 <= media_final < 7:
        return "Situação: RECUPERAÇÃO"
    else:
        return "Situação: REPROVADO"

print(f'Média: {obter_media(notas):.2f}')
print(f'Maior nota: {obter_maior_nota(notas):.2f}')
print(f'Menor_nota: {obter_menor_nota(notas):.2f}')
print(f'Situação: {verificar_situacao_aluno(notas)}')



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Varias funcoes, cada uma com uma tarefa
# Reutilizei obter_media() dentro de verificar_situacao()
# return concentra calculo; print fica no fluxo principal
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
