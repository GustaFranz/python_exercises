# EXERCICIO 143 - Confirmador de venda na cantina com match/case (contexto comercial)
#
# PASSO A PASSO
## Passo 1: Crie VendaInvalidaError para tipos de item nao permitidos.
## Passo 2: Crie confirmar_item(codigo) com match/case dentro da funcao.
##         Aceite: S (salgado), B (bebida), D (doce), L (lanche).
##         Padronize a entrada com strip().upper().
## Passo 3: No case _, lance VendaInvalidaError com mensagem clara.
## Passo 4: Fora da funcao, use while True com try/except para nova entrada.
## Passo 5: Exiba a confirmacao da venda quando o codigo for valido.
#
# ENUNCIADO
# Crie um confirmador de vendas para a cantina escolar.
# O sistema deve:
## solicitar o codigo do item (S, B, D ou L);
## exibir a confirmacao do tipo de produto vendido;
## impedir codigos invalidos sem quebrar o programa.
#
# ORIENTACOES
## match/case na funcao; try/except no fluxo principal (SRP).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

class VendaInvalidaError(Exception):
    """Lançada quando o codigo do item nao e S, B, D ou L."""


def confirmar_item(codigo_bruto):
    codigo = codigo_bruto.strip().upper()
    match codigo:
        case "S":
            return "Salgado"
        case "B":
            return "Bebida"
        case "D":
            return "Doce"
        case "L":
            return "Lanche"
        case _:
            raise VendaInvalidaError(
                "Digite uma dessas opcoes: S (Salgado), B (Bebida), D (Doce), L (Lanche)."
            )


while True:
    entrada = input(
        "| S (Salgado)\n"
        "| B (Bebida)\n"
        "| D (Doce)\n"
        "| L (Lanche)\n"
        "| Digite o codigo do item: "
    )
    entrada_maiuscula = entrada.upper()
    try:
        item = confirmar_item(entrada)
        print(
            f"\n//green/Venda confirmada:/green "
            f"//yellow/{entrada_maiuscula}/yellow — //bold-green/{item}/bold-green\n"
        )
        break
    except VendaInvalidaError as e:
        print(f"\n//bold-red/Codigo invalido./bold-red //red/{e}/red\n")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# match/case dentro da funcao concentra a validacao do item da cantina
# case _ com raise VendaInvalidaError rejeita codigos fora do padrao
# try/except fora da funcao pede nova entrada sem misturar responsabilidades
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
