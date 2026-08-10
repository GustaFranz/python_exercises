# 73 - Closure: fabrica de validadores

## Objetivo

Criar fabrica que gera validadores com min e max configuraveis.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Clinica BemViver |
| **Setor** | Saude / triagem |
| **Solicitacao** | Validar sinais vitais com faixas diferentes por tipo de exame. |

## Enunciado

Implemente a fabrica:

```python
def criar_validador(minimo, maximo):
    def validar(valor) -> bool:
        return minimo <= valor <= maximo
    return validar
```

No `main`:

1) Crie `validar_pressao = criar_validador(90, 140)`.
2) Crie `validar_temp = criar_validador(35.0, 37.5)`.
3) Execute 4 testes e exiba resultado (`True`/`False`):
   - `validar_pressao(120)` → `True`
   - `validar_pressao(160)` → `False`
   - `validar_temp(36.8)` → `True`
   - `validar_temp(38.0)` → `False`

Exemplo de saida:

```
Pressao 120: True
Pressao 160: False
Temp 36.8: True
Temp 38.0: False
```

## Passo a passo

1. Defina a funcao externa `criar_validador(minimo, maximo)` — ela recebe a configuracao da faixa.
2. Dentro dela, defina `validar(valor) -> bool` retornando `minimo <= valor <= maximo` (comparacao encadeada do Python testa as duas pontas de uma vez).
3. Retorne `validar` sem parenteses — a fabrica devolve a funcao configurada.
4. No corpo principal, crie dois validadores independentes:
   - `validar_pressao = criar_validador(90, 140)`;
   - `validar_temp = criar_validador(35.0, 37.5)`.
5. Execute os 4 testes do enunciado e exiba cada um no formato `Pressao 120: True` (use f-string).
6. Confira que cada closure lembra a SUA faixa: pressao usa 90-140, temperatura usa 35.0-37.5.

## Como executar

```bash
cd "73_closure_fabrica_validadores"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def criar_validador(minimo, maximo):
    # Funcao interna captura minimo e maximo do escopo externo
    def validar(valor):
        # Comparacao encadeada: True se valor esta dentro da faixa
        return minimo <= valor <= maximo

    # Devolve o validador ja configurado com a faixa
    return validar


# Cada exame tem sua propria faixa — a fabrica evita repetir a regra
validar_pressao = criar_validador(90, 140)
validar_temp = criar_validador(35.0, 37.5)

# 4 testes pedidos, cada closure usando a faixa que capturou
print(f"Pressao 120: {validar_pressao(120)}")  # dentro de 90..140 -> True
print(f"Pressao 160: {validar_pressao(160)}")  # acima de 140 -> False
print(f"Temp 36.8: {validar_temp(36.8)}")      # dentro de 35.0..37.5 -> True
print(f"Temp 38.0: {validar_temp(38.0)}")      # acima de 37.5 -> False
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Fabrica de validadores de faixa para sinais vitais.

Padrao muito comum em producao: regras parametrizadas viram funcoes
configuradas uma unica vez e reutilizadas em todo o fluxo (formularios,
pipelines de dados, triagem clinica).
"""

from collections.abc import Callable

# Validador: recebe um valor numerico e responde se esta na faixa
Validador = Callable[[float], bool]


def criar_validador(minimo: float, maximo: float) -> Validador:
    """Retorna funcao que valida se um valor esta em [minimo, maximo]."""

    def validar(valor: float) -> bool:
        # minimo e maximo ficam capturados no closure;
        # a comparacao encadeada testa as duas pontas de uma vez
        return minimo <= valor <= maximo

    return validar


def main() -> None:
    # Faixas clinicas configuradas uma unica vez
    validar_pressao = criar_validador(90, 140)
    validar_temp = criar_validador(35.0, 37.5)

    # Pares (rotulo, validador, valor) evitam repetir print manualmente
    testes = [
        ("Pressao", validar_pressao, 120),
        ("Pressao", validar_pressao, 160),
        ("Temp", validar_temp, 36.8),
        ("Temp", validar_temp, 38.0),
    ]

    for rotulo, validador, valor in testes:
        print(f"{rotulo} {valor}: {validador(valor)}")


if __name__ == "__main__":
    main()
```

</details>
