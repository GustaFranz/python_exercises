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

## Como executar

```bash
cd "49_excecao_validar_idade"
python main.py
```
