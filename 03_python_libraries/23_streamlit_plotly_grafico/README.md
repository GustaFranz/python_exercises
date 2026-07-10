# 23 - Streamlit + Plotly - Grafico de barras

## Demanda

A Coordenacao quer visualizar media por disciplina em grafico de barras interativo.

## Contexto do problema

Complementa metricas com visualizacao e tabela de recuperacao.

## Conceitos que voce vai usar

### `px.bar()`

Cria grafico de barras com Plotly Express.

### `st.plotly_chart()`

Embute grafico Plotly na pagina Streamlit.

### `use_container_width=True`

Grafico usa largura total disponivel.

### `text_auto='.1f'`

Exibe valor formatado no topo de cada barra.

### `st.dataframe()`

Exibe tabela interativa filtrada.

## Tarefas

1. Grafico media por disciplina.
2. Tabela de alunos em recuperacao.

## Criterios de aceite

- Grafico de barras visivel.
- Tabela mostra apenas recuperacao.

## Como executar

```bash
cd 23_streamlit_plotly_grafico
streamlit run main.py
```

## Referencia no projeto real

`dashboard.py linhas 47-59`
