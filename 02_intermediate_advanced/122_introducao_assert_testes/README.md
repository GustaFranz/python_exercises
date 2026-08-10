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

## Como executar

```bash
cd "122_introducao_assert_testes"
python main.py
```
