# 42 - DESAFIO - Pipeline de dados escolares

## Objetivo

Montar pipeline merge + JSON + CSV + with open em um case de dados.

## Conteudos cobertos

- Merge de duas fontes
- Persistencia JSON
- Leitura/escrita CSV
- Context manager `with open`

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DataEdu Analytics |
| **Setor** | Educacao / engenharia de dados junior |
| **Solicitacao** | Pipeline de staging: cruzar cadastro e notas, persistir JSON e exportar CSV limpo. |

## Enunciado

Fontes em memoria (pode gravar em arquivos no inicio):

**cadastro.json** (lista):
```json
[{"id": 1, "nome": "Ana", "turma": "7A"}, {"id": 2, "nome": "Bruno", "turma": "7B"}, {"id": 3, "nome": "Carla", "turma": "7A"}]
```

**notas.csv**:
```
id,nota
1,8.0
2,5.5
4,9.0
```

Checklist:

1) Com `with open`, carregue JSON e CSV.
2) Faca merge (left join por `id`): aluno sem nota -> `nota: None`; nota orfa (id 4) vai para lista de inconsistencias.
3) Persista o resultado consolidado em `saida/consolidado.json`.
4) Exporte apenas registros com nota valida para `saida/aprovacao.csv` (id,nome,turma,nota,status) onde status = aprovado se nota >= 6.
5) Imprima resumo do pipeline: lidos, consolidados, inconsistencias, exportados.

## Passo a passo

1. Importe `json`, `csv` e `os` no topo do script.
2. Defina constantes: `ARQ_CADASTRO = "cadastro.json"`, `ARQ_NOTAS = "notas.csv"`, `PASTA_SAIDA = "saida"` e `NOTA_APROVACAO = 6.0`.
3. Defina `preparar_arquivos()` que grava as duas fontes em disco: `cadastro.json` com `json.dump(...)` e `notas.csv` com `f.write(...)`, ambos usando `with open(..., "w", encoding="utf-8")`.
4. Defina `carregar_fontes()` que retorna `(cadastro, notas)`: leia o JSON com `json.load` e o CSV com `csv.DictReader` (use `newline=""` ao abrir o CSV).
5. Defina `merge_left(cadastro, notas)`:
   - Monte o indice `indice_notas = {int(r["id"]): float(r["nota"]) for r in notas}` (o CSV entrega tudo como string).
   - Crie `consolidado`: para cada aluno, copie o dict e adicione `"nota": indice_notas.get(aluno["id"])` — o `.get` devolve `None` quando o aluno nao tem nota.
   - Crie `inconsistencias`: ids do indice de notas que nao existem no cadastro (use um `set` com os ids do cadastro para testar).
   - Retorne `(consolidado, inconsistencias)`.
6. Crie a pasta de saida com `os.makedirs(PASTA_SAIDA, exist_ok=True)` e grave `saida/consolidado.json` com `json.dump(..., ensure_ascii=False, indent=2)`.
7. Defina `exportar_csv(consolidado)`: filtre apenas registros com `nota is not None`, grave `saida/aprovacao.csv` com `csv.writer` (cabecalho `id,nome,turma,nota,status`) e calcule `status = "aprovado" if nota >= NOTA_APROVACAO else "reprovado"`. Retorne quantos registros foram exportados.
8. Chame as funcoes em sequencia e imprima o resumo: lidos, consolidados, inconsistencias (quantidade e conteudo) e exportados.

## Como executar

