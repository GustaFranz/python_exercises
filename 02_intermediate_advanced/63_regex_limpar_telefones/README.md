# 63 - Regex: limpar telefones

## Objetivo

Limpe digitos com regex e formate telefones 11 digitos como (XX) XXXXX-XXXX.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Padronizar telefones de responsaveis para formato unico. |

## Enunciado

Lista suja de telefones:
```python
telefones = [
    "(11) 98765-4321",
    "11 987654321",
    "+55 11 98765-4321",
    "11987654321",
]
```

Para cada item:

1) Extraia apenas digitos com `re.sub(r"\D", "", texto)`.
2) Se tiver 11 digitos, formate como `(XX) XXXXX-XXXX`.
3) Ignore entradas com menos de 10 digitos.

Implemente `padronizar_telefone(texto: str) -> str | None` e exiba a lista de telefones formatados.

Exemplo de saida:

```
Telefones padronizados:
(11) 98765-4321
(11) 98765-4321
(11) 98765-4321
(11) 98765-4321
```

## Passo a passo

1. Importe `re` e crie a lista `telefones` com as 4 strings do enunciado.
2. Defina a funcao `padronizar_telefone(texto: str) -> str | None`.
3. Dentro dela, extraia apenas os digitos com `nums = re.sub(r"\D", "", texto)` (`\D` casa tudo que NAO e digito e substitui por vazio).
4. Trate o codigo do pais: se `nums` tiver mais de 11 digitos e comecar com `"55"` (caso do `+55 11 ...`), fique apenas com os 11 ultimos digitos (`nums = nums[-11:]`).
5. Se `len(nums)` for menor que 10, retorne `None` (entrada invalida, sera ignorada).
6. Se tiver 11 digitos, fatie a string para montar o formato: `ddd = nums[0:2]`, `parte1 = nums[2:7]`, `parte2 = nums[7:]` e retorne `f"({ddd}) {parte1}-{parte2}"`.
7. No corpo principal, percorra `telefones`, chame `padronizar_telefone` para cada item e guarde apenas os resultados que nao forem `None` (list comprehension resolve).
8. Exiba o titulo `"Telefones padronizados:"` e cada telefone formatado em uma linha.

## Como executar

```bash
cd "63_regex_limpar_telefones"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import re

# Lista suja vinda do cadastro: formatos variados e codigo de pais
telefones = [
    "(11) 98765-4321",
    "11 987654321",
    "+55 11 98765-4321",
    "11987654321",
]


def padronizar_telefone(texto):
    # \D casa tudo que nao e digito; substituindo por "" sobram so os numeros
    nums = re.sub(r"\D", "", texto)

    # Numeros com +55 viram 13 digitos: descarta o codigo do pais
    # ficando apenas com os 11 ultimos (DDD + celular)
    if len(nums) > 11 and nums.startswith("55"):
        nums = nums[-11:]

    # Menos de 10 digitos nao e telefone valido -> ignora
    if len(nums) < 10:
        return None

    # Fatia a string nas partes do formato (XX) XXXXX-XXXX
    ddd = nums[0:2]      # 2 primeiros digitos = DDD
    parte1 = nums[2:7]   # 5 digitos seguintes
    parte2 = nums[7:]    # 4 digitos finais
    return f"({ddd}) {parte1}-{parte2}"


# Padroniza todos e descarta os None (entradas invalidas)
formatados = []
for telefone in telefones:
    resultado = padronizar_telefone(telefone)
    if resultado is not None:
        formatados.append(resultado)

print("Telefones padronizados:")
for telefone in formatados:
    print(telefone)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Padroniza telefones de responsaveis para o formato (XX) XXXXX-XXXX."""

import re

# Constantes nomeadas: o "porque" dos numeros magicos fica documentado
CODIGO_PAIS = "55"
DIGITOS_CELULAR = 11
DIGITOS_MINIMOS = 10

# Padrao compilado uma vez para reuso em todo o modulo
SO_DIGITOS = re.compile(r"\D")


def padronizar_telefone(texto: str) -> str | None:
    """Extrai os digitos de um telefone sujo e devolve no formato (XX) XXXXX-XXXX.

    Retorna None quando a entrada tem menos digitos que o minimo aceitavel.
    """
    nums = SO_DIGITOS.sub("", texto)

    # Remove o codigo do pais mantendo os 11 ultimos digitos (DDD + numero)
    if len(nums) > DIGITOS_CELULAR and nums.startswith(CODIGO_PAIS):
        nums = nums[-DIGITOS_CELULAR:]

    # Guard clause: descarta entradas curtas demais
    if len(nums) < DIGITOS_MINIMOS:
        return None

    # Fatiamento unico e legivel: (DDD) prefixo-sufixo
    return f"({nums[:2]}) {nums[2:7]}-{nums[7:]}"


def main() -> None:
    telefones = [
        "(11) 98765-4321",
        "11 987654321",
        "+55 11 98765-4321",
        "11987654321",
    ]

    # Chama a funcao uma unica vez por item usando o walrus operator (:=),
    # evitando processar a mesma string duas vezes
    formatados = [
        resultado
        for telefone in telefones
        if (resultado := padronizar_telefone(telefone)) is not None
    ]

    print("Telefones padronizados:")
    print("\n".join(formatados))


if __name__ == "__main__":
    main()
```

</details>
