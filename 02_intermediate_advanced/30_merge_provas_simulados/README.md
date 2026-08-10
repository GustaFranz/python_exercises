# 30 - Merge: provas e simulados

## Objetivo

Mesclar duas avaliacoes por aluno em registro unico.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Avalia Escolar Online |
| **Setor** | Edtech / avaliacoes |
| **Solicitacao** | Consolidar nota de prova e simulado por aluno para boletim bimestral. |

## Enunciado

provas = {"Ana": 7.0, "Bruno": 5.5, "Carla": 8.5}
simulados = {"Ana": 8.0, "Bruno": 6.0, "Daniel": 7.0}
Uniao de todos os nomes (set de chaves).
Para cada aluno: nota_prova, nota_simulado (None se ausente), media das disponiveis.
Exiba boletim consolidado.

## Passo a passo

1. Declare os dicionarios `provas` e `simulados` do enunciado.
2. Monte a uniao dos nomes com operador de conjuntos: `nomes = set(provas) | set(simulados)` — `set(dict)` pega as chaves; `|` une os dois conjuntos sem repetir.
3. Crie a lista vazia `boletim`.
4. Percorra `for nome in sorted(nomes):` — o `sorted` garante ordem alfabetica estavel na exibicao.
5. Dentro do loop, busque `nota_prova = provas.get(nome)` e `nota_simulado = simulados.get(nome)` (ausente vira `None`).
6. Calcule a media apenas das notas disponiveis: monte `disponiveis = [n for n in (nota_prova, nota_simulado) if n is not None]` e faca `media = sum(disponiveis) / len(disponiveis)`.
7. Faca `boletim.append({"nome": ..., "prova": ..., "simulado": ..., "media": ...})`.
8. Exiba o boletim consolidado formatando `None` como `"—"` e a media com `:.1f`.

## Como executar

```bash
cd "30_merge_provas_simulados"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Duas fontes de avaliacao; nem todo aluno esta nas duas.
provas = {"Ana": 7.0, "Bruno": 5.5, "Carla": 8.5}
simulados = {"Ana": 8.0, "Bruno": 6.0, "Daniel": 7.0}


def formatar(nota):
    # Converte None em travessao para a exibicao ficar limpa.
    return "—" if nota is None else nota


# Uniao das chaves: todos os alunos que aparecem em qualquer fonte.
# set(dict) extrai as chaves; | e o operador de uniao de conjuntos.
nomes = set(provas) | set(simulados)

boletim = []
for nome in sorted(nomes):  # sorted garante ordem alfabetica
    # .get() devolve None quando o aluno nao tem aquela avaliacao.
    nota_prova = provas.get(nome)
    nota_simulado = simulados.get(nome)

    # Media considera apenas as notas que existem (nao-None).
    disponiveis = [n for n in (nota_prova, nota_simulado) if n is not None]
    media = sum(disponiveis) / len(disponiveis)

    boletim.append({
        "nome": nome,
        "prova": nota_prova,
        "simulado": nota_simulado,
        "media": media,
    })

# Exibe o boletim consolidado.
print("=== Boletim consolidado ===")
for b in boletim:
    print(
        f"{b['nome']} | prova: {formatar(b['prova'])} | "
        f"simulado: {formatar(b['simulado'])} | media: {b['media']:.1f}"
    )
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Consolida notas de prova e simulado em boletim unico por aluno."""

from dataclasses import dataclass
from statistics import mean

PROVAS = {"Ana": 7.0, "Bruno": 5.5, "Carla": 8.5}
SIMULADOS = {"Ana": 8.0, "Bruno": 6.0, "Daniel": 7.0}


@dataclass
class LinhaBoletim:
    """Registro consolidado de um aluno no boletim."""

    nome: str
    prova: float | None
    simulado: float | None
    media: float

    def formatada(self) -> str:
        """Linha pronta para exibicao, com None renderizado como travessao."""
        prova = "—" if self.prova is None else self.prova
        simulado = "—" if self.simulado is None else self.simulado
        return (
            f"{self.nome} | prova: {prova} | "
            f"simulado: {simulado} | media: {self.media:.1f}"
        )


def consolidar(
    provas: dict[str, float], simulados: dict[str, float]
) -> list[LinhaBoletim]:
    """Une as duas fontes e calcula a media das notas disponiveis."""
    boletim = []
    # Uniao das chaves cobre alunos presentes em qualquer uma das fontes.
    for nome in sorted(set(provas) | set(simulados)):
        prova = provas.get(nome)
        simulado = simulados.get(nome)
        # Filtra as notas existentes; statistics.mean calcula a media.
        disponiveis = [n for n in (prova, simulado) if n is not None]
        boletim.append(
            LinhaBoletim(
                nome=nome,
                prova=prova,
                simulado=simulado,
                media=mean(disponiveis),
            )
        )
    return boletim


def main() -> None:
    print("=== Boletim consolidado ===")
    for linha in consolidar(PROVAS, SIMULADOS):
        print(linha.formatada())


if __name__ == "__main__":
    main()
```

</details>
