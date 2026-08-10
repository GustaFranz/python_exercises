# 117 - Introducao a refatoracao

## Objetivo

Identificar problemas em codigo monolitico e planejar separacao em funcoes.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DevEscola Labs |
| **Setor** | Educacao / formacao dev |
| **Solicitacao** | Reorganizar script legado de notas antes de integrar ao sistema novo. |

## Visao do bloco (exercicios 117 a 121)

Topico **Refatoracao**: melhorar estrutura sem mudar comportamento.

| # | Foco |
|---|------|
| 117 | Introducao + identificar codigo monolitico |
| 118 | Extrair funcoes |
| 119 | Renomear variaveis confusas |
| 120 | Separar I/O, regra e apresentacao |
| 121 | Refatorar script longo (~70 linhas) em funcoes + menu |

## Enunciado

Estude o codigo monolitico abaixo (nao execute — refatore):

```python
notas = [7, 8, 5, 9, 6]
s = 0
for n in notas:
    s = s + n
m = s / len(notas)
if m >= 7:
    print("Turma aprovada com media", m)
else:
    print("Turma reprovada com media", m)
for n in notas:
    if n < 7:
        print("Recuperacao:", n)
```

Tarefas:

1) Em comentarios, liste **3 problemas** desse codigo (ex.: nomes confusos, tudo no fluxo principal).
2) Implemente as funcoes:
   - `calcular_media(notas) -> float`
   - `turma_aprovada(media, corte=7) -> bool`
   - `listar_recuperacao(notas, corte=7)` — imprime notas abaixo do corte
3) Monte `main()` limpo que reproduz **exatamente** o mesmo resultado do script original.

## Passo a passo

1. Leia o codigo monolitico e escreva, em comentarios no topo do arquivo, 3 problemas identificados (ex.: nomes `s`, `m`, `n` nao revelam intencao; toda a logica roda solta no fluxo principal; o corte `7` esta repetido como numero magico em dois lugares).
2. Implemente `calcular_media(notas) -> float`: some as notas (pode usar `sum(notas)`) e divida por `len(notas)`.
3. Implemente `turma_aprovada(media, corte=7) -> bool` retornando `media >= corte` — a funcao so decide, nao imprime.
4. Implemente `listar_recuperacao(notas, corte=7)`: percorra as notas e imprima `"Recuperacao:", nota` para cada nota abaixo do corte.
5. Monte `main()` orquestrando: calcule a media, decida aprovacao com `turma_aprovada`, imprima `"Turma aprovada com media"` ou `"Turma reprovada com media"` seguido da media, e chame `listar_recuperacao`.
6. Use a mesma lista `[7, 8, 5, 9, 6]` e confira que a saida e **identica** a do script original: `Turma aprovada com media 7.0`, depois `Recuperacao: 5` e `Recuperacao: 6`.

## Como executar

```bash
cd "117_introducao_refatoracao"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# PROBLEMAS DO CODIGO MONOLITICO:
# 1) Nomes sem significado: s, m, n nao dizem o que armazenam
# 2) Tudo no fluxo principal: impossivel reutilizar ou testar partes
# 3) Numero magico: o corte 7 aparece repetido em dois pontos da logica


def calcular_media(notas):
    # sum() substitui o loop manual de acumulacao (s = s + n)
    return sum(notas) / len(notas)


def turma_aprovada(media, corte=7):
    # Funcao pura: recebe valores, retorna bool, nao imprime nada
    return media >= corte


def listar_recuperacao(notas, corte=7):
    # Unica responsabilidade: mostrar as notas abaixo do corte
    for nota in notas:
        if nota < corte:
            print("Recuperacao:", nota)


def main():
    # Fluxo principal enxuto: apenas orquestra as funcoes
    notas = [7, 8, 5, 9, 6]
    media = calcular_media(notas)

    # Mesmas mensagens do script original (comportamento preservado)
    if turma_aprovada(media):
        print("Turma aprovada com media", media)
    else:
        print("Turma reprovada com media", media)

    listar_recuperacao(notas)


main()
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
# PROBLEMAS DO CODIGO MONOLITICO:
# 1) Nomes de uma letra (s, m, n) escondem a intencao do codigo
# 2) Logica de calculo, decisao e impressao misturadas no fluxo principal
# 3) Corte de aprovacao (7) duplicado como numero magico

# Constante unica: o corte muda em UM lugar e vale para todo o modulo
CORTE_APROVACAO = 7


def calcular_media(notas: list[float]) -> float:
    """Media aritmetica simples das notas."""
    return sum(notas) / len(notas)


def turma_aprovada(media: float, corte: float = CORTE_APROVACAO) -> bool:
    """Regra de negocio isolada: aprovacao por media minima."""
    return media >= corte


def listar_recuperacao(notas: list[float], corte: float = CORTE_APROVACAO) -> None:
    """Imprime as notas abaixo do corte (camada de apresentacao)."""
    for nota in notas:
        if nota < corte:
            print("Recuperacao:", nota)


def main() -> None:
    notas = [7, 8, 5, 9, 6]
    media = calcular_media(notas)

    # Ternario escolhe a palavra; a mensagem continua identica a original
    situacao = "aprovada" if turma_aprovada(media) else "reprovada"
    print(f"Turma {situacao} com media", media)

    listar_recuperacao(notas)


if __name__ == "__main__":
    main()
```

</details>
