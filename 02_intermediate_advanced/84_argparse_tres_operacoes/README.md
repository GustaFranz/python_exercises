# 84 - Argparse: ferramenta com 3 operacoes

## Objetivo

Integrar argparse com tres subcomandos em ferramenta unica.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LimpezaDados Servicos |
| **Setor** | Tratamento de dados |
| **Solicitacao** | CLI interna para contar, filtrar e exportar linhas de arquivo texto. |

## Enunciado

Crie `dados.txt` com 5 linhas de exemplo no inicio do script.

Configure 3 subcomandos:

**`contar --arquivo`**
- Exibe total de linhas do arquivo

**`filtrar --arquivo --texto`**
- Exibe linhas que contem o texto informado

**`exportar --arquivo --saida`**
- Copia arquivo para destino com `with open`

Implemente cada operacao em funcao separada: `contar_linhas`, `filtrar_linhas`, `exportar_arquivo`.

No `main`, roteie com `if args.comando == "contar": ...`

Exemplo de execucao:

```bash
python main.py contar --arquivo dados.txt
python main.py filtrar --arquivo dados.txt --texto erro
python main.py exportar --arquivo dados.txt --saida copia.txt
```

## Como executar

```bash
cd "84_argparse_tres_operacoes"
python main.py contar --arquivo dados.txt
```
