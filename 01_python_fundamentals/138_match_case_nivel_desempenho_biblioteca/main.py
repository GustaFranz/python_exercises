# EXERCICIO 138 - Nivel de desempenho na biblioteca escolar (contexto educacional)
#
# ENUNCIADO
# Crie um sistema para a biblioteca escolar que classifica o nivel de leitura do aluno.
# O sistema deve:
## solicitar o nivel informado (P, I, A ou S — Principiante, Intermediario, Avancado, Superior);
## exibir a descricao do nivel de desempenho em leitura;
## recusar codigos invalidos e permitir nova tentativa.
#
# ORIENTACOES
## Use match/case dentro de uma funcao de validacao.
## Trate erros com try/except fora da funcao (SRP).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class NivelInvalidoError(Exception):
    """Lançada quando o usuário não digitar nenhuma das opções válidas: (P, I, A ou S — Principiante, Intermediario, Avancado, Superior)"""

def validar_nivel(nivel):
    nivel_leitura = nivel.strip().upper()
    match nivel_leitura:
        case "P":
            return "Principiante"
        case "I":
            return "Intermediário"
        case "A":
            return "Avançado"
        case "S":
            return "Superior"
        case _:
            raise NivelInvalidoError("Digite uma oção válida: P (Principiante), I (Intermediario), A (Avancado) ou S (Superior).")
        

while True:
    entrada = input("Digite o nível de leitura do aluno: ")
    entrada_maiuscula = entrada.upper()

    try:
        nivel_leitura = validar_nivel(entrada)
        print(f'Nível registrado com sucesso. {entrada_maiuscula}: {nivel_leitura}.')
        break
    
    except NivelInvalidoError as e:
        print(f'Erro: {e}')



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Terceiro exercicio do grupo reforcou a mesma logica com outro vocabulario
# match/case valida P, I, A e S para nivel de leitura na biblioteca
# NivelInvalidoError no case _ protege o cadastro contra codigos errados
# SRP: validacao dentro da funcao; tratamento de erro no fluxo principal
# Animado em resolver sozinho so com o enunciado, sem passo a passo guiado
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
