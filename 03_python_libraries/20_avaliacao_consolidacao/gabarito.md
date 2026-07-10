# Avaliacao - Consolidacao (Fase 2) - Gabarito

> Confira somente apos responder perguntas.md

## Pergunta 1

Inner mantem so linhas presentes em ambas as tabelas. Left manteria todas de simulado e preencheria NaN onde prova nao tem dado. O boletim usa inner para exigir nota em todas as fontes.

---

## Pergunta 2

CSV e Excel podem ler numeros como texto (object). Calcular com strings gera erro ou resultado incorreto. `astype(float)` garante operacao matematica valida.

---

## Pergunta 3

Simulado vem em escala **0-1** (proporcao). Na formula, `nota_simulado * 10` converte para 0-10. Prova ja esta em 0-10 (peso 10). Projeto vai de 0-5; multiplica por 2 para equivaler a 0-10 (peso 5). Formula: `(sim*10 + prov*10 + proj*2*5) / 25`. Ex: sim=0.95, prov=9.5, proj=5 -> (9.5+95+50)/25 = 6.18, arredondado 6.2.

---

## Pergunta 4

Use apply quando a regra nao e expressao simples coluna a coluna. No boletim: `situacao` com condicional Aprovado/Recuperacao. Poderia ser vetorizado, mas apply deixa regra legivel.

---

## Pergunta 5

utf-8-sig adiciona BOM que faz Excel no Windows reconhecer UTF-8 e exibir acentos corretamente ao abrir o CSV com duplo clique.

---

## Pergunta 6

Cria grupos de linhas, um por combinacao turma+aluno. O loop `for (turma, aluno), tabela_aluno in ...` gera um boletim HTML para cada aluno.

---

## Pergunta 7

`dados['situacao'].eq('Recuperacao').mean() * 100` - True vira 1, mean da proporcao, vezes 100 da percentual.

---

## Pergunta 8

Bruno desaparece da tabela final do inner join. So permanecem alunos com registro em ambas as fontes.

---
