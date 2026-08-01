# EXERCICIO 154 - Funcao com **kwargs: perfil do aluno (contexto educacional)
#
# ENUNCIADO
# Crie uma funcao chamada exibir_perfil que recebe **kwargs.
# A funcao deve percorrer os pares chave-valor e exibir cada informacao em uma linha.
# Teste com:
## exibir_perfil(nome="Ana", idade=15, turma="9B")
## exibir_perfil(nome="Carlos", escola="EE Prof. Silva", turno="matutino")
#
# ORIENTACOES
## Use def exibir_perfil(**kwargs):.
## Percorra com for chave, valor in kwargs.items().
## Exiba no formato: Chave: valor (ex.: Nome: Ana).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class NomeInvalidoError(Exception):
    """Lançada quando o nome do aluno contém apenas números."""


class IdadeInvalidaError(Exception):
    """Lançada quando a idade não é um inteiro positivo maior que zero."""


class CidadeInvalidaError(Exception):
    """Lançada quando a cidade contém apenas números."""


class ValorVazioError(Exception):
    """Lançada quando um campo obrigatório do perfil fica em branco."""


def formatar_perfil_aluno(**dados_aluno: str) -> str:
    ordem_padronizada = ["nome", "idade", "cidade"]
    linhas_formatadas = []

    for chave in ordem_padronizada:
        valor = dados_aluno.get(chave)
        valor_texto = str(valor).strip() if valor is not None else ""

        if not valor_texto:
            raise ValorVazioError(
                f"O campo '{chave.title()}' não pode ficar em branco!"
            )

        match chave:
            case "nome":
                if valor_texto.isdigit():
                    raise NomeInvalidoError(
                        "O nome do aluno não pode conter apenas números!"
                    )
            case "idade":
                if not valor_texto.isdigit() or int(valor_texto) <= 0:
                    raise IdadeInvalidaError(
                        "A idade deve ser um número inteiro positivo maior que zero!"
                    )
            case "cidade":
                if valor_texto.isdigit():
                    raise CidadeInvalidaError(
                        "A cidade não pode conter apenas números!"
                    )

        linhas_formatadas.append(f"{chave.title()}: {valor_texto.title()}")

    return "\n".join(linhas_formatadas)


print("=================== CADASTRO DE PERFIS DE ALUNOS ===================")

while True:
    try:
        quantidade_perfis = int(
            input("Quantos perfis de alunos quer cadastrar? ")
        )
        if quantidade_perfis <= 0:
            print("Digite um número maior que zero!\n")
            continue
        break
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido!\n")

lista_perfis_cadastrados = []
campos_obrigatorios = ["nome", "idade", "cidade"]

for indice in range(1, quantidade_perfis + 1):
    while True:
        print(
            f"\n---------------- CADASTRO DO ALUNO {indice} DE {quantidade_perfis} ----------------"
        )
        perfil_temporario = {}

        for campo in campos_obrigatorios:
            perfil_temporario[campo] = input(
                f"Informe {campo.title()}: "
            ).strip()

        try:
            relatorio_formatado = formatar_perfil_aluno(**perfil_temporario)
            lista_perfis_cadastrados.append(relatorio_formatado)
            print("Perfil validado e cadastrado com sucesso!")
            break
        except (
            NomeInvalidoError,
            IdadeInvalidaError,
            CidadeInvalidaError,
            ValorVazioError,
        ) as erro:
            print(f"\nERRO NO CADASTRO: {erro}")
            print("Por favor, preencha as informações deste aluno novamente.")

print("\n===============================================================")
print("                    RELATÓRIO FINAL DE PERFIS                  ")
print("===============================================================")

for indice, perfil_formatado in enumerate(
    lista_perfis_cadastrados, start=1
):
    print(f"\n--- ALUNO {indice} ---")
    print(perfil_formatado)



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# **kwargs recebe argumentos nomeados e chega como dicionario
# **perfil_temporario na chamada desempacota o dict para **kwargs
# .get(chave) busca o valor sem quebrar se a chave nao existir
# Excecoes customizadas (Nome, Idade, Cidade, ValorVazio) deixam o erro claro
# match/case valida cada campo; try/except fora da funcao pede nova entrada
# strip/title padronizam texto; o relatorio final lista todos os perfis
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
