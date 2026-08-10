# 01 - Introducao a list comprehension

## Objetivo

Conhecer list comprehension e o mapa dos 5 exercicios do topico.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / plataforma escolar |
| **Solicitacao** | Automatizar a lista de presenca da reuniao pedagogica. |

## Visao do bloco (exercicios 01 a 05)

Este topico treina **list comprehension**: sintaxe compacta para criar listas a partir de iteraveis, com ou sem filtro condicional.

| # | Nivel | Foco |
|---|-------|------|
| 01 | Leve | Introducao + presenca formatada (passo a passo) |
| 02 | Leve | Transformar valores (dobrar precos) |
| 03 | Ponte | Filtrar e extrair nomes aprovados |
| 04 | Entrevista | Ranking de engajamento + taxa + top N |
| 05 | Entrevista | Pipeline de limpeza de notas + auditoria |

## Enunciado

A empresa enviou a lista de status brutos da chamada:
status_brutos = ["P", "F", "P", "P", "F", "P"]
Onde P = presente e F = falta.
Gere uma nova lista legivel usando list comprehension:
- "Presente" para P
- "Falta" para F
Exiba a lista original e a lista formatada.

## Passo a passo

1. Crie a lista `status_brutos = ["P", "F", "P", "P", "F", "P"]` exatamente como veio da empresa.
2. Crie a lista `status_formatados` com uma list comprehension no formato `[expressao for s in status_brutos]`.
3. Na expressao, use o operador ternario para transformar cada item: `"Presente" if s == "P" else "Falta"`.
4. Nao use loop com `append` — o objetivo aqui e praticar a sintaxe de comprehension.
5. Exiba com `print` a lista original (`status_brutos`) com um rotulo claro.
6. Exiba a lista formatada (`status_formatados`) com outro rotulo claro.

## Como executar

```bash
cd "01_introducao_list_comprehension"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Lista bruta enviada pela empresa: P = presente, F = falta
status_brutos = ["P", "F", "P", "P", "F", "P"]

# List comprehension com ternario na expressao:
# para cada s da lista, gera "Presente" quando s == "P" e "Falta" nos demais casos
status_formatados = ["Presente" if s == "P" else "Falta" for s in status_brutos]

# Exibe as duas listas com rotulos claros para comparacao lado a lado
print("Status brutos:    ", status_brutos)
print("Status formatados:", status_formatados)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Formata a lista de presenca da chamada para leitura humana."""

# Mapa de traducao: centraliza a regra de negocio em um unico lugar.
# Se amanha surgir "J" (justificada), basta adicionar uma entrada aqui.
ROTULOS = {"P": "Presente", "F": "Falta"}


def formatar_presenca(status_brutos: list[str]) -> list[str]:
    """Converte codigos brutos (P/F) em rotulos legiveis.

    dict.get com valor padrao protege contra codigos desconhecidos
    sem quebrar o processamento do lote.
    """
    return [ROTULOS.get(status, "Desconhecido") for status in status_brutos]


def main() -> None:
    # Dados de entrada do enunciado
    status_brutos = ["P", "F", "P", "P", "F", "P"]

    # Aplica a formatacao usando a funcao dedicada
    status_formatados = formatar_presenca(status_brutos)

    # Relatorio simples: original e formatada, alinhadas por rotulo
    print(f"Status brutos:     {status_brutos}")
    print(f"Status formatados: {status_formatados}")


# Garante que o script so roda quando executado diretamente,
# permitindo importar formatar_presenca em testes sem efeitos colaterais
if __name__ == "__main__":
    main()
```

</details>
