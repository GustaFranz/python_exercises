# 04 - Pathlib - Glob com padroes de arquivo

## Demanda

O sistema precisa encontrar automaticamente todos os arquivos de notas em cada fonte, sem listar nomes manualmente. Cada tipo de dado tem um padrao de nome diferente.

## Contexto do problema

No projeto real, `ler_simulados()` busca `simulado_*.csv`, `ler_provas()` busca `provas_*.xlsx` e `ler_projetos()` busca `projeto_*.pdf`. Aqui usamos `.csv` em todas as pastas para focar no pathlib (no projeto real as extensoes variam).

## Conceitos que voce vai usar

### `.glob("padrao")`

Busca arquivos que combinam com o padrao. `*` significa qualquer texto.

### `list(...)`

Converte o iterador do glob em lista para contar e percorrer.

### `.name`

Retorna so o nome do arquivo, sem o caminho da pasta.

### Padroes do projeto real

| Pasta | Padrao real | Padrao neste exercicio |
|-------|-------------|------------------------|
| dados/simulados | `simulado_*.csv` | `simulado_*.csv` |
| dados/provas | `provas_*.xlsx` | `provas_*.csv` |
| dados/projetos | `projeto_*.pdf` | `projeto_*.csv` |

## Tarefas

1. Defina `pasta_projeto` e as tres pastas de dados.
2. Use `glob` para listar arquivos em cada pasta com o padrao correto.
3. Imprima a quantidade e o `.name` de cada arquivo encontrado.
4. Se alguma lista ficar vazia, imprima aviso (preparacao para `FileNotFoundError` do projeto real).

## Criterios de aceite

- Encontra 2 simulados, 1 prova e 1 projeto (arquivos em `dados/`).
- Usa tres padroes glob diferentes.
- Nao lista arquivos de outras pastas por engano.

## Como executar

```bash
cd 04_pathlib_glob_padroes
python main.py
```

## Referencia no projeto real

`src/leitor_simulados.py` (linha 9), `src/leitor_provas.py` (linha 11), `src/leitor_projetos.py` (linha 29)
