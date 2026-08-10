# 06 - Introducao a dict comprehension

## Objetivo

Conhecer dict comprehension e o mapa dos exercicios 06 a 10.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Instituto Planalto Cursos |
| **Setor** | Cursos tecnicos |
| **Solicitacao** | Mapear carga horaria semanal por disciplina. |

## Visao do bloco (exercicios 06 a 10)

Topico **dict comprehension**: criar dicionarios a partir de iteraveis de forma compacta.

| # | Nivel | Foco |
|---|-------|------|
| 06 | Leve | Introducao + carga horaria (passo a passo) |
| 07 | Leve | Desconto em precos |
| 08 | Ponte | Contagem de status |
| 09 | Entrevista | Indice de medias + elegibilidade a bonus |
| 10 | Entrevista | Plano de acao / backlog por turma |

## Enunciado

disciplinas = ["Python", "Logica", "Banco de Dados", "Git"]
cargas = [4, 3, 4, 2]
Monte o dicionario disciplina_carga com dict comprehension pareando as duas listas.
Exiba o dicionario formatado (uma disciplina por linha).

## Passo a passo

1. Crie as listas `disciplinas = ["Python", "Logica", "Banco de Dados", "Git"]` e `cargas = [4, 3, 4, 2]`.
2. Crie `disciplina_carga` com dict comprehension usando `zip` para parear as listas: `{disciplina: carga for disciplina, carga in zip(disciplinas, cargas)}`.
3. Pratique a forma com comprehension (existe o atalho `dict(zip(...))`, mas o objetivo aqui e a sintaxe `{chave: valor for ...}`).
4. Percorra `disciplina_carga.items()` com um `for` e exiba uma linha por disciplina no formato `disciplina: X horas/semana`.

## Como executar

```bash
cd "06_introducao_dict_comprehension"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Listas paralelas enviadas pela secretaria do instituto (enunciado)
disciplinas = ["Python", "Logica", "Banco de Dados", "Git"]
cargas = [4, 3, 4, 2]

# Dict comprehension + zip: pareia cada disciplina com a carga da mesma posicao
# e monta o mapa disciplina -> horas semanais em uma linha
disciplina_carga = {disciplina: carga for disciplina, carga in zip(disciplinas, cargas)}

# Exibe uma disciplina por linha, como pede o enunciado
print("Carga horaria semanal por disciplina:")
for disciplina, carga in disciplina_carga.items():
    print(f"  {disciplina}: {carga} horas/semana")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Mapa de carga horaria semanal por disciplina."""


def montar_grade(disciplinas: list[str], cargas: list[int]) -> dict[str, int]:
    """Pareia disciplinas e cargas em um dicionario.

    zip(..., strict=True) falha cedo se as listas tiverem tamanhos
    diferentes — em dados corporativos, e melhor quebrar do que
    truncar silenciosamente pela lista menor.
    """
    return {disc: carga for disc, carga in zip(disciplinas, cargas, strict=True)}


def main() -> None:
    # Dados de entrada do enunciado
    disciplinas = ["Python", "Logica", "Banco de Dados", "Git"]
    cargas = [4, 3, 4, 2]

    # Monta o indice disciplina -> carga
    disciplina_carga = montar_grade(disciplinas, cargas)

    # Relatorio alinhado: nome a esquerda, carga a direita
    print("Carga horaria semanal por disciplina:")
    for disciplina, carga in disciplina_carga.items():
        print(f"  {disciplina:<15} {carga} horas/semana")

    # Total geral agrega valor ao relatorio sem custo extra
    print(f"\nTotal semanal: {sum(disciplina_carga.values())} horas")


if __name__ == "__main__":
    main()
```

</details>
