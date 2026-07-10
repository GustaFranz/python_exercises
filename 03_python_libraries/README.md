# 03 — Python Libraries

Laboratorio de mini-projetos para dominar **bibliotecas e automacao** usadas em projetos reais — especialmente o [automacao-dashboard-boletim-escolar](https://github.com/GustaFranz/automacao-dashboard-boletim-escolar).

**Total:** 28 exercicios (`01` a `28`).

[← Voltar ao README principal](../README.md) · [Fundamentos](../01_python_fundamentals/) · [Intermediario](../02_intermediate_advanced/) · [Materiais PDF](../04_study_materials/)

---

## Objetivo desta area

| Item | Descricao |
|------|-----------|
| **Para quem** | Quem ja domina fundamentos e intermediario, ou esta montando automacao com dados |
| **Nivel** | Bibliotecas reais — pathlib, pandas, streamlit, RPA |
| **O que treina** | Caminhos, leitura de dados, consolidacao, dashboard e pipeline integrado |
| **Cada exercicio** | Pasta `NN_snake_case/` com `README.md`, `main.py` e `dados/` (avaliacoes: `perguntas.md`) |

Cada exercicio de codigo simula uma **demanda real** (tom corporativo), explica os **conceitos dos comandos** antes da tarefa e pede implementacao em `main.py` — sem solucao pronta.

> **Regra de ouro:** responda as avaliacoes (13, 20, 27, 28) antes de abrir `gabarito.md`.

---

## Pre-requisitos recomendados

- Trilhas `01_python_fundamentals` e `02_intermediate_advanced` (ou equivalente)
- Ambiente virtual Python 3.x
- Dependencias: `pip install -r requirements.txt`

---

## Como executar

```bash
git clone https://github.com/GustaFranz/python_exercises.git
cd python_exercises/03_python_libraries
pip install -r requirements.txt
cd 01_pathlib_navegar_pastas
python main.py
```

Para exercicios Streamlit (21–23):

```bash
streamlit run main.py
```

Para o exercicio 02 (script em `src/`):

```bash
cd 02_pathlib_raiz_do_projeto
python src/main.py
```

Para exercicios de **avaliacao** (13, 20, 27, 28): abra `perguntas.md` — nao ha `main.py` na raiz.

---

## Stack treinada

| Biblioteca | Uso |
|------------|-----|
| **pathlib** | Caminhos portaveis, glob, mkdir, write_text |
| **shutil** | Mover arquivos baixados (Downloads → dados/) |
| **pandas** | Leitura, merge, groupby, exportacao |
| **openpyxl** | Leitura de Excel |
| **pdfplumber** | Extracao de tabelas em PDF |
| **streamlit** | Dashboard web |
| **plotly** | Graficos interativos |
| **pyautogui** | Automacao de interface (RPA) |

---

## Indice dos exercicios

<details open>
<summary><strong>Fase 1 — Pathlib, Shutil e leitura (01-13)</strong></summary>

| # | Exercicio | Biblioteca | Tipo |
|---|-----------|------------|------|
| 01 | [Pathlib — Navegar pastas](./01_pathlib_navegar_pastas/) | pathlib | codigo |
| 02 | [Pathlib — Raiz do projeto](./02_pathlib_raiz_do_projeto/) | pathlib | codigo |
| 03 | [Pathlib — Montar caminhos](./03_pathlib_montar_caminhos/) | pathlib | codigo |
| 04 | [Pathlib — Glob com padroes](./04_pathlib_glob_padroes/) | pathlib | codigo |
| 05 | [Pathlib — Verificar existencia](./05_pathlib_verificar_existencia/) | pathlib | codigo |
| 06 | [Pathlib — Criar pastas de saida](./06_pathlib_criar_pastas_saida/) | pathlib | codigo |
| 07 | [Shutil — Mover arquivo](./07_shutil_mover_arquivo/) | shutil | codigo |
| 08 | [Pandas — Ler CSV](./08_pandas_ler_csv/) | pandas | codigo |
| 09 | [Pandas — Concat varios CSVs](./09_pandas_concat_varios_csv/) | pandas | codigo |
| 10 | [Pandas — Melt formato longo](./10_pandas_melt_formato_longo/) | pandas | codigo |
| 11 | [Pandas — Ler Excel](./11_pandas_ler_excel/) | pandas + openpyxl | codigo |
| 12 | [PDFPlumber — Extrair tabela](./12_pdfplumber_extrair_tabela/) | pdfplumber | codigo |
| 13 | [Avaliacao — Leitura de dados](./13_avaliacao_leitura_de_dados/) | revisao fase 1 | perguntas |

</details>

<details open>
<summary><strong>Fase 2 — Consolidacao e indicadores (14-20)</strong></summary>

| # | Exercicio | Biblioteca | Tipo |
|---|-----------|------------|------|
| 14 | [Pandas — Merge duas fontes](./14_pandas_merge_duas_fontes/) | pandas | codigo |
| 15 | [Pandas — Media ponderada](./15_pandas_media_ponderada/) | pandas | codigo |
| 16 | [Pandas — Regra aprovacao](./16_pandas_regra_aprovacao/) | pandas | codigo |
| 17 | [Pandas — Exportar CSV](./17_pandas_exportar_csv/) | pandas | codigo |
| 18 | [Pandas — Groupby indicadores](./18_pandas_groupby_indicadores/) | pandas | codigo |
| 19 | [Pandas — Filtros percentuais](./19_pandas_filtros_percentuais/) | pandas | codigo |
| 20 | [Avaliacao — Consolidacao](./20_avaliacao_consolidacao/) | revisao fase 2 | perguntas |

</details>

<details open>
<summary><strong>Fase 3 — Saida, interface e automacao (21-28)</strong></summary>

| # | Exercicio | Biblioteca | Tipo |
|---|-----------|------------|------|
| 21 | [Streamlit — Metricas](./21_streamlit_metricas/) | streamlit | codigo |
| 22 | [Streamlit — Filtro sidebar](./22_streamlit_filtro_sidebar/) | streamlit | codigo |
| 23 | [Streamlit + Plotly — Grafico](./23_streamlit_plotly_grafico/) | streamlit + plotly | codigo |
| 24 | [Gerar boletim HTML](./24_gerar_boletim_html/) | pandas + html | codigo |
| 25 | [PyAutoGUI — Coleta portal](./25_pyautogui_coleta_portal/) | pyautogui | codigo |
| 26 | [Pipeline integrado](./26_pipeline_main_integrado/) | orquestracao | codigo |
| 27 | [Avaliacao — Projeto completo](./27_avaliacao_projeto_completo/) | revisao final | perguntas |
| 28 | [Avaliacao — Merge triplo e modulos](./28_avaliacao_merge_triplo_e_modulos/) | merge + imports | perguntas |

</details>

---

## Preparacao para o projeto real

| Modulo real (boletim escolar) | Exercicios que preparam |
|-------------------------------|-------------------------|
| `src/leitor_simulados.py` | 01, 02, 04, 08, 09, 10 |
| `src/leitor_provas.py` | 11 |
| `src/leitor_projetos.py` | 12 |
| `src/consolidacao.py` | 14, 15, 16, 17 |
| `src/boletins.py` | 06, 24 |
| `src/automacao_portal.py` | 03, 05, 07, 25 |
| `dashboard.py` | 18, 19, 21, 22, 23 |
| `main.py` (orquestracao) | 26 |

Marque seu progresso em [progresso.md](./progresso.md).

---

## Convencoes

| Onde | Regra |
|------|-------|
| **Pastas** | `NN_snake_case` — numero + nome sem espacos |
| **README** | Demanda, Contexto, Conceitos, Tarefas, Criterios, Como executar |
| **Codigo** | `main.py` com enunciado em comentarios + area vazia para solucao |
| **Dados** | Pasta `dados/` dentro de cada exercicio |
| **Avaliacoes** | `perguntas.md` + `gabarito.md` (separado) |

Detalhes completos: [Convencoes no README principal](../README.md#convencoes).

---

## Ordem de estudo recomendada

1. Faca os exercicios **em ordem numerica**.
2. Complete **01 a 07** antes de avancar no pandas — sao a base de caminhos do boletim.
3. Ao terminar cada fase, responda a **avaliacao** antes de abrir o gabarito.
4. Volte ao [boletim escolar](https://github.com/GustaFranz/automacao-dashboard-boletim-escolar) e releia o modulo correspondente.

---

## Materiais de apoio

Guias em PDF relacionados (pathlib, shutil, pandas): [materiais de estudo](../04_study_materials/).

---

## Transparencia

Todos os dados sao **ficticios**. Nenhum aluno ou instituicao real e representado.

Repositorio de **pratica** — exercicios incompletos e rascunhos sao esperados.
