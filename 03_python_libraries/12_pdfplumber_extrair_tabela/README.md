# 12 - PDFPlumber - Extrair tabela de PDF

## Demanda

A Coordenacao envia notas de projeto pedagogico em PDF. O setor de dados precisa extrair a tabela automaticamente, sem digitacao manual.

## Contexto do problema

Terceira fonte de notas do boletim. PDF e o formato mais dificil de ler.

## Conceitos que voce vai usar

### `pdfplumber.open()`

Abre o PDF para leitura. Use com `with` para fechar automaticamente.

### `.pages`

Lista de paginas do documento.

### `.extract_tables()`

Extrai tabelas da pagina como lista de listas (linhas e celulas).

### `pd.DataFrame(dados, columns=cabecalho)`

Converte tabela extraida em DataFrame.

### `.rename(columns={...})`

Padroniza nomes (ex: 'Turma' -> 'turma') para o merge funcionar.

### `melt`

Apos padronizar, converter para longo com nota_projeto.

## Tarefas

1. Extrair tabela de `dados/projeto_7ano.pdf`.
2. Renomear Turma->turma, Aluno->aluno.
3. Aplicar melt com nota_projeto.
4. Exibir resultado.

## Criterios de aceite

- Tabela extraida sem erro.
- Colunas padronizadas.
- Formato longo correto.

## Como executar

```bash
cd 12_pdfplumber_extrair_tabela
python main.py
```

## Referencia no projeto real

`src/leitor_projetos.py`
