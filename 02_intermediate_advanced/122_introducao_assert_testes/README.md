# 122 - Introducao a testes com assert

## Objetivo

Validar funcao pura de media com assertions.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DevEscola Labs |
| **Setor** | Educacao / qualidade |
| **Solicitacao** | Garantir que funcao de media escolar funciona antes de ir para producao. |

## Visao do bloco (exercicios 122 a 126)

Topico **Testes com assert**: validar comportamento com assercoes simples.

| # | Foco |
|---|------|
| 122 | Introducao + testar media com assert |
| 123 | Asserts para casos de borda |
| 124 | Asserts para funcao de desconto |
| 125 | Suite de asserts para CRUD em memoria |
| 126 | testes.py separado com regras de negocio (desconto/pedido) |

## Enunciado

Implemente:

```python
def media(notas: list[float]) -> float:
    return sum(notas) / len(notas)
```

Escreva testes com `assert` (sem framework externo):

```python
assert media([10, 8, 6]) == 8.0
assert media([7]) == 7.0
assert media([5, 5, 5, 5]) == 5.0
```

Ao final, exiba:

```
Todos os testes passaram.
```

## Passo a passo

1. Defina `media(notas: list[float]) -> float` retornando `sum(notas) / len(notas)`.
2. Abaixo da funcao, escreva os tres testes exatamente como no enunciado: `assert media([10, 8, 6]) == 8.0`, `assert media([7]) == 7.0` e `assert media([5, 5, 5, 5]) == 5.0`.
3. Adicione uma mensagem em cada assert (segundo argumento) para facilitar o diagnostico, ex.: `assert media([7]) == 7.0, "media de um unico valor deve ser o proprio valor"`.
4. Depois dos asserts, exiba `print("Todos os testes passaram.")` — essa linha so executa se nenhum assert falhar.
5. Teste o mecanismo: troque temporariamente um valor esperado (ex.: `== 9.0`) e rode de novo para ver o `AssertionError`; depois desfaca.

## Como executar

```bash
cd "122_introducao_assert_testes"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def media(notas: list[float]) -> float:
    # Funcao pura: mesmo input, mesmo output — por isso e facil de testar
    return sum(notas) / len(notas)


# Cada assert compara o resultado real com o esperado;
# a mensagem apos a virgula aparece no AssertionError se o teste falhar
assert media([10, 8, 6]) == 8.0, "media de [10, 8, 6] deveria ser 8.0"
assert media([7]) == 7.0, "media de um unico valor deve ser o proprio valor"
assert media([5, 5, 5, 5]) == 5.0, "media de valores iguais deve ser o proprio valor"

# So chega aqui se nenhum assert levantou AssertionError
print("Todos os testes passaram.")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Funcao de media escolar validada com assercoes simples.

Em producao esses testes virariam funcoes test_* rodadas pelo pytest:
    def test_media_basica():
        assert media([10, 8, 6]) == 8.0
E bastaria executar `pytest` na pasta — sem print manual de sucesso.
"""

from statistics import fmean


def media(notas: list[float]) -> float:
    """Retorna a media aritmetica das notas.

    fmean() e a forma idiomatica da stdlib: sempre devolve float
    e e mais precisa/rapida que sum/len para listas grandes.
    """
    return fmean(notas)


def testar_media() -> None:
    """Agrupa os testes em uma funcao: organiza e permite reexecutar."""
    assert media([10, 8, 6]) == 8.0, "media de [10, 8, 6] deveria ser 8.0"
    assert media([7]) == 7.0, "lista unitaria deve retornar o proprio valor"
    assert media([5, 5, 5, 5]) == 5.0, "valores iguais devem retornar o proprio valor"


if __name__ == "__main__":
    # O guard evita rodar os testes se o modulo for importado por outro arquivo
    testar_media()
    print("Todos os testes passaram.")
```

</details>
