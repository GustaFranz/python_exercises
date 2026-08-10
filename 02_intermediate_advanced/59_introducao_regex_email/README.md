# 59 - Introducao a regex e e-mail

## Objetivo

Valide e-mails com regex (padrao simples com @ e dominio).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MktEscolar |
| **Setor** | Marketing / comunicacao |
| **Solicitacao** | Validar e-mails de responsaveis antes de enviar campanha. |

## Visao do bloco (exercicios 59 a 63)

Topico **Regex com modulo `re`**: validar, extrair e formatar texto.

| # | Nivel | Foco |
|---|-------|------|
| 59 | Leve | Introducao + validar e-mail simples |
| 60 | Leve | Extrair numeros de texto |
| 61 | Ponte | Mascarar CPF parcial |
| 62 | Entrevista | Parsear linhas + rejeicoes + filtro turma |
| 63 | Entrevista | Limpar e padronizar telefones |

## Enunciado

1) Implemente:
```python
def validar_email(email: str) -> bool:
    # use re.fullmatch com padrao simples
```

Padrao sugerido: `r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"`

2) Teste os 3 e-mails:
   - `"ana@escola.com"` — valido
   - `"ana.escola.com"` — invalido
   - `"bruno@mail"` — invalido

3) Exiba resultado de cada teste: `"Valido"` ou `"Invalido"`.

Exemplo de saida:

```
ana@escola.com: Valido
ana.escola.com: Invalido
bruno@mail: Invalido
```

## Passo a passo

1. Importe `re` no topo do script.
2. Defina a constante `PADRAO_EMAIL = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"` — leia o padrao por partes: `[\w.+-]+` (parte local), `@`, `[\w.-]+` (dominio), `\.` (ponto literal) e `[a-zA-Z]{2,}` (extensao com 2+ letras).
3. Defina `def validar_email(email: str) -> bool:` que retorna `re.fullmatch(PADRAO_EMAIL, email) is not None` — o `fullmatch` exige que o padrao case com a string inteira e devolve `None` quando nao casa.
4. Crie a lista `emails = ["ana@escola.com", "ana.escola.com", "bruno@mail"]`.
5. Percorra a lista com `for email in emails:` e monte o texto com ternario: `"Valido" if validar_email(email) else "Invalido"`.
6. Exiba cada resultado no formato `f"{email}: {resultado}"`.

## Como executar

```bash
cd "59_introducao_regex_email"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import re

# Padrao simples: parte local + @ + dominio + . + extensao com 2+ letras
PADRAO_EMAIL = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"


def validar_email(email):
    # fullmatch exige que o padrao cubra a string INTEIRA;
    # devolve um Match quando casa e None quando nao casa
    return re.fullmatch(PADRAO_EMAIL, email) is not None


# Casos de teste do enunciado: 1 valido e 2 invalidos
emails = ["ana@escola.com", "ana.escola.com", "bruno@mail"]

for email in emails:
    # Ternario converte o bool em texto para exibicao
    resultado = "Valido" if validar_email(email) else "Invalido"
    print(f"{email}: {resultado}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Validacao simples de e-mail com regex compilada."""

import re

# re.compile no nivel do modulo: o padrao e compilado uma unica vez,
# mesmo que validar_email seja chamada milhares de vezes na campanha
PADRAO_EMAIL = re.compile(r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$")


def validar_email(email: str) -> bool:
    """Retorna True se o e-mail casa com o padrao minimo de campanha.

    Regex nao substitui verificacao real de entrega; para producao,
    o ideal e validar formato aqui e confirmar via e-mail de opt-in.
    """
    return PADRAO_EMAIL.fullmatch(email) is not None


def main() -> None:
    emails = ["ana@escola.com", "ana.escola.com", "bruno@mail"]

    for email in emails:
        resultado = "Valido" if validar_email(email) else "Invalido"
        print(f"{email}: {resultado}")


if __name__ == "__main__":
    main()
```

</details>
