# 21 - Streamlit - Metricas em colunas

## Demanda

A Diretoria quer painel web com indicadores numericos da turma, sem instalar software.

## Contexto do problema

Primeiro passo do dashboard: exibir numeros-chave.

## Conceitos que voce vai usar

### `st.set_page_config()`

Configura titulo e layout da pagina.

### `st.title() / st.caption()`

Titulo principal e texto de apoio.

### `st.columns(3)`

Divide linha em 3 colunas para metricas lado a lado.

### `st.metric()`

Exibe indicador com label e valor.

## Tarefas

1. Leia notas.csv.
2. Exiba media geral, total alunos e % recuperacao em 3 colunas.

## Criterios de aceite

- Pagina abre com streamlit run.
- Tres metricas visiveis.

## Como executar

```bash
cd 21_streamlit_metricas
streamlit run main.py
```

## Referencia no projeto real

`dashboard.py linhas 7-40`
