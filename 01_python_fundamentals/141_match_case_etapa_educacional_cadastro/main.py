# EXERCICIO 141 - Etapa educacional no cadastro de alunos (contexto educacional)
#
# ENUNCIADO
# Crie um cadastro que valida a etapa educacional do aluno por codigo numerico.
# Codigos aceitos: 1 (Anos Iniciais), 2 (Anos Finais), 3 (Ensino Medio).
# O sistema deve:
## solicitar o codigo da etapa;
## exibir a descricao da etapa cadastrada;
## recusar codigos invalidos e permitir nova entrada.
#
# ORIENTACOES
## Use match/case dentro da funcao de validacao.
## Trate erros com try/except fora da funcao (SRP).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
class EtapaInvalidaError(Exception):
    """Lançada quando a etapa lançada não é uma das opões válidas: 1 (Anos Iniciais), 2 (Anos Finais), 3 (Ensino Medio)."""

def validar_etapa(etapa_bruta):
    etapa = etapa_bruta.strip().upper()
    match etapa:
        case "1":
            return "Anos Iniciais"
        case "2":
            return "Anos Finais"
        case "3":
            return "Ensino Medio"
        case _:
            raise EtapaInvalidaError("Digite dessas opções: 1 (Anos Iniciais), 2 (Anos Finais), 3 (Ensino Medio).")

while True:
    entrada = input("Digite a etapa educacional do aluno: ")
    etapa_maiuscula = entrada.upper()
    try:
        etapa = validar_etapa(entrada)
        print(f"Etapa cadastrada com sucesso. {etapa_maiuscula} - {etapa}")
        break

    except EtapaInvalidaError as e:
        print(f'Etapa inválida. {e}')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Exercicio so com enunciado ajudou a fixar o padrao sem olhar sugestao de codigo
# match/case valida etapas 1, 2 e 3 do cadastro educacional
# EtapaInvalidaError deixa a mensagem de erro especifica para o usuario
# SRP: regra na funcao; interface e tratamento de erro no loop principal
# Animado em cadastrar etapa educacional com validacao segura
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
