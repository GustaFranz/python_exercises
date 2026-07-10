# 33 - JSON: append em arquivo

## Objetivo

Adicionar registro a lista existente em JSON.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Biblioteca Digital Nexus |
| **Setor** | Cultura / acervo |
| **Solicitacao** | Incluir novo livro no acervo JSON sem perder registros anteriores. |

## Enunciado

Arquivo livros.json pode comecar vazio [] ou com registros.
Funcao adicionar_livro(caminho, livro_dict):
- 1) Carrega lista existente (ou [] se arquivo nao existe)
- 2) Append do novo livro
- 3) Salva lista atualizada
Teste adicionando 2 livros: titulo e autor.
Exiba acervo final.

## Como executar

```bash
cd "33_json_append_arquivo"
python main.py
```
