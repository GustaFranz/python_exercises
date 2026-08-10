# 49 - Excecao customizada: validar idade

## Objetivo

Crie IdadeInvalidaError e validar_idade(idade) com minimo 16.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Academia Prime |
| **Setor** | Fitness / matriculas |
| **Solicitacao** | Impedir cadastro de menores de 16 anos na musculacao. |

## Enunciado

1) Crie a excecao:
```python
class IdadeInvalidaError(Exception):
    pass
```

2) Implemente:
```python
def validar_idade(idade: int) -> None:
    # levanta IdadeInvalidaError se idade < 16
    # mensagem deve informar idade minima e valor recebido
```

3) Teste com idades `15`, `16` e `22`:
   - Idade `15`: use `try/except` e exiba mensagem de erro.
   - Idades `16` e `22`: exiba `"Cadastro liberado"`.

Exemplo de saida:

```
Erro: Idade minima 16. Recebido: 15
Cadastro liberado
Cadastro liberado
```

## Passo a passo

1. Defina a constante `IDADE_MINIMA = 16` no topo do script.
2. Defina a classe `IdadeInvalidaError(Exception)` com corpo `pass` (ou docstring).
3. Defina `def validar_idade(idade: int) -> None:` que levanta `raise IdadeInvalidaError(f"Idade minima {IDADE_MINIMA}. Recebido: {idade}")` quando `idade < IDADE_MINIMA`; se a idade for valida, a funcao simplesmente nao faz nada (retorno implicito `None`).
4. Teste a idade `15` dentro de `try:` e capture com `except IdadeInvalidaError as e:`, exibindo `f"Erro: {e}"`.
5. Teste as idades `16` e `22` chamando `validar_idade(...)` direto e exibindo `"Cadastro liberado"` apos cada chamada.

## Como executar

```bash
cd "49_excecao_validar_idade"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Regra de negocio centralizada em constante: facil de ajustar depois
IDADE_MINIMA = 16


# Excecao customizada para a regra de idade da academia
class IdadeInvalidaError(Exception):
    pass


def validar_idade(idade):
    # Levanta erro com mensagem que informa o minimo e o valor recebido
    if idade < IDADE_MINIMA:
        raise IdadeInvalidaError(f"Idade minima {IDADE_MINIMA}. Recebido: {idade}")
    # Idade valida: a funcao nao precisa retornar nada


# Idade 15: invalida — captura o erro para nao derrubar o programa
try:
    validar_idade(15)
except IdadeInvalidaError as e:
    print(f"Erro: {e}")

# Idades 16 e 22: validas — nenhum erro e levantado
validar_idade(16)
print("Cadastro liberado")

validar_idade(22)
print("Cadastro liberado")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Validacao de idade minima para matricula na musculacao."""

IDADE_MINIMA = 16


class IdadeInvalidaError(Exception):
    """Idade abaixo do minimo permitido para matricula."""


def validar_idade(idade: int) -> None:
    """Levanta IdadeInvalidaError se a idade for menor que IDADE_MINIMA."""
    if idade < IDADE_MINIMA:
        raise IdadeInvalidaError(f"Idade minima {IDADE_MINIMA}. Recebido: {idade}")


def main() -> None:
    # Um unico loop cobre todos os casos de teste
    for idade in (15, 16, 22):
        try:
            validar_idade(idade)
        except IdadeInvalidaError as erro:
            # Caso invalido: mensagem amigavel sem derrubar o programa
            print(f"Erro: {erro}")
        else:
            # else roda apenas quando o try nao levantou excecao
            print("Cadastro liberado")


if __name__ == "__main__":
    main()
```

</details>
