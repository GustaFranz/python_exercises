# 12 - Set: intersecao de turmas

## Objetivo

Encontrar elementos comuns entre conjuntos com intersecao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Colegio Integrado Lider |
| **Setor** | Educacao / atividades extracurriculares |
| **Solicitacao** | Identificar alunos que participam de robotica E de teatro. |

## Enunciado

robotica = {"Ana", "Carlos", "Bruno", "Elena"}
teatro = {"Bruno", "Elena", "Felipe", "Ana"}
Calcule participantes_em_ambas com intersecao (& ou .intersection()).
Exiba as duas turmas, os alunos em ambas e a quantidade.

## Passo a passo

1. Crie os conjuntos `robotica` e `teatro` com os nomes do enunciado (use chaves `{}`, sintaxe literal de set).
2. Calcule `participantes_em_ambas` com o operador de intersecao: `robotica & teatro` (equivalente a `robotica.intersection(teatro)`).
3. Exiba as duas turmas originais, usando `sorted(...)` para mostrar em ordem alfabetica (set nao garante ordem).
4. Exiba os alunos presentes em ambas as turmas (tambem com `sorted`).
5. Exiba a quantidade de alunos na intersecao com `len(participantes_em_ambas)`.

## Como executar

```bash
cd "12_set_intersecao_turmas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Inscritos em cada atividade extracurricular (enunciado)
robotica = {"Ana", "Carlos", "Bruno", "Elena"}
teatro = {"Bruno", "Elena", "Felipe", "Ana"}

# O operador & devolve a intersecao: apenas quem esta nos DOIS conjuntos
participantes_em_ambas = robotica & teatro

# sorted() converte para lista ordenada, deixando a exibicao previsivel
print("Turma de robotica:", sorted(robotica))
print("Turma de teatro:  ", sorted(teatro))
print("Em ambas:         ", sorted(participantes_em_ambas))
print("Quantidade:       ", len(participantes_em_ambas))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Identifica alunos inscritos em robotica E teatro."""


def alunos_em_ambas(turma_a: set[str], turma_b: set[str]) -> list[str]:
    """Intersecao das turmas, ja ordenada para exibicao.

    Set e a estrutura certa aqui: intersecao e O(min(len(a), len(b))),
    contra O(n*m) se fossem listas com in.
    """
    return sorted(turma_a & turma_b)


def main() -> None:
    # Dados de entrada do enunciado
    robotica = {"Ana", "Carlos", "Bruno", "Elena"}
    teatro = {"Bruno", "Elena", "Felipe", "Ana"}

    # Calcula a intersecao ordenada
    em_ambas = alunos_em_ambas(robotica, teatro)

    # Relatorio para a coordenacao de atividades
    print(f"Turma de robotica: {sorted(robotica)}")
    print(f"Turma de teatro:   {sorted(teatro)}")
    print(f"Em ambas:          {em_ambas}")
    print(f"Quantidade:        {len(em_ambas)}")


if __name__ == "__main__":
    main()
```

</details>
