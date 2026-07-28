# EXERCICIO 144 - Registro de pagamento na loja escolar (contexto comercial)
#
# ENUNCIADO
# Crie um registro de pagamentos para a loja de materiais escolares.
# Codigos aceitos: E (entrada), P (parcelado), T (troca), G (gratuito/bolsa).
# O sistema deve:
## solicitar o tipo de pagamento;
## exibir a descricao do registro financeiro;
## permitir nova tentativa quando o codigo for invalido.
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
import easyansi
easyansi.activate()


class PagamentoInvalidoError(Exception):
    """Lançada quando o tipo de pagamento nao e E, P, T ou G."""


def registrar_pagamento(codigo_bruto):
    codigo = codigo_bruto.strip().upper()
    match codigo:
        case "E":
            return "Entrada — pagamento inicial"
        case "P":
            return "Parcelado — pagamento em prestacoes"
        case "T":
            return "Troca — registro de devolucao/troca"
        case "G":
            return "Gratuito/bolsa — sem cobranca"
        case _:
            raise PagamentoInvalidoError(
                "Digite uma dessas opcoes: E (Entrada), P (Parcelado), T (Troca), G (Gratuito/bolsa)."
            )


while True:
    entrada = input(
        "| E (Entrada)\n"
        "| P (Parcelado)\n"
        "| T (Troca)\n"
        "| G (Gratuito/bolsa)\n"
        "| Digite o tipo de pagamento: "
    )
    entrada_maiuscula = entrada.upper()
    try:
        registro = registrar_pagamento(entrada)
        print(
            f"\n//green/Pagamento registrado:/green "
            f"//yellow/{entrada_maiuscula}/yellow — //bold-green/{registro}/bold-green\n"
        )
        break
    except PagamentoInvalidoError as e:
        print(f"\n//bold-red/Tipo invalido./bold-red //red/{e}/red\n")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# match/case valida os tipos financeiros da loja escolar
# raise no case _ mantem a regra de negocio na funcao
# try/except no loop principal trata erro e permite nova tentativa
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
