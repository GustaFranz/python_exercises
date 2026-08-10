# 34 - JSON: append em arquivo

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

## Passo a passo

1. Importe `json` e crie a constante `CAMINHO = "livros.json"`.
2. Defina `def carregar_livros(caminho):` que abre o arquivo com `with open(caminho, encoding="utf-8")` e retorna `json.load(arquivo)`; dentro de `try/except FileNotFoundError`, retorne `[]` quando o arquivo nao existir (primeiro uso).
3. Defina `def salvar_livros(caminho, livros):` que grava com `json.dump(livros, arquivo, indent=2, ensure_ascii=False)` em modo `"w"`.
4. Defina `def adicionar_livro(caminho, livro):` seguindo o padrao read-modify-write:
   - `livros = carregar_livros(caminho)` (read);
   - `livros.append(livro)` (modify);
   - `salvar_livros(caminho, livros)` (write).
5. No fluxo principal, chame `adicionar_livro` duas vezes com dicts `{"titulo": ..., "autor": ...}` (ex.: "Dom Casmurro" de Machado de Assis e "Vidas Secas" de Graciliano Ramos).
6. Ao final, carregue o acervo com `carregar_livros(CAMINHO)` e exiba cada livro no formato `titulo — autor`.

## Como executar

```bash
cd "34_json_append_arquivo"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import json

CAMINHO = "livros.json"


def carregar_livros(caminho):
    # Read: devolve a lista existente ou [] no primeiro uso.
    try:
        with open(caminho, encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        # Arquivo ainda nao existe: acervo comeca vazio.
        return []


def salvar_livros(caminho, livros):
    # Write: regrava o arquivo inteiro com a lista atualizada.
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=2, ensure_ascii=False)


def adicionar_livro(caminho, livro):
    # Padrao read-modify-write: carregar -> alterar -> gravar.
    # JSON nao suporta append direto; e preciso reescrever a lista.
    livros = carregar_livros(caminho)
    livros.append(livro)
    salvar_livros(caminho, livros)
    print(f"Livro adicionado: {livro['titulo']}")


# Adiciona 2 livros ao acervo (cada chamada persiste no disco).
adicionar_livro(CAMINHO, {"titulo": "Dom Casmurro", "autor": "Machado de Assis"})
adicionar_livro(CAMINHO, {"titulo": "Vidas Secas", "autor": "Graciliano Ramos"})

# Recarrega do disco para provar que a gravacao funcionou.
print("=== Acervo final ===")
for livro in carregar_livros(CAMINHO):
    print(f"{livro['titulo']} — {livro['autor']}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Acervo de livros em JSON com insercao sem perda de registros."""

import json
from pathlib import Path

CAMINHO = Path(__file__).parent / "livros.json"

Livro = dict[str, str]


def carregar_livros(caminho: Path) -> list[Livro]:
    """Retorna o acervo atual, ou lista vazia se o arquivo nao existe."""
    # Guard clause: sem arquivo, o acervo comeca vazio.
    if not caminho.exists():
        return []
    return json.loads(caminho.read_text(encoding="utf-8"))


def salvar_livros(caminho: Path, livros: list[Livro]) -> None:
    """Regrava o arquivo com o acervo completo."""
    conteudo = json.dumps(livros, indent=2, ensure_ascii=False)
    caminho.write_text(conteudo, encoding="utf-8")


def adicionar_livro(caminho: Path, livro: Livro) -> None:
    """Insere um livro preservando os anteriores (read-modify-write)."""
    livros = carregar_livros(caminho)  # read
    livros.append(livro)               # modify
    salvar_livros(caminho, livros)     # write
    print(f"Livro adicionado: {livro['titulo']}")


def main() -> None:
    # Comeca do zero a cada execucao para a saida ser previsivel.
    CAMINHO.unlink(missing_ok=True)

    adicionar_livro(CAMINHO, {"titulo": "Dom Casmurro", "autor": "Machado de Assis"})
    adicionar_livro(CAMINHO, {"titulo": "Vidas Secas", "autor": "Graciliano Ramos"})

    # Recarrega do disco: confirma que a persistencia esta correta.
    print("=== Acervo final ===")
    for livro in carregar_livros(CAMINHO):
        print(f"{livro['titulo']} — {livro['autor']}")


if __name__ == "__main__":
    main()
```

</details>
