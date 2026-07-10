# 03 - Pathlib - Montar caminhos do pipeline

## Demanda

O sistema de boletim organiza arquivos em pastas fixas: simulados, provas, relatorios e boletins. Voce deve montar todos esses caminhos a partir da raiz do projeto, sem digitar caminhos completos.

## Contexto do problema

Cada modulo do projeto real define variaveis de pasta no topo do arquivo. Isso centraliza a estrutura e evita erros de digitacao.

## Conceitos que voce vai usar

### Operador `/` com Path

Junta partes do caminho de forma segura entre Windows e Linux.

### Caminhos do projeto real

- `dados/simulados` — CSVs baixados do portal
- `dados/provas` — planilhas de provas
- `dados/projetos` — PDFs de projetos
- `saidas/relatorios` — CSV consolidado
- `saidas/boletins` — HTML por aluno
- `saidas/prints` — capturas da automacao

### `Path.home()`

Retorna a pasta do usuario (ex: `C:/Users/nome`). No projeto real: `Path.home() / "Downloads"`.

### `.as_uri()`

Converte o caminho para URL `file:///...`. No projeto real, abre o portal: `webbrowser.open(portal_login.as_uri())`.

## Tarefas

1. Defina `pasta_projeto` com `Path(__file__).resolve().parent`.
2. Crie variaveis para as 6 pastas listadas acima usando `/`.
3. Crie `pasta_downloads = Path.home() / "Downloads"`.
4. Imprima cada caminho em uma linha, com rotulo claro (ex: `Simulados: ...`).
5. (Extra) Defina `portal_login = pasta_projeto / "portal_simulado" / "login.html"` e imprima `portal_login.as_uri()`.

## Criterios de aceite

- Todas as 7 variaveis de caminho definidas.
- Nenhuma string com barra invertida manual (`\\`).
- Saida legivel com nome da pasta e caminho completo.

## Como executar

```bash
cd 03_pathlib_montar_caminhos
python main.py
```

## Referencia no projeto real

`src/automacao_portal.py` (linhas 13-17), `src/consolidacao.py` (linha 7), `src/boletins.py` (linha 8)
