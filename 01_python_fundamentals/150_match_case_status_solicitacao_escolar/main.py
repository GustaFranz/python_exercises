# EXERCICIO 150 - Status de solicitacao escolar com match/case e | (contexto administrativo)
#
# ENUNCIADO
# Crie um classificador de status para solicitacoes da secretaria escolar
# (ex.: segunda via de historico, declaracao de matricula).
# Em sistemas reais, o mesmo status pode chegar com codigo curto ou nome completo.
# Status aceitos (use | para agrupar equivalentes):
## pendente: P, PENDENTE ou AGUARDANDO;
## aprovado: A, APROVADO ou OK;
## recusado: R, RECUSADO ou NEGADO.
# O sistema deve:
## solicitar o status da solicitacao;
## exibir a descricao do status correspondente;
## recusar valores invalidos e permitir nova tentativa.
#
# ORIENTACOES
## Use match/case com | dentro da funcao de validacao.
## Trate erros com try/except fora da funcao (SRP).
## Padronize a entrada com strip().upper() antes do match.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()


class StatusInvalidoError(Exception):
    """Lançada quando o status da solicitacao nao e reconhecido."""


def classificar_status(status_bruto):
    status = status_bruto.strip().upper()
    match status:
        case "P" | "PENDENTE" | "AGUARDANDO":
            return "Pendente — solicitacao em analise"
        case "A" | "APROVADO" | "OK":
            return "Aprovado — solicitacao liberada"
        case "R" | "RECUSADO" | "NEGADO":
            return "Recusado — solicitacao nao autorizada"
        case _:
            raise StatusInvalidoError(
                "Use P/PENDENTE/AGUARDANDO, A/APROVADO/OK ou R/RECUSADO/NEGADO."
            )


while True:
    entrada = input(
        "| P / PENDENTE / AGUARDANDO\n"
        "| A / APROVADO / OK\n"
        "| R / RECUSADO / NEGADO\n"
        "| Digite o status da solicitacao: "
    )
    entrada_maiuscula = entrada.strip().upper()
    try:
        descricao = classificar_status(entrada)
        print(
            f"\n//green/Status registrado:/green "
            f"//yellow/{entrada_maiuscula}/yellow — //bold-green/{descricao}/bold-green\n"
        )
        break
    except StatusInvalidoError as e:
        print(f"\n//bold-red/Status invalido./bold-red //red/{e}/red\n")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Em sistemas reais o mesmo status chega como codigo curto ou nome completo
# case com | une P/PENDENTE/AGUARDANDO no mesmo tratamento
# A/APROVADO/OK e R/RECUSADO/NEGADO seguem a mesma ideia de equivalencia
# case _ rejeita qualquer valor fora da lista oficial da secretaria
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
