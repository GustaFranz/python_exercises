# 72 - Closure: fabrica de relatorio por turma

## Objetivo

Criar geradores de relatorio via closure que capturam turma e professor e calculam estatisticas da lista de alunos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Padronizar relatorios de turma com cabecalho fixo e metricas (quantidade e media) para entrega ao coordenador. |

## Enunciado

- Implemente `criar_gerador_relatorio(turma, professor)`:
  - retorna funcao `gerar(lista_alunos)` (closure).
  - `lista_alunos` e lista de dicts `{nome, nota}`.
  - `gerar` retorna string formatada (nao precisa imprimir dentro da closure) com:
    - cabecalho: turma e professor capturados
    - quantidade de alunos
    - media das notas (1 casa decimal; 0 alunos -> media 0.0)
- Crie pelo menos 2 geradores (turmas diferentes) e teste com listas distintas.
- Exiba os relatorios retornados.

Exemplo de entrada:

```python
alunos_7a = [{"nome": "Ana", "nota": 7.5}, {"nome": "Pedro", "nota": 6.0}]
```

## Passo a passo

1. Defina a funcao externa `criar_gerador_relatorio(turma, professor)`.
2. Dentro dela, defina a funcao interna `gerar(lista_alunos)` — `turma` e `professor` serao usados via closure, sem novos parametros.
3. Dentro de `gerar`:
   - calcule `qtd = len(lista_alunos)`;
   - some as notas com `sum(aluno["nota"] for aluno in lista_alunos)`;
   - calcule `media = soma / qtd if qtd > 0 else 0.0` (protege contra lista vazia);
   - monte e RETORNE uma string multilinha (f-string com `\n`) contendo: cabecalho com turma e professor, quantidade de alunos e media com 1 casa decimal (`round(media, 1)` ou `:.1f`).
4. A funcao externa retorna `gerar` sem parenteses.
5. No corpo principal, crie dois geradores: `rel_7a = criar_gerador_relatorio("7A", "Prof. Ana")` e `rel_8b = criar_gerador_relatorio("8B", "Prof. Bruno")`.
6. Chame `rel_7a` com `[{"nome": "Ana", "nota": 7.5}, {"nome": "Pedro", "nota": 6.0}]` e `rel_8b` com `[{"nome": "Carla", "nota": 9.0}]`.
7. Exiba com `print` as duas strings retornadas — cada closure deve mostrar sua propria turma e professor no cabecalho.

## Como executar

```bash
cd "72_closure_relatorio_turma"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def criar_gerador_relatorio(turma, professor):
    # Funcao interna: turma e professor vem do escopo externo (closure)
    def gerar(lista_alunos):
        # Quantidade de alunos da lista recebida
        qtd = len(lista_alunos)

        # Soma as notas com generator expression (nao cria lista intermediaria)
        soma = sum(aluno["nota"] for aluno in lista_alunos)

        # Protege contra divisao por zero quando a turma esta vazia
        media = soma / qtd if qtd > 0 else 0.0

        # Retorna a string pronta — quem imprime e o main
        return (
            f"=== Relatorio da turma {turma} — {professor} ===\n"
            f"Alunos: {qtd}\n"
            f"Media: {round(media, 1)}"
        )

    return gerar


# Dois geradores diferentes: cada closure guarda seu proprio contexto
rel_7a = criar_gerador_relatorio("7A", "Prof. Ana")
rel_8b = criar_gerador_relatorio("8B", "Prof. Bruno")

# Listas de alunos distintas para cada turma
alunos_7a = [{"nome": "Ana", "nota": 7.5}, {"nome": "Pedro", "nota": 6.0}]
alunos_8b = [{"nome": "Carla", "nota": 9.0}]

# Cada gerador produz o relatorio com o cabecalho da sua turma
print(rel_7a(alunos_7a))
print()
print(rel_8b(alunos_8b))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Fabrica de relatorios de turma com contexto capturado por closure.

O closure funciona como uma "mini configuracao": cada gerador nasce
com turma e professor fixos, e recebe apenas os dados variaveis.
Para media, usamos statistics.mean, o modulo padrao para estatisticas.
"""

from collections.abc import Callable
from statistics import mean

# Um aluno e um dict com nome (str) e nota (float)
Aluno = dict[str, object]
GeradorRelatorio = Callable[[list[Aluno]], str]


def criar_gerador_relatorio(turma: str, professor: str) -> GeradorRelatorio:
    """Retorna funcao que gera relatorio textual para a turma configurada."""

    def gerar(lista_alunos: list[Aluno]) -> str:
        qtd = len(lista_alunos)

        # mean() lanca erro com lista vazia, entao tratamos o caso zero antes
        notas = [aluno["nota"] for aluno in lista_alunos]
        media = mean(notas) if notas else 0.0

        # String multilinha montada de uma vez; formatacao :.1f
        # garante sempre 1 casa decimal (ex.: 9.0, nao 9)
        return (
            f"=== Relatorio da turma {turma} — {professor} ===\n"
            f"Alunos: {qtd}\n"
            f"Media: {media:.1f}"
        )

    return gerar


def main() -> None:
    # Cada fabrica gera um closure independente com seu proprio contexto
    rel_7a = criar_gerador_relatorio("7A", "Prof. Ana")
    rel_8b = criar_gerador_relatorio("8B", "Prof. Bruno")

    alunos_7a = [{"nome": "Ana", "nota": 7.5}, {"nome": "Pedro", "nota": 6.0}]
    alunos_8b = [{"nome": "Carla", "nota": 9.0}]

    # A closure calcula e retorna; a exibicao e responsabilidade do main
    print(rel_7a(alunos_7a), rel_8b(alunos_8b), sep="\n\n")


if __name__ == "__main__":
    main()
```

</details>
