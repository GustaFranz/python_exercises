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

## Como executar

```bash
cd "68_recursao_estrutura_aninhada"
python main.py
```
