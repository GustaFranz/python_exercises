# 61 - Regex: mascarar CPF

## Objetivo

Mascare CPF 123.456.789-00 para ***.***.***-00 com re.sub.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Clinica BemViver |
| **Setor** | Saude / LGPD |
| **Solicitacao** | Exibir CPF mascarado em telas de recepcao. |

## Enunciado

- Mascare CPF 123.456.789-00 para ***.***.***-00 com re.sub.

## Passo a passo

1. Importe o modulo `re` no topo do arquivo.
2. Crie a variavel `cpf = "123.456.789-00"` com o CPF de entrada.
3. Defina a funcao `mascarar_cpf(cpf: str) -> str`.
4. Dentro da funcao, use `re.sub` com um padrao que descreva o CPF formatado: tres blocos de 3 digitos separados por ponto, um hifen e um grupo de captura para os 2 digitos finais (ex.: `r"\d{3}\.\d{3}\.\d{3}-(\d{2})"`).
5. Na string de substituicao, escreva os asteriscos fixos e referencie o grupo capturado com `\1` (ex.: `r"***.***.***-\1"`).
6. Retorne o resultado de `re.sub`.
7. No corpo principal, chame `mascarar_cpf(cpf)` e exiba o CPF mascarado com `print`.

## Como executar

```bash
cd "61_regex_mascarar_cpf"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import re

# CPF de entrada, ja no formato XXX.XXX.XXX-XX
cpf = "123.456.789-00"


def mascarar_cpf(cpf: str) -> str:
    # O padrao descreve o CPF formatado:
    # \d{3}\.      -> 3 digitos seguidos de ponto (o \. escapa o ponto)
    # \d{3}\.      -> mais 3 digitos e ponto
    # \d{3}-       -> mais 3 digitos e o hifen
    # (\d{2})      -> grupo de captura com os 2 digitos finais (queremos mante-los)
    padrao = r"\d{3}\.\d{3}\.\d{3}-(\d{2})"

    # re.sub troca tudo que casou pelo texto novo;
    # \1 na substituicao devolve o conteudo do grupo 1 (os 2 digitos finais)
    return re.sub(padrao, r"***.***.***-\1", cpf)


# Chama a funcao e exibe o resultado mascarado
cpf_mascarado = mascarar_cpf(cpf)
print(cpf_mascarado)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Mascara CPFs formatados para exibicao em telas (LGPD)."""

import re

# re.compile pre-compila o padrao: util quando ele sera usado varias vezes
# (em loops, em varios pontos do sistema) e deixa o nome do padrao explicito
PADRAO_CPF = re.compile(r"\d{3}\.\d{3}\.\d{3}-(\d{2})")


def mascarar_cpf(cpf: str) -> str:
    """Substitui os 3 primeiros blocos do CPF por ***, mantendo os 2 digitos finais.

    Ex.: "123.456.789-00" -> "***.***.***-00"
    """
    # O metodo .sub do padrao compilado funciona igual ao re.sub,
    # mas sem recompilar a regex a cada chamada
    return PADRAO_CPF.sub(r"***.***.***-\1", cpf)


def main() -> None:
    # Dado de entrada do enunciado
    cpf = "123.456.789-00"

    # Exibe apenas a versao mascarada — o CPF completo nao deve ir para a tela
    print(mascarar_cpf(cpf))


# Guard clause padrao de mercado: o codigo so roda quando o arquivo
# e executado diretamente, nao quando e importado como modulo
if __name__ == "__main__":
    main()
```

</details>
