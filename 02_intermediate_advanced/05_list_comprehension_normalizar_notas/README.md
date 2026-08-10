# 05 - List comprehension: pipeline de limpeza de notas

## Objetivo

Simular pipeline de qualidade de dados com list comprehension e regras de negocio.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Municipal de Educacao |
| **Setor** | Gestao publica escolar / dados |
| **Solicitacao** | Limpar lote de notas do staging antes de publicar no dashboard da rede. |

## Enunciado

notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]

Regras do pipeline:
- Aceitar apenas `int` ou `float` (ignorar `None` e strings).
- Nota valida: entre 0 e 10 (inclusive).
- Arredondar validas para 1 casa decimal.
- Classificar: `aprovado` (>= 6) ou `recuperacao` (< 6).

Tarefas:
1) `notas_validas` com list comprehension (filtro).
2) `notas_arredondadas` com list comprehension (`round`).
3) `status_lote` com list comprehension de dicts `{nota, status}`.
4) Relatorio de auditoria: recebidas, descartadas, % descartado, media das validas,
   quantidade aprovado/recuperacao, lista final de status.

## Passo a passo

1. Crie a lista `notas_brutas` com os 12 valores do enunciado (incluindo os invalidos).
2. Defina uma funcao auxiliar `eh_nota_valida(valor)` que retorna `True` apenas se o valor for numerico e estiver no intervalo 0 a 10. Use `isinstance(valor, (int, float)) and not isinstance(valor, bool)` — o `not isinstance(..., bool)` e necessario porque `True`/`False` sao subclasses de `int` em Python.
3. Crie `notas_validas` com list comprehension filtrando com a funcao: `[nota for nota in notas_brutas if eh_nota_valida(nota)]`.
4. Crie `notas_arredondadas` com outra comprehension aplicando `round(float(nota), 1)` em cada nota valida.
5. Crie `status_lote` com comprehension de dicts: `{"nota": nota, "status": "aprovado" if nota >= 6.0 else "recuperacao"}` para cada nota arredondada.
6. Calcule os indicadores da auditoria: total recebidas (`len(notas_brutas)`), total descartadas (recebidas menos validas), percentual de descarte, media das validas (`sum / len`, com protecao contra lista vazia) e as quantidades de `aprovado` e `recuperacao` (use `sum(1 for item in status_lote if ...)`).
7. Exiba o relatorio de auditoria com todos os indicadores e, ao final, a lista `status_lote` formatada (um item por linha).

## Como executar

```bash
cd "05_list_comprehension_normalizar_notas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Lote bruto do staging, com erros propositais (enunciado)
notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]

# Regra de aprovacao como constante nomeada
NOTA_APROVACAO = 6.0


def eh_nota_valida(valor):
    """Retorna True se o valor for numerico (nao bool) e estiver entre 0 e 10.

    bool e checado antes porque True/False sao subclasses de int em Python:
    sem essa checagem, True passaria como se fosse a nota 1.
    """
    if isinstance(valor, bool):
        return False
    return isinstance(valor, (int, float)) and 0 <= valor <= 10


# Etapa 1: filtra o lote mantendo apenas valores validos
notas_validas = [nota for nota in notas_brutas if eh_nota_valida(nota)]

# Etapa 2: padroniza a escala com 1 casa decimal (float garante 0 -> 0.0)
notas_arredondadas = [round(float(nota), 1) for nota in notas_validas]

# Etapa 3: mapeia cada nota para o status com ternario dentro do dict
status_lote = [
    {"nota": nota, "status": "aprovado" if nota >= NOTA_APROVACAO else "recuperacao"}
    for nota in notas_arredondadas
]

# Etapa 4: indicadores de auditoria do lote
total_recebidas = len(notas_brutas)
total_descartadas = total_recebidas - len(notas_validas)
# Ternarios protegem contra divisao por zero em lotes vazios
pct_descartadas = (total_descartadas / total_recebidas * 100) if total_recebidas else 0.0
media_validas = (sum(notas_arredondadas) / len(notas_arredondadas)) if notas_arredondadas else 0.0
# Generator expression conta cada grupo sem criar lista intermediaria
qtd_aprovados = sum(1 for item in status_lote if item["status"] == "aprovado")
qtd_recuperacao = sum(1 for item in status_lote if item["status"] == "recuperacao")

print("=== RELATORIO DE AUDITORIA DO LOTE ===")
print(f"Total recebidas:   {total_recebidas}")
print(f"Total descartadas: {total_descartadas}")
print(f"% Descartadas:     {pct_descartadas:.2f}%")
print(f"Media das validas: {media_validas:.2f}")
print(f"Aprovados:         {qtd_aprovados}")
print(f"Recuperacao:       {qtd_recuperacao}")
print("\n--- DADOS FINAIS PARA O DASHBOARD ---")
for item in status_lote:
    print(f'  nota: {item["nota"]:<5} | status: {item["status"]}')
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Pipeline de sanitizacao do lote de notas do staging."""

from statistics import fmean

# Limites e regra de aprovacao centralizados no topo do modulo
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0
NOTA_APROVACAO = 6.0


def validar_nota(valor: object) -> float | None:
    """Devolve a nota como float se for valida, senao None.

    Guard clauses deixam cada regra de descarte explicita e em ordem:
    primeiro tipo (bool e subclasse de int!), depois intervalo.
    """
    if isinstance(valor, bool):
        return None
    if not isinstance(valor, (int, float)):
        return None
    if not NOTA_MINIMA <= valor <= NOTA_MAXIMA:
        return None
    return round(float(valor), 1)


def classificar(nota: float) -> str:
    """Regra de negocio de classificacao do aluno."""
    return "aprovado" if nota >= NOTA_APROVACAO else "recuperacao"


def main() -> None:
    # Lote bruto do staging (enunciado)
    notas_brutas = [7.5, -1, 8.0, 11, 6.5, None, 4.0, 15, 9.0, "7", 0, 10]

    # Valida e arredonda em uma passagem: o walrus (:=) guarda o resultado
    # de validar_nota para reutilizar no filtro sem chamar a funcao duas vezes
    notas_validas = [
        nota for bruta in notas_brutas
        if (nota := validar_nota(bruta)) is not None
    ]

    # Lista final para o dashboard: nota + status calculado
    status_lote = [{"nota": nota, "status": classificar(nota)} for nota in notas_validas]

    # Indicadores de auditoria
    total_recebidas = len(notas_brutas)
    total_descartadas = total_recebidas - len(notas_validas)
    pct_descartadas = (total_descartadas / total_recebidas * 100) if total_recebidas else 0.0
    # fmean e a media aritmetica da stdlib, mais clara que sum/len manual
    media_validas = fmean(notas_validas) if notas_validas else 0.0
    qtd_aprovados = sum(1 for item in status_lote if item["status"] == "aprovado")
    qtd_recuperacao = len(status_lote) - qtd_aprovados

    print("=== RELATORIO DE AUDITORIA DO LOTE ===")
    print(f"Total recebidas:   {total_recebidas}")
    print(f"Total descartadas: {total_descartadas}")
    print(f"% Descartadas:     {pct_descartadas:.2f}%")
    print(f"Media das validas: {media_validas:.2f}")
    print(f"Aprovados:         {qtd_aprovados}")
    print(f"Recuperacao:       {qtd_recuperacao}")
    print("\n--- DADOS FINAIS PARA O DASHBOARD ---")
    for item in status_lote:
        print(f'  nota: {item["nota"]:<5} | status: {item["status"]}')


if __name__ == "__main__":
    main()
```

</details>
