# 126 - Assert: testes separados com regras de negocio

## Objetivo

Separar implementacao e testes em modulos distintos, cobrindo casos de borda de regras comerciais.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DevEscola Labs |
| **Setor** | Educacao / qualidade |
| **Solicitacao** | Validar modulo de desconto e pedido minimo antes de liberar checkout do bazar escolar. |

## Estrutura de arquivos

```
126_assert_testes_separados/
├── README.md
├── main.py       # orquestracao / instrucoes
├── calculos.py   # regras de negocio (implementar)
└── testes.py     # asserts de casos normais e borda (implementar)
```

## Enunciado

- Em `calculos.py`, implemente:
  - `calcular_desconto(valor, percentual)` — retorna valor com desconto aplicado
  - `validar_pedido(qtd)` — retorna `True` se quantidade valida para checkout
- Em `testes.py`, importe `calculos` e cubra casos de borda com `assert`:
  - desconto 0%, 100%, valor zero, percentual negativo, percentual acima de 100
  - pedido com qtd 0, negativa e positiva valida
- Execute `python testes.py` e exiba mensagem de sucesso ao final.
- `main.py` orienta execucao dos testes (sem duplicar logica de negocio).

## Passo a passo

1. Em `calculos.py`, implemente `calcular_desconto(valor: float, percentual: float) -> float`:
   - se `percentual < 0 ou percentual > 100`, faca `raise ValueError(...)` (aqui o percentual vai de 0 a 100, diferente do exercicio 124);
   - senao, retorne `valor * (1 - percentual / 100)`.
2. Ainda em `calculos.py`, implemente `validar_pedido(qtd: int) -> bool` retornando `qtd >= 1` (a propria expressao booleana ja e o retorno).
3. Em `testes.py`, importe as funcoes: `from calculos import calcular_desconto, validar_pedido`.
4. Escreva os asserts dos casos normais e de borda do desconto:
   - `calcular_desconto(100, 0) == 100`, `calcular_desconto(100, 10) == 90`, `calcular_desconto(100, 100) == 0`, `calcular_desconto(0, 50) == 0`.
5. Para os percentuais invalidos (`-5` e `150`), use o padrao `try/except ValueError`: chame a funcao dentro do `try`; se NAO levantar erro, faca `assert False, "deveria ter levantado ValueError"`; no `except`, siga em frente (teste passou).
6. Escreva os asserts do pedido: `validar_pedido(0) == False`, `validar_pedido(-3) == False`, `validar_pedido(5) == True`.
7. Coloque a execucao dos asserts dentro de `if __name__ == "__main__":` e finalize com `print("Todos os testes passaram.")`.
8. Em `main.py`, apenas exiba a orientacao: `print("Execute: python testes.py")` — sem duplicar logica de negocio.

## Como executar

```bash
cd "126_assert_testes_separados"
python testes.py
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`calculos.py`**

```python
"""Regras de negocio do checkout do bazar escolar."""


def calcular_desconto(valor: float, percentual: float) -> float:
    # Percentual fora de [0, 100] e erro de programacao de quem chamou:
    # levantar ValueError e melhor que devolver um valor silenciosamente errado
    if percentual < 0 or percentual > 100:
        raise ValueError(f"Percentual invalido: {percentual}")
    # Converte percentual (0-100) em fator: 10% -> pagar 90% do valor
    return valor * (1 - percentual / 100)


def validar_pedido(qtd: int) -> bool:
    # A comparacao ja produz True/False — nao precisa de if/else
    return qtd >= 1
```

**`testes.py`**

```python
"""Testes do modulo calculos — execute com: python testes.py"""

from calculos import calcular_desconto, validar_pedido


def testar_calcular_desconto():
    # Casos normais e bordas do intervalo valido
    assert calcular_desconto(100, 0) == 100, "0% nao deve alterar o valor"
    assert calcular_desconto(100, 10) == 90, "10% sobre 100 deveria dar 90"
    assert calcular_desconto(100, 100) == 0, "100% deve zerar o valor"
    assert calcular_desconto(0, 50) == 0, "valor zero segue zero com desconto"

    # Percentual negativo DEVE levantar ValueError
    try:
        calcular_desconto(100, -5)
        assert False, "percentual negativo deveria levantar ValueError"
    except ValueError:
        pass  # comportamento esperado: o teste passa

    # Percentual acima de 100 DEVE levantar ValueError
    try:
        calcular_desconto(100, 150)
        assert False, "percentual > 100 deveria levantar ValueError"
    except ValueError:
        pass


