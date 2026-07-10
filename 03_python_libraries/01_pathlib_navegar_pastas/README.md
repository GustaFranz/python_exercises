# 01 - Pathlib - Navegar pastas do projeto

## Demanda

A TI do Colegio Caminhos do Futuro contratou voce para criar um script que localize automaticamente todos os arquivos de notas dentro da estrutura de pastas do sistema, sem depender de caminhos digitados manualmente.

## Contexto do problema

Antes de ler qualquer nota, o sistema precisa saber onde os arquivos estao. Hoje a equipe abre pastas manualmente; o objetivo e automatizar essa descoberta.

## Conceitos que voce vai usar

### `pathlib.Path`

Classe moderna para trabalhar com caminhos de arquivo. Substitui strings frageis como 'C:\\pasta\\arquivo.csv'.

### `__file__`

Variavel que guarda o caminho do arquivo Python em execucao. Permite achar a pasta do projeto automaticamente.

### `.resolve()`

Transforma o caminho em caminho absoluto (completo), eliminando atalhos e '..'.

### `.parent`

Sobe um nivel na arvore de pastas. `.parent.parent` sobe dois niveis.

### `Operador /`

Com Path, `/` junta pastas de forma segura: `pasta / 'dados' / 'arquivo.csv'`.

### `.exists()`

Retorna True se o caminho existe no disco.

### `.glob('*.csv')`

Busca arquivos que combinam com o padrao. Retorna um iterador de Paths.

## Tarefas

1. Defina `pasta_projeto` usando `Path(__file__).resolve().parent`.
2. Defina `pasta_dados` como subpasta `dados` dentro do exercicio.
3. Liste todos os arquivos `.csv` com `.glob()`.
4. Exiba o caminho completo de cada arquivo encontrado.

## Criterios de aceite

- O script imprime pelo menos 1 arquivo CSV.
- Os caminhos exibidos sao absolutos ou relativos consistentes.
- Nao ha caminho fixo tipo `C:/Users/...` no codigo.

## Como executar

```bash
cd 01_pathlib_navegar_pastas
python main.py
```

## Trilha Pathlib e Shutil (exercicios 01 a 07)

Estes sete exercicios cobrem tudo que o projeto de boletim usa de `pathlib` e `shutil`:

| Exercicio | Tema | Modulo real |
|-----------|------|-------------|
| 01 | glob basico | leitor_simulados |
| 02 | parent.parent (src/) | todos os modulos em src/ |
| 03 | montar caminhos com / | automacao_portal, consolidacao |
| 04 | glob com padroes | leitores de simulado, prova, projeto |
| 05 | exists() antes de agir | automacao_portal |
| 06 | mkdir e write_text | consolidacao, boletins |
| 07 | shutil.move | automacao_portal |

## Referencia no projeto real

`src/leitor_simulados.py (linhas 4-9) no projeto automacao-dashboard-boletim-escolar`
