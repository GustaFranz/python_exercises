# 119 - Refatoracao: renomear variaveis

## Objetivo

Substituir nomes confusos por nomes descritivos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / scripts |
| **Solicitacao** | Tornar script de verificacao de disco legivel para novo tecnico. |

## Enunciado

Refatore o script abaixo renomeando variaveis confusas (mantenha a mesma logica):

```python
x = 85
l = ["disco1", "disco2"]
i = 0
while i < len(l):
    print(l[i], "uso:", x, "%")
    if x > 80:
        print("ALERTA:", l[i])
    i += 1
```

Mapeamento sugerido:

- `x` → `uso_percentual`
- `l` → `discos`
- `i` → `indice`

Regra de negocio: exibir alerta se `uso_percentual > 80`.

Exiba o status de cada disco com os novos nomes.

## Passo a passo

1. Copie o script legado e aplique o mapeamento de nomes: `x` vira `uso_percentual`, `l` vira `discos` e `i` vira `indice`.
2. Mantenha os mesmos valores: `uso_percentual = 85` e `discos = ["disco1", "disco2"]`.
3. Mantenha a mesma estrutura do `while indice < len(discos)` com `indice += 1` no final — neste exercicio a meta e legibilidade, nao mudar a logica.
4. Dentro do loop, imprima o status (`discos[indice], "uso:", uso_percentual, "%"`) e o alerta quando `uso_percentual > 80`.
5. Rode e confira que a saida e identica a do script original — refatoracao nao muda comportamento, so a clareza.

## Como executar

```bash
cd "119_refatoracao_renomear_variaveis"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Antes: x = 85 — impossivel saber o que "x" significa
# Depois: o nome carrega o significado (percentual de uso do disco)
uso_percentual = 85

# Antes: l = [...] — "l" ainda confunde com o numero 1
discos = ["disco1", "disco2"]

# Antes: i — agora o papel de indice do loop fica explicito
indice = 0

# Mesma estrutura do script original: so os nomes mudaram
while indice < len(discos):
    print(discos[indice], "uso:", uso_percentual, "%")
    # Regra de negocio: alerta acima de 80% de uso
    if uso_percentual > 80:
        print("ALERTA:", discos[indice])
    indice += 1
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
# Constante nomeada: a regra "alerta acima de 80%" ganha um nome oficial
LIMITE_ALERTA = 80


def verificar_discos(discos: list[str], uso_percentual: int) -> None:
    """Exibe o status de cada disco e alerta quando o uso passa do limite."""
    # Alem de renomear, um dev senior trocaria o while com indice manual
    # por um for direto: menos variaveis, zero risco de loop infinito.
    # A saida continua identica a do script original.
    for disco in discos:
        print(disco, "uso:", uso_percentual, "%")
        if uso_percentual > LIMITE_ALERTA:
            print("ALERTA:", disco)


def main() -> None:
    discos = ["disco1", "disco2"]
    uso_percentual = 85
    verificar_discos(discos, uso_percentual)


if __name__ == "__main__":
    main()
```

</details>
