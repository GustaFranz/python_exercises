# Avaliacao - Projeto completo (Fase 3) - Gabarito

> Confira somente apos responder perguntas.md

## Pergunta 1

1) executar_automacao() baixa CSVs 2) consolidar_notas() le e une fontes 3) salvar_relatorio_final() exporta CSV 4) gerar_boletins() cria HTMLs. Dashboard roda separado com streamlit run.

---

## Pergunta 2

automacao_portal: RPA download. leitor_simulados/provas/projetos: leitura e melt por formato. consolidacao: merge, media, situacao, export. boletins: HTML por aluno.

---

## Pergunta 3

Porque os CSVs de simulado vem do portal e precisam estar em dados/simulados/ antes dos leitores rodarem. RPA atualiza a entrada do pipeline.

---

## Pergunta 4

move transfere arquivo (some de Downloads). copy duplicaria. move organiza sem deixar copia duplicada na pasta de download.

---

## Pergunta 5

Streamlit oferece interface web interativa (filtros, graficos) sem construir HTML/JS manualmente. Ideal para painel gerencial rapido.

---

## Pergunta 6

Exibe o valor numerico formatado com 1 casa decimal no topo de cada barra, facilitando leitura sem passar mouse.

---

## Pergunta 7

Alunos da turma faltante somem do merge inner. Metricas e graficos ficam incompletos ou vazios para essa turma. Boletins nao gerados para alunos sem dados.

---

## Pergunta 8

1) Criar leitor_trabalhos.py com ler + melt 2) Adicionar pasta dados/trabalhos 3) Incluir merge em consolidacao.py 4) Ajustar formula de media 5) Atualizar boletim/dashboard. Cada leitor independente.

---
