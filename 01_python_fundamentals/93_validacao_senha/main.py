# EXERCICIO 93 - Validacao de senha (contexto de seguranca)
#
# ENUNCIADO
# Crie funcoes para validar senhas de usuarios com base em regras de seguranca.
# Regras:
## minimo 8 caracteres;
## deve conter numero;
## deve conter letra maiuscula.
# Senhas para teste: senhas = ["abc123", "Senha123", "python2024", "SEGURA99", "fraca"]
# O programa deve retornar quais senhas sao validas.
#
# ORIENTACOES
## Crie funcao validar_senha(senha).
## Use funcoes auxiliares se necessario.
## Utilize return True/False.
## Percorra a lista usando funcao principal.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import re

import easyansi

easyansi.activate()

# Importando a biblioteca de expressões regulares (Regex).
# Tradução: o 're' vai analisar os padrões no texto pra mim sem eu precisar fazer 10 'ifs'.
senhas = ["abc123", "Senha123", "python2024", "SEGURA99", "fraca"]


def validar_senha(senha):
    """
    Se a senha for integra, retorna True. caso contrario, retorna False.
    """
    # r"..." -> Avisa o Python: "Não mexe nas minhas barras invertidas, deixa elas em paz".
    # ^ e $  -> Começo e fim do texto. (Olha a senha inteira, não só um pedaço)
    # (?=.*[A-Z]) -> Dá umas espiada pra frente e garante: obrigatório pelo menos uma MAIÚSCULA.
    # (?=.*\d)     -> Dá outra espiada e garante: \d de dígito, ou seja, obrigatório ter NÚMERO".
    # .{8,}        -> O ponto é qualquer caractere, e o {8,} diz: "No MÍNIMO 8 de tamanho, menos que isso é inválido".
    padrao = r"^(?=.*[A-Z])(?=.*\d).{8,}$"

    # re.match pega a senha e joga contra o padrão pra verificar
    if re.match(padrao, senha):
        return True  # Passou no teste.
    return False  # Senha fraca.


def main():
    # Minha função principal pra organizar o relatório e não deixar o código bagunçado.
    print("//magenta/===== VALIDADOR DE SENHAS =====/magenta")

    # Loop padrão: vai pegar uma senha por vez dentro da lista (senhas)
    for senha in senhas:
        # Se a função validar_senha disser que é True...
        if validar_senha(senha):
            print(f"//green/Senha:/green //yellow/{senha:<12}/yellow -> //bold-green/VALIDA ✓/bold-green")
        else:
            print(f"//green/Senha:/green //yellow/{senha:<12}/yellow -> //bold-red/INVALIDA ✗/bold-red")


if __name__ == "__main__":
    main()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro contato com regex (re.match) para validar padroes
# Return True/False concentra a regra na funcao validar_senha
# if __name__ == '__main__' protege a execucao do main()
# Animado em validar varias senhas num loop com poucas linhas
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
