# 128 - Type hints: list e dict

## Objetivo

Anotar funcoes que recebem list[str] e retornam dict[str, float].

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | BigData Escolar |
| **Setor** | Educacao / analytics |
| **Solicitacao** | Tipar funcoes do relatorio de frequencia de palavras em redacoes. |

## Enunciado

Implemente com type hints:

```python
def contar_tamanhos(palavras: list[str]) -> dict[str, int]:
    # retorna {palavra: len(palavra)} para cada palavra

def media_tamanhos(palavras: list[str]) -> float:
    # media dos tamanhos; retorna 0.0 se lista vazia
```

No `main`:

1) Teste com `palavras = ["ana", "bolo", "escola"]`.
2) Exiba o dict de tamanhos e a media.

Exemplo de saida:

```
Tamanhos: {'ana': 3, 'bolo': 4, 'escola': 6}
Media: 4.33
```

## Como executar

```bash
cd "128_type_hints_list_dict"
python main.py
```
