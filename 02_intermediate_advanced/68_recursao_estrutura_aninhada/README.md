# 68 - Recursao: estrutura aninhada

## Objetivo

Percorrer dict aninhado simulando pastas e arquivos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / backup |
| **Solicitacao** | Listar todos os arquivos em estrutura de pastas para auditoria. |

## Enunciado

Estrutura simulada de pastas:
```python
arvore = {
    "documentos": {"relatorio.txt": None, "notas": {"prova1.pdf": None}},
    "imagens": {"logo.png": None},
}
```

Regra: `None` = arquivo; `dict` = pasta.

Implemente:

```python
def listar_arquivos(no: dict, caminho: str = "") -> None:
    # se valor e dict: percorra recursivamente
    # se valor e None: imprima caminho completo do arquivo
```

No `main`, chame `listar_arquivos(arvore)` e exiba todos os caminhos.

Exemplo de saida:

```
documentos/relatorio.txt
documentos/notas/prova1.pdf
imagens/logo.png
```

## Passo a passo

1. Crie o dict `arvore` exatamente como no enunciado.
2. Defina `listar_arquivos(no: dict, caminho: str = "") -> None` — `caminho` acumula o trajeto ja percorrido e comeca vazio na raiz.
3. Dentro da funcao, percorra `no.items()` com `for chave, valor in ...` (cada chave e um nome de pasta ou de arquivo).
4. Monte o caminho atual tratando a raiz: `caminho_atual = f"{caminho}/{chave}" if caminho else chave` (na raiz nao ha `/` inicial).
5. Verifique o tipo do valor com `isinstance(valor, dict)`:
   - se for `dict`, e uma pasta: chame `listar_arquivos(valor, caminho_atual)` recursivamente para entrar nela;
   - se for `None`, e um arquivo: imprima `caminho_atual`.
6. No corpo principal, chame `listar_arquivos(arvore)` — a saida deve listar os 3 arquivos com seus caminhos completos.

## Como executar

```bash
cd "68_recursao_estrutura_aninhada"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Estrutura simulada: dict = pasta, None = arquivo
arvore = {
    "documentos": {"relatorio.txt": None, "notas": {"prova1.pdf": None}},
    "imagens": {"logo.png": None},
}


def listar_arquivos(no, caminho=""):
    # Percorre cada entrada do nivel atual (pasta ou arquivo)
    for chave, valor in no.items():
        # Na raiz o caminho e vazio, entao usamos so a chave;
        # nos niveis internos concatenamos com "/"
        caminho_atual = f"{caminho}/{chave}" if caminho else chave

        if isinstance(valor, dict):
            # E uma pasta: entra nela recursivamente carregando o caminho acumulado
            listar_arquivos(valor, caminho_atual)
        else:
            # E um arquivo (None): imprime o caminho completo montado ate aqui
            print(caminho_atual)


# Dispara a listagem a partir da raiz da arvore
listar_arquivos(arvore)
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Lista arquivos de uma arvore de pastas simulada (dict aninhado).

O mesmo raciocinio recursivo vale para estruturas reais: em disco,
um dev usaria pathlib (Path.rglob("*")) ou os.walk, que ja fazem
essa recursao por baixo dos panos.
"""

from typing import Iterator

# Alias documenta o formato: chave = nome, valor = subarvore (pasta) ou None (arquivo)
Arvore = dict[str, "Arvore | None"]


def iterar_arquivos(no: Arvore, caminho: str = "") -> Iterator[str]:
    """Gera o caminho completo de cada arquivo da arvore.

    Funcao geradora: quem chama decide o que fazer com os caminhos
    (imprimir, gravar, contar), separando o percurso da apresentacao.
    """
    for chave, valor in no.items():
        # Monta o caminho acumulado, sem barra inicial na raiz
        caminho_atual = f"{caminho}/{chave}" if caminho else chave

        if isinstance(valor, dict):
            # yield from delega a geracao para a chamada recursiva:
            # cada arquivo achado la dentro "sobe" direto para quem consome
            yield from iterar_arquivos(valor, caminho_atual)
        else:
            # Folha da arvore (None) = arquivo: entrega o caminho pronto
            yield caminho_atual


def main() -> None:
    arvore: Arvore = {
        "documentos": {"relatorio.txt": None, "notas": {"prova1.pdf": None}},
        "imagens": {"logo.png": None},
    }

    # O percurso gera os caminhos; a apresentacao (print) fica no main
    for caminho in iterar_arquivos(arvore):
        print(caminho)


if __name__ == "__main__":
    main()
```

</details>
