# Progresso pessoal

Marque com `[x]` conforme for concluindo.

## Fase 1 — Pathlib, Shutil e leitura

- [ ] 01_pathlib_navegar_pastas
- [ ] 02_pathlib_raiz_do_projeto
- [ ] 03_pathlib_montar_caminhos
- [ ] 04_pathlib_glob_padroes
- [ ] 05_pathlib_verificar_existencia
- [ ] 06_pathlib_criar_pastas_saida
- [ ] 07_shutil_mover_arquivo
- [ ] 08_pandas_ler_csv
- [ ] 09_pandas_concat_varios_csv
- [ ] 10_pandas_melt_formato_longo
- [ ] 11_pandas_ler_excel
- [ ] 12_pdfplumber_extrair_tabela
- [ ] 13_avaliacao_leitura_de_dados

## Fase 2 — Consolidacao

- [ ] 14_pandas_merge_duas_fontes
- [ ] 15_pandas_media_ponderada
- [ ] 16_pandas_regra_aprovacao
- [ ] 17_pandas_exportar_csv
- [ ] 18_pandas_groupby_indicadores
- [ ] 19_pandas_filtros_percentuais
- [ ] 20_avaliacao_consolidacao

## Fase 3 — Saida e automacao

- [ ] 21_streamlit_metricas
- [ ] 22_streamlit_filtro_sidebar
- [ ] 23_streamlit_plotly_grafico
- [ ] 24_gerar_boletim_html
- [ ] 25_pyautogui_coleta_portal
- [ ] 26_pipeline_main_integrado
- [ ] 27_avaliacao_projeto_completo
- [ ] 28_avaliacao_merge_triplo_e_modulos

## Revisao no boletim real

Apos cada fase, reler no projeto principal:

- Exercicios 01-07: `src/automacao_portal.py`, `src/leitor_simulados.py`, `src/consolidacao.py`, `src/boletins.py`
- Fase 1 (pandas): `src/leitor_simulados.py`, `leitor_provas.py`, `leitor_projetos.py`
- Fase 2: `src/consolidacao.py`, `dashboard.py` (parte pandas)
- Fase 3: `dashboard.py`, `src/boletins.py`, `src/automacao_portal.py`, `main.py`

### Pos-exercicio 28 (merge triplo e imports)

1. `src/leitor_simulados.py`, `src/leitor_provas.py`, `src/leitor_projetos.py`
2. `src/consolidacao.py` (merge triplo completo)
3. `main.py` (imports e ordem de execucao)
4. `src/boletins.py` (import de consolidar_notas)
