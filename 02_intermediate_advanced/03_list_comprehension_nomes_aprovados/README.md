# 03 - List comprehension: nomes aprovados

## Objetivo

Filtrar dados com list comprehension e condicao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Colegio Horizonte |
| **Setor** | Educacao basica |
| **Solicitacao** | Lista rapida de alunos aprovados para mural digital. |

## Enunciado

Dados da turma:
alunos = [
    {"nome": "Ana", "nota": 7.5},
    {"nome": "Bruno", "nota": 4.0},
    {"nome": "Carla", "nota": 8.0},
    {"nome": "Daniel", "nota": 5.5},
]
Gere lista apenas com nomes dos aprovados (nota >= 6) usando list comprehension.
Exiba total de aprovados e a lista de nomes.

## Passo a passo

1. Crie a lista `alunos` com os 4 dicionarios do enunciado (chaves `nome` e `nota`).
2. Defina a constante `NOTA_CORTE = 6.0` no topo, para nao deixar numero magico na regra.
3. Crie `nomes_aprovados` com list comprehension que combina filtro e extracao de campo: `[aluno["nome"] for aluno in alunos if aluno["nota"] >= NOTA_CORTE]`.
4. Calcule o total de aprovados com `len(nomes_aprovados)`.
5. Exiba o total de aprovados e a lista de nomes com rotulos claros.

## Como executar

```bash
cd "03_list_comprehension_nomes_aprovados"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Dados da turma (enunciado)
alunos = [
    {"nome": "Ana", "nota": 7.5},
    {"nome": "Bruno", "nota": 4.0},
    {"nome": "Carla", "nota": 8.0},
    {"nome": "Daniel", "nota": 5.5},
]

# Constante deixa a regra de aprovacao explicita e facil de ajustar
NOTA_CORTE = 6.0

# Comprehension com filtro (if depois do for) + extracao de campo na expressao:
# so entram alunos com nota >= corte, e de cada um pegamos apenas o nome
nomes_aprovados = [aluno["nome"] for aluno in alunos if aluno["nota"] >= NOTA_CORTE]

# Relatorio pedido: total e lista de nomes
print("Total de aprovados:", len(nomes_aprovados))
print("Aprovados:", nomes_aprovados)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Extrai a lista de aprovados da turma para o mural digital."""

# Regra de negocio centralizada em constante de modulo
NOTA_CORTE = 6.0


def listar_aprovados(alunos: list[dict], nota_corte: float = NOTA_CORTE) -> list[str]:
    """Devolve os nomes dos alunos com nota maior ou igual ao corte.

    A funcao recebe o corte como parametro: facilita reuso e testes
    com regras diferentes sem alterar o codigo.
    """
    return [aluno["nome"] for aluno in alunos if aluno["nota"] >= nota_corte]


def main() -> None:
    # Dados de entrada do enunciado
    alunos = [
        {"nome": "Ana", "nota": 7.5},
        {"nome": "Bruno", "nota": 4.0},
        {"nome": "Carla", "nota": 8.0},
        {"nome": "Daniel", "nota": 5.5},
    ]

    # Filtra os aprovados usando a funcao dedicada
    nomes_aprovados = listar_aprovados(alunos)

    # Relatorio para o mural: total e nomes separados por virgula
    print(f"Total de aprovados: {len(nomes_aprovados)}")
    print(f"Aprovados: {', '.join(nomes_aprovados)}")


if __name__ == "__main__":
    main()
```

</details>
