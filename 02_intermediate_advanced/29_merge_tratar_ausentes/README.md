# 29 - Merge: tratar registros ausentes

## Objetivo

Tratar dados ausentes com valor padrao e flags no merge.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Hospital Escola Vida |
| **Setor** | Saude / prontuario |
| **Solicitacao** | Cruzar pacientes com resultados de exame tratando ausencias. |

## Enunciado

pacientes = ["P001", "P002", "P003", "P004"]
resultados = {"P001": "normal", "P003": "atencao", "P005": "normal"}
Cruze pacientes com resultados.
Ausentes: resultado = "pendente", flag_ausente = True.
Presentes: flag_ausente = False.
Exiba relatorio e total pendentes.

## Passo a passo

1. Declare a lista `pacientes` e o dicionario `resultados` do enunciado (repare que `P005` esta em `resultados` mas nao na lista de pacientes — ele fica de fora, pois a fonte principal e `pacientes`).
2. Crie a lista vazia `relatorio`.
3. Percorra `for paciente in pacientes:`.
4. Dentro do loop, verifique presenca com `if paciente in resultados:` — presente: `resultado = resultados[paciente]` e `flag_ausente = False`; ausente: `resultado = "pendente"` e `flag_ausente = True`.
5. Faca `relatorio.append({"paciente": ..., "resultado": ..., "flag_ausente": ...})`.
6. Conte os pendentes com `sum(1 for r in relatorio if r["flag_ausente"])`.
7. Exiba cada registro do relatorio (paciente, resultado e flag) e o total de pendentes no final.

## Como executar

```bash
cd "29_merge_tratar_ausentes"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Fonte principal: pacientes que devem aparecer no relatorio.
pacientes = ["P001", "P002", "P003", "P004"]
# Fonte secundaria: resultados de exame (P005 nao esta na lista principal).
resultados = {"P001": "normal", "P003": "atencao", "P005": "normal"}

# Monta o relatorio cruzando as duas fontes.
relatorio = []
for paciente in pacientes:
    if paciente in resultados:
        # Presente: usa o resultado real e marca flag como False.
        registro = {
            "paciente": paciente,
            "resultado": resultados[paciente],
            "flag_ausente": False,
        }
    else:
        # Ausente: valor padrao "pendente" + flag True para auditoria.
        registro = {
            "paciente": paciente,
            "resultado": "pendente",
            "flag_ausente": True,
        }
    relatorio.append(registro)

# Total de pendentes: soma 1 para cada flag_ausente True.
total_pendentes = sum(1 for r in relatorio if r["flag_ausente"])

# Exibe o relatorio final.
print("=== Relatorio de exames ===")
for r in relatorio:
    print(f"{r['paciente']} | {r['resultado']} | ausente: {r['flag_ausente']}")

print(f"Total pendentes: {total_pendentes}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Cruza pacientes com resultados de exame, sinalizando ausencias."""

from dataclasses import dataclass

# Fonte principal e fonte secundaria do cruzamento.
PACIENTES = ["P001", "P002", "P003", "P004"]
RESULTADOS = {"P001": "normal", "P003": "atencao", "P005": "normal"}

RESULTADO_PENDENTE = "pendente"


@dataclass
class RegistroExame:
    """Linha do relatorio: paciente, resultado e flag de ausencia."""

    paciente: str
    resultado: str
    flag_ausente: bool


def cruzar(pacientes: list[str], resultados: dict[str, str]) -> list[RegistroExame]:
    """Gera um registro por paciente, tratando resultados ausentes."""
    relatorio = []
    for paciente in pacientes:
        # .get() devolve None quando nao ha resultado para o paciente.
        resultado = resultados.get(paciente)
        relatorio.append(
            RegistroExame(
                paciente=paciente,
                # Se ausente, usa o padrao "pendente".
                resultado=resultado if resultado is not None else RESULTADO_PENDENTE,
                # A flag deriva diretamente da ausencia do lookup.
                flag_ausente=resultado is None,
            )
        )
    return relatorio


def main() -> None:
    relatorio = cruzar(PACIENTES, RESULTADOS)

    # Booleans somam como 1/0, entao sum() conta os pendentes.
    total_pendentes = sum(r.flag_ausente for r in relatorio)

    print("=== Relatorio de exames ===")
    for r in relatorio:
        print(f"{r.paciente} | {r.resultado} | ausente: {r.flag_ausente}")

    print(f"Total pendentes: {total_pendentes}")


if __name__ == "__main__":
    main()
```

</details>
