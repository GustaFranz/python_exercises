# Avaliacao - Leitura de dados (Fase 1) - Gabarito

> Confira somente apos responder perguntas.md

## Pergunta 1

`__file__` e o caminho do script atual. `.resolve()` torna absoluto. `.parent` sobe para a pasta do script; `.parent.parent` sobe mais um nivel quando o script esta em `src/` e precisa acessar `dados/` na raiz do projeto. Isso torna o codigo portavel entre computadores, diferente de caminho fixo que quebra em outra maquina.

---

## Pergunta 2

`concat` empilha tabelas. `ignore_index=True` recria indice 0..n-1. Sem isso, indices repetidos podem confundir operacoes futuras e dificultar rastreio de linhas.

---

## Pergunta 3

Largo: disciplinas sao colunas. Longo: cada linha e uma disciplina. Merge precisa que disciplina seja valor em coluna, nao nome de coluna diferente em cada arquivo.

---

## Pergunta 4

Pandas lanca erro (ValueError) indicando que a aba nao existe, ou pode ler aba errada se usar indice numerico sem conferir. O script para ou importa dados incorretos.

---

## Pergunta 5

1) `with pdfplumber.open(arquivo) as pdf` 2) percorrer `pdf.pages` 3) `pagina.extract_tables()` 4) pegar cabecalho=linhas[0], dados=linhas[1:] 5) `pd.DataFrame(dados, columns=cabecalho)`.

---

## Pergunta 6

Merge exige nomes identicos nas chaves. 'Turma' e 'turma' sao colunas diferentes para o Pandas. Sem padronizar, o merge falha ou cria colunas duplicadas.

---

## Pergunta 7

Quando ausencia de arquivo invalida todo o fluxo e seguir com DataFrame vazio geraria relatorios falsos. Melhor falhar cedo com mensagem clara para o operador.

---

## Pergunta 8

Erro: tenta merge com tabela em formato largo. `disciplina` nao existe como coluna em `tabela` (esta espalhada em colunas Matematica, Ciencias...). Precisa aplicar `melt` antes do merge.

---
