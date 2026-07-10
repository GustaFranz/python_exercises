# Avaliacao - Merge triplo e modulos src - Gabarito

> Confira somente apos responder perguntas.md

---

## Parte A — Merge triplo

### Pergunta 1

O pandas `merge` aceita no maximo **duas** tabelas por chamada. O merge triplo e dois merges encadeados: primeiro cruza simulados com provas, depois o resultado com projetos. O padrao e legivel e igual ao exercicio 14 (merge duplo), so que com uma etapa a mais.

---

### Pergunta 2

Chaves: `turma`, `aluno`, `disciplina`. So `aluno` nao basta porque o mesmo aluno tem **varias disciplinas** (varias linhas) e pode existir em turmas diferentes. As tres colunas identificam **uma nota unica** na matriz turma+aluno+disciplina.

---

### Pergunta 3

O melt converte formato **largo** (disciplinas em colunas) para **longo** (uma linha por disciplina). Assim todas as fontes ficam com a mesma estrutura antes do merge: `turma`, `aluno`, `disciplina`, `nota_*`. Sem melt, as chaves nao batem.

---

### Pergunta 4

Apos o 1o merge: `turma`, `aluno`, `disciplina`, `nota_simulado`, `nota_prova`.

Apos o 2o merge: acrescenta `nota_projeto`.

Colunas auxiliares como `nota_projeto_convertida`, `media` e `situacao` so aparecem **depois**, na etapa de calculo.

---

### Pergunta 5

A linha de Ciencias **some** do resultado. O inner join so mantem combinacoes presentes **nas duas** tabelas. Sem Ciencias em simulados, nao ha par simulado+prova para Ciencias — a linha e descartada.

---

### Pergunta 6

Bruno **desaparece** da tabela final. O terceiro merge e inner: exige registro em simulados, provas **e** projetos para a mesma chave. Sem projeto, a linha nao passa.

---

### Pergunta 7

Os leitores preservam o valor **bruto** do arquivo (proporcao 0-1 no simulado). A regra de negocio (peso 10 na formula) fica centralizada em `consolidacao.py`. Se a formula mudar, altera-se um unico lugar, nao tres leitores.

---

### Pergunta 8

Ordem apos os merges:

1. `astype(float)` em `nota_simulado`, `nota_prova`, `nota_projeto`
2. `nota_projeto_convertida = nota_projeto * 2`
3. `media = (sim*10 + prov*10 + proj_conv*5) / 25`
4. `media.round(1)`
5. `situacao` via `apply` (Aprovado se media >= 6, senao Recuperacao)
6. `return tabela`

---

## Parte B — Imports e modulos src

### Pergunta 9

`src` e o **pacote Python** (pasta `src/` na raiz do projeto). O `main.py` fica **fora** de `src/`, entao importa com `from src.consolidacao import ...`. Sem o prefixo `src.`, o Python nao encontraria o modulo ao rodar da raiz.

---

### Pergunta 10

O projeto roda com a **raiz** como diretorio de trabalho (`python main.py`). Imports absolutos com `src.` funcionam igual de `main.py` ou de qualquer arquivo, evitando imports relativos confusos (`from .leitor_simulados import ...`) e erros ao executar arquivos de formas diferentes.

---

### Pergunta 11

`python main.py` executa o **pipeline completo** (automacao, consolidacao, export, boletins). `python src/consolidacao.py` executa **so** o bloco `if __name__ == "__main__"` da consolidacao (consolidar + salvar CSV de teste), sem RPA nem boletins. Util para testar um modulo isolado.

---

### Pergunta 12

Cada modulo e **autonomo**: `gerar_boletins()` busca os dados que precisa sem depender de variaveis globais ou do que `main()` fez antes. Isso permite rodar `python src/boletins.py` sozinho. O custo e consolidar duas vezes no fluxo completo — trade-off de **baixo acoplamento** vs eficiencia.

---

### Pergunta 13

**Leitura** (`ler_*`): I/O — glob, read_csv, read_excel, pdfplumber. **Transformacao** (`transformar_*`): padronizacao para formato longo. Separar permite testar a leitura sem transformar, reutilizar a transformacao em testes e manter cada funcao com uma responsabilidade (alinhado ao exercicio modular do boletim).

---

### Pergunta 14

Garante que o codigo de teste (`ler_simulados()`, `print(head())`, etc.) **so roda** quando o arquivo e executado diretamente. Quando outro modulo faz `from src.leitor_simulados import ler_simulados`, esse bloco **nao** executa — evita efeitos colaterais na importacao.

---

### Pergunta 15

Fluxo de dados para Ana Silva, Matematica:

1. `dados/simulados/simulado_*.csv` — arquivo no disco
2. `ler_simulados()` — le e concatena CSVs
3. `transformar_simulados_para_longo()` — gera linha com `nota_simulado`
4. `ler_provas()` + `transformar_provas_para_longo()` — `nota_prova`
5. `ler_projetos()` + `transformar_projetos_para_longo()` — `nota_projeto`
6. `consolidar_notas()` — merges, calcula `media` e `situacao`
7. `salvar_relatorio_final()` — grava CSV (opcional no fluxo do boletim)
8. `gerar_boletins()` — chama `consolidar_notas()` de novo, `groupby` turma+aluno, monta HTML com a linha de Matematica

A linha HTML exibe disciplina, tres notas, media e situacao daquela combinacao.

---