```bash
cd "42_desafio_pipeline_dados_escolares"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import csv
import json
import os

# Constantes no topo: caminhos e regra de negocio em um unico lugar
ARQ_CADASTRO = "cadastro.json"
ARQ_NOTAS = "notas.csv"
PASTA_SAIDA = "saida"
NOTA_APROVACAO = 6.0

# Dados de origem do enunciado (gravados em arquivos no inicio)
CADASTRO_INICIAL = [
    {"id": 1, "nome": "Ana", "turma": "7A"},
    {"id": 2, "nome": "Bruno", "turma": "7B"},
    {"id": 3, "nome": "Carla", "turma": "7A"},
]
NOTAS_INICIAIS = "id,nota\n1,8.0\n2,5.5\n4,9.0\n"


def preparar_arquivos():
    # Grava as fontes em disco para o pipeline ser reproduzivel
    with open(ARQ_CADASTRO, "w", encoding="utf-8") as f:
        json.dump(CADASTRO_INICIAL, f, ensure_ascii=False, indent=2)
    with open(ARQ_NOTAS, "w", encoding="utf-8") as f:
        f.write(NOTAS_INICIAIS)


def carregar_fontes():
    # json.load converte o texto do arquivo em lista de dicts
    with open(ARQ_CADASTRO, "r", encoding="utf-8") as f:
        cadastro = json.load(f)
    # DictReader devolve cada linha do CSV como dict de strings
    with open(ARQ_NOTAS, "r", encoding="utf-8", newline="") as f:
        notas = list(csv.DictReader(f))
    return cadastro, notas


def merge_left(cadastro, notas):
    # Indice id -> nota: converte os textos do CSV para int e float
    indice_notas = {int(r["id"]): float(r["nota"]) for r in notas}
    # Conjunto com os ids conhecidos para detectar notas orfas
    ids_cadastro = {aluno["id"] for aluno in cadastro}

    # Left join: todo aluno entra; sem nota o .get devolve None
    consolidado = [
        {**aluno, "nota": indice_notas.get(aluno["id"])} for aluno in cadastro
    ]
    # Nota cujo id nao existe no cadastro vira inconsistencia
    inconsistencias = [
        {"id": id_, "nota": nota}
        for id_, nota in indice_notas.items()
        if id_ not in ids_cadastro
    ]
    return consolidado, inconsistencias


def persistir_json(consolidado):
    # exist_ok=True evita erro se a pasta ja existir
    os.makedirs(PASTA_SAIDA, exist_ok=True)
    caminho = os.path.join(PASTA_SAIDA, "consolidado.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(consolidado, f, ensure_ascii=False, indent=2)


def exportar_csv(consolidado):
    # Exporta apenas registros com nota valida (nao None)
    com_nota = [r for r in consolidado if r["nota"] is not None]
    caminho = os.path.join(PASTA_SAIDA, "aprovacao.csv")
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["id", "nome", "turma", "nota", "status"])
        for r in com_nota:
            # Regra de aprovacao aplicada na exportacao
            status = "aprovado" if r["nota"] >= NOTA_APROVACAO else "reprovado"
            escritor.writerow([r["id"], r["nome"], r["turma"], r["nota"], status])
    # Retorna a contagem para o resumo final
    return len(com_nota)


# Execucao do pipeline, etapa por etapa
preparar_arquivos()
cadastro, notas = carregar_fontes()
consolidado, inconsistencias = merge_left(cadastro, notas)
persistir_json(consolidado)
exportados = exportar_csv(consolidado)

# Resumo final com as metricas pedidas
print(f"Lidos: {len(cadastro)} alunos, {len(notas)} notas")
print(f"Consolidados: {len(consolidado)}")
print(f"Inconsistencias: {len(inconsistencias)} -> {inconsistencias}")
print(f"Exportados: {exportados}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Pipeline de staging: cruza cadastro e notas, persiste JSON e exporta CSV."""

import csv
import json
from pathlib import Path

# Path centraliza os caminhos e facilita compor pastas com o operador /
ARQ_CADASTRO = Path("cadastro.json")
ARQ_NOTAS = Path("notas.csv")
PASTA_SAIDA = Path("saida")
NOTA_APROVACAO = 6.0

CADASTRO_INICIAL = [
    {"id": 1, "nome": "Ana", "turma": "7A"},
    {"id": 2, "nome": "Bruno", "turma": "7B"},
    {"id": 3, "nome": "Carla", "turma": "7A"},
]
NOTAS_INICIAIS = "id,nota\n1,8.0\n2,5.5\n4,9.0\n"


def preparar_fontes() -> None:
    """Grava as fontes de exemplo para o pipeline ser self-contained."""
    # write_text abre, escreve e fecha o arquivo em uma unica chamada
    ARQ_CADASTRO.write_text(
        json.dumps(CADASTRO_INICIAL, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    ARQ_NOTAS.write_text(NOTAS_INICIAIS, encoding="utf-8")


def carregar_fontes() -> tuple[list[dict], dict[int, float]]:
    """Le as duas fontes e devolve as notas ja indexadas por id."""
    cadastro = json.loads(ARQ_CADASTRO.read_text(encoding="utf-8"))
    # Dict comprehension converte tipos direto na leitura do CSV
    with ARQ_NOTAS.open(encoding="utf-8", newline="") as f:
        indice_notas = {int(r["id"]): float(r["nota"]) for r in csv.DictReader(f)}
    return cadastro, indice_notas


def consolidar(
    cadastro: list[dict], indice_notas: dict[int, float]
) -> tuple[list[dict], list[dict]]:
    """Left join por id: aluno sem nota recebe None; nota orfa vira inconsistencia."""
    consolidado = [
        {**aluno, "nota": indice_notas.get(aluno["id"])} for aluno in cadastro
    ]
    ids_conhecidos = {aluno["id"] for aluno in cadastro}
    inconsistencias = [
        {"id": id_, "nota": nota}
        for id_, nota in indice_notas.items()
        if id_ not in ids_conhecidos
    ]
    return consolidado, inconsistencias


def exportar(consolidado: list[dict]) -> int:
    """Persiste o JSON consolidado e o CSV de aprovacao; retorna exportados."""
    PASTA_SAIDA.mkdir(exist_ok=True)
    (PASTA_SAIDA / "consolidado.json").write_text(
        json.dumps(consolidado, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Guard: so registros com nota entram no CSV de aprovacao
    com_nota = [r for r in consolidado if r["nota"] is not None]
    with (PASTA_SAIDA / "aprovacao.csv").open("w", encoding="utf-8", newline="") as f:
        # DictWriter casa cada chave do dict com a coluna certa
        escritor = csv.DictWriter(f, fieldnames=["id", "nome", "turma", "nota", "status"])
        escritor.writeheader()
        for registro in com_nota:
            status = "aprovado" if registro["nota"] >= NOTA_APROVACAO else "reprovado"
            escritor.writerow({**registro, "status": status})
    return len(com_nota)


def main() -> None:
    preparar_fontes()
    cadastro, indice_notas = carregar_fontes()
    consolidado, inconsistencias = consolidar(cadastro, indice_notas)
    exportados = exportar(consolidado)

    # Resumo alinhado facilita leitura em terminal
    print(f"Lidos:           {len(cadastro)} alunos / {len(indice_notas)} notas")
    print(f"Consolidados:    {len(consolidado)}")
    print(f"Inconsistencias: {len(inconsistencias)} -> {inconsistencias}")
    print(f"Exportados:      {exportados}")


# Permite importar as funcoes em testes sem executar o pipeline
if __name__ == "__main__":
    main()
```

</details>
