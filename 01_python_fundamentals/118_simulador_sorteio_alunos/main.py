# EXERCICIO 118 - Simulador de sorteio de alunos (contexto educacional)
#
# ENUNCIADO
# Um professor deseja sortear alunos para apresentar trabalhos.
# alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel"]
# O sistema deve:
## sortear 3 alunos diferentes;
## garantir que nao haja repeticao;
## exibir o resultado final do sorteio.
#
# ORIENTACOES
## Utilize random.
## Use choice ou sample.
## Evite repeticao manual.
## Exiba resultado formatado.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import random
import easyansi
easyansi.activate()

alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel"]

def sortear_alunos(alunos, quantidade):
    """Sorteia uma quantidade especifica de alunos sem repeticao"""
    if quantidade > len(alunos):
        raise ValueError("Quantidade de alunos a sortear excede o total de alunos disponíveis.")
    return random.sample(alunos, quantidade)

def main():
    quantidade_sorteio = 3
    alunos_sorteados = sortear_alunos(alunos, quantidade_sorteio)

    print(f"//bold-magenta/============= //bold-blue/SORTEIO DE ALUNOS //bold-magenta/=============\n")
    print(f"//green/Alunos sorteados: //yellow/{', '.join(alunos_sorteados)}/yellow\n")
    
if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# random.sample sorteia sem repeticao de uma vez
# Melhor que choice em loop para lista final
# Animado em aplicar sorteio justo na sala de aula
# Estudei random alem do randint do exercicio 117
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
