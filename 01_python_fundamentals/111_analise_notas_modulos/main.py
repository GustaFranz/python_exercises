# EXERCICIO 111 - Analise de notas com modulos (contexto educacional)
#
# ENUNCIADO
# Crie um sistema dividido em modulos para analisar notas de alunos.
# notas = [7.5, 3.2, 8.0, 6.5, 4.0]
# O sistema deve calcular media, maior nota, menor nota e situacao do aluno,
# mas cada parte deve estar em um modulo diferente.
#
# ORIENTACOES
## Modulo media.py.
## Modulo estatisticas.py.
## Modulo situacao.py.
## main.py apenas orquestra o sistema.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()
import media
import maior_nota
import menor_nota
import situacao_aluno   

print(f"\n//magenta/==============/magenta //yellow/ANÁLISE DE NOTAS/yellow //magenta/==============/magenta|\n")
print(f"//green/Notas:/green //blue/[7.5, 3.2, 8.0, 6.5, 4.0]/blue")
print(f"//green/Media:/green //yellow/{media.calcular_media([7.5, 3.2, 8.0, 6.5, 4.0])}/yellow")
print(f"//green/Maior nota:/green //yellow/{maior_nota.obter_maior_nota([7.5, 3.2, 8.0, 6.5, 4.0])}/yellow")
print(f"//green/Menor nota:/green //yellow/{menor_nota.obter_menor_nota([7.5, 3.2, 8.0, 6.5, 4.0])}/yellow")
media_aluno = media.calcular_media([7.5, 3.2, 8.0, 6.5, 4.0])
print(f"//green/Situacao do aluno:/green //yellow/{situacao_aluno.situacao_aluno(media_aluno)}/yellow")



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Varios modulos, cada um com uma tarefa especifica
# main importa media, maior_nota, menor_nota e situacao_aluno
# Reutilizei calcular_media no fluxo de situacao do aluno
# Animado em montar analise com arquivos separados
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