def testar_validar_pedido():
    # Bordas: zero e negativo bloqueiam; positivo libera
    assert validar_pedido(0) == False, "qtd 0 nao pode fechar pedido"
    assert validar_pedido(-3) == False, "qtd negativa nao pode fechar pedido"
    assert validar_pedido(5) == True, "qtd 5 deve liberar o pedido"


if __name__ == "__main__":
    # So roda a suite quando executado diretamente (nao ao importar)
    testar_calcular_desconto()
    testar_validar_pedido()
    print("Todos os testes passaram.")
```

**`main.py`**

```python
# main.py apenas orienta — a logica vive em calculos.py e os testes em testes.py
print("Modulo de checkout do bazar escolar.")
print("Execute: python testes.py")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`calculos.py`**

```python
"""Regras de negocio do checkout do bazar escolar.

Modulo puro (sem prints, sem input): facil de importar e de testar.
"""

PERCENTUAL_MINIMO = 0.0
PERCENTUAL_MAXIMO = 100.0
QTD_MINIMA_PEDIDO = 1


def calcular_desconto(valor: float, percentual: float) -> float:
    """Aplica desconto percentual (0 a 100) sobre o valor.

    Raises:
        ValueError: se o percentual estiver fora do intervalo [0, 100].
    """
    # Guard clause: valida a entrada antes de qualquer calculo
    if not PERCENTUAL_MINIMO <= percentual <= PERCENTUAL_MAXIMO:
        raise ValueError(f"Percentual invalido: {percentual} (esperado 0 a 100)")
    return valor * (1 - percentual / 100)


def validar_pedido(qtd: int) -> bool:
    """Retorna True se a quantidade permite finalizar o pedido."""
    return qtd >= QTD_MINIMA_PEDIDO
```

**`testes.py`**

```python
"""Testes do modulo calculos — execute com: python testes.py

Com pytest o codigo ficaria menor: os try/except de erro esperado
virariam `with pytest.raises(ValueError):` e nao precisariamos
chamar as funcoes de teste manualmente — o runner as descobre pelo
prefixo test_.
"""

from calculos import calcular_desconto, validar_pedido


def _espera_value_error(funcao, *args) -> None:
    """Auxiliar: garante que a chamada levanta ValueError (mini pytest.raises)."""
    try:
        funcao(*args)
    except ValueError:
        return  # erro esperado aconteceu: teste passa
    raise AssertionError(f"{funcao.__name__}{args} deveria levantar ValueError")


def test_desconto_casos_validos() -> None:
    assert calcular_desconto(100, 0) == 100, "0% nao deve alterar o valor"
    assert calcular_desconto(100, 10) == 90, "10% sobre 100 deveria dar 90"
    assert calcular_desconto(100, 100) == 0, "100% deve zerar o valor"
    assert calcular_desconto(0, 50) == 0, "valor zero segue zero"


def test_desconto_percentuais_invalidos() -> None:
    _espera_value_error(calcular_desconto, 100, -5)
    _espera_value_error(calcular_desconto, 100, 150)


def test_validar_pedido() -> None:
    assert validar_pedido(0) is False, "qtd 0 bloqueia o checkout"
    assert validar_pedido(-3) is False, "qtd negativa bloqueia o checkout"
    assert validar_pedido(5) is True, "qtd valida libera o checkout"


if __name__ == "__main__":
    test_desconto_casos_validos()
    test_desconto_percentuais_invalidos()
    test_validar_pedido()
    print("Todos os testes passaram.")
```

**`main.py`**

```python
"""Ponto de entrada: orienta a execucao da suite sem duplicar logica."""

if __name__ == "__main__":
    print("Modulo de checkout do bazar escolar.")
    print("Execute: python testes.py")
```

</details>
