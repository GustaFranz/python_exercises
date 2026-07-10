# 24 - Gerar boletim HTML por aluno

## Demanda

Cada familia deve receber boletim individual em HTML para consulta offline.

## Contexto do problema

Saida individual do sistema de boletins.

## Conceitos que voce vai usar

### `groupby(['turma','aluno'])`

Separa dados por aluno para gerar um arquivo cada.

### `.iterrows()`

Percorre linhas do DataFrame do aluno.

### `f-string multilinha`

Monta HTML com dados dinamicos.

### `re.sub()`

Remove caracteres invalidos do nome do arquivo.

### `.write_text(encoding='utf-8')`

Salva arquivo HTML no disco.

## Tarefas

1. Gere 1 HTML por aluno em saidas/boletins/.
2. Tabela com disciplina, notas e situacao.

## Criterios de aceite

- Um arquivo por aluno.
- HTML abre no navegador.
- Nomes de arquivo sem espacos especiais.

## Como executar

```bash
cd 24_gerar_boletim_html
python main.py
```

## Referencia no projeto real

`src/boletins.py`
