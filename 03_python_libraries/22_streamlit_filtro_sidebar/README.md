# 22 - Streamlit - Filtro na sidebar

## Demanda

O usuario precisa filtrar indicadores por turma usando menu lateral.

## Contexto do problema

Dashboard do boletim permite escolher turma na sidebar.

## Conceitos que voce vai usar

### `st.sidebar`

Area lateral para controles (filtros, botoes).

### `st.selectbox()`

Lista suspensa de opcoes.

### `.unique()`

Lista valores unicos de turma para o selectbox.

### `dados[dados['turma'] == valor]`

Filtra tabela pela turma selecionada.

## Tarefas

1. Selectbox de turma na sidebar.
2. Metricas atualizam conforme turma.

## Criterios de aceite

- Trocar turma muda metricas.
- Pelo menos 2 turmas no selectbox.

## Como executar

```bash
cd 22_streamlit_filtro_sidebar
streamlit run main.py
```

## Referencia no projeto real

`dashboard.py linhas 14-17`
