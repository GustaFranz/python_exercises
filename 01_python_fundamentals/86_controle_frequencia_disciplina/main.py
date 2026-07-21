# EXERCICIO 86 - Controle de frequencia por disciplina (contexto educacional)
#
# ENUNCIADO
# Considere o seguinte dicionario de disciplinas com frequencia dos alunos:
# frequencia = {"matematica": 85, "portugues": 70, "historia": 90, "ciencias": 60, "geografia": 75}
# O programa deve:
## separar disciplinas com frequencia >= 75 (aprovadas) e < 75 (em alerta);
## criar dois dicionarios;
## calcular a media geral de frequencia.
#
# ORIENTACOES
## Percorra o dicionario.
## Crie novos dicionarios por condicao.
## Utilize sum() / len() para media.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

aprovados = {}
em_alerta = {}

frequencia = {"matematica": 85, "portugues": 70, "historia": 90, "ciencias": 60, "geografia": 75}
media_frequencia = sum(frequencia.values()) / len(frequencia)
    
for disciplina, frequencia_alunos in frequencia.items():
    if frequencia_alunos < 75:
        em_alerta[disciplina] = frequencia_alunos
    else:
        aprovados[disciplina] = frequencia_alunos

print(f'//green/Disciplinas em alerta: //yellow/{em_alerta}')
print(f'//green/Disciplinas aprovadas: //yellow/{aprovados}')
print(f'//green/A média de frequência é: //yellow/{media_frequencia}')
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Dict de disciplinas classificado por percentual
# Media geral com sum(values) / len(dict)
# Alerta automatico para frequencia abaixo de 75%
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
