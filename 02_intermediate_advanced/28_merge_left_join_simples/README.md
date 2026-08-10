# 28 - Merge: left join simples

## Objetivo

Simular left join mantendo todos os registros da fonte principal.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataEdu Analytics |
| **Setor** | Dados educacionais |
| **Solicitacao** | Manter todos os alunos da turma mesmo sem nota lancada. |

## Enunciado

turma = [
    {"matricula": "A01", "nome": "Ana"},
    {"matricula": "A02", "nome": "Bruno"},
    {"matricula": "A03", "nome": "Carla"},
]
notas = {"A01": 7.5, "A03": 8.0}
Faca left join: todos da turma + nota (ou "sem nota").
Exiba tabela matricula | nome | nota.

## Passo a passo

1. Declare a lista `turma` (lista de dicts com `"matricula"` e `"nome"`) e o dicionario `notas` do enunciado.
2. Crie a lista vazia `resultado` para armazenar os registros do join.
3. Percorra `for aluno in turma:` — no left join, a lista da esquerda (turma) e preservada por completo.
4. Dentro do loop, busque a nota com `notas.get(aluno["matricula"], "sem nota")` — o segundo argumento do `.get()` e o valor padrao quando a matricula nao tem nota.
5. Monte o registro unificado copiando os campos: `{"matricula": ..., "nome": ..., "nota": ...}` e faca `append` em `resultado`.
6. Exiba o cabecalho `matricula | nome | nota` e, em loop, cada registro formatado com f-string.

## Como executar

```bash
cd "28_merge_left_join_simples"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Fonte principal (lado esquerdo do join): todos os alunos da turma.
turma = [
    {"matricula": "A01", "nome": "Ana"},
    {"matricula": "A02", "nome": "Bruno"},
    {"matricula": "A03", "nome": "Carla"},
]
# Fonte secundaria: notas lancadas (A02 ainda sem nota).
notas = {"A01": 7.5, "A03": 8.0}

# Left join: preserva todos da turma; ausentes recebem o padrao "sem nota".
resultado = [
    {
        "matricula": aluno["matricula"],
        "nome": aluno["nome"],
        # .get() com valor padrao evita KeyError e ja preenche o ausente.
        "nota": notas.get(aluno["matricula"], "sem nota"),
    }
    for aluno in turma
]

# Exibe a tabela final.
print("matricula | nome | nota")
for registro in resultado:
    print(f"{registro['matricula']} | {registro['nome']} | {registro['nota']}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Left join entre cadastro da turma e notas lancadas."""

# Lado esquerdo do join: cadastro completo da turma.
TURMA = [
    {"matricula": "A01", "nome": "Ana"},
    {"matricula": "A02", "nome": "Bruno"},
    {"matricula": "A03", "nome": "Carla"},
]
# Lado direito: notas por matricula (pode estar incompleto).
NOTAS = {"A01": 7.5, "A03": 8.0}

# Valor exibido quando a matricula nao tem nota lancada.
SEM_NOTA = "sem nota"


def left_join(
    turma: list[dict[str, str]], notas: dict[str, float]
) -> list[dict[str, object]]:
    """Preserva todos os alunos da turma, anexando a nota quando existir."""
    return [
        # O desempacotamento **aluno copia matricula e nome;
        # a chave "nota" e adicionada com o resultado do lookup.
        {**aluno, "nota": notas.get(aluno["matricula"], SEM_NOTA)}
        for aluno in turma
    ]


def main() -> None:
    resultado = left_join(TURMA, NOTAS)

    print("matricula | nome | nota")
    for registro in resultado:
        print(f"{registro['matricula']} | {registro['nome']} | {registro['nota']}")


if __name__ == "__main__":
    main()
```

</details>
