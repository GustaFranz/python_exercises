# 121 - Refatoracao: script longo em funcoes

## Objetivo

Refatorar script monolitico (~70 linhas) em funcoes claras com menu, preservando regras de negocio.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | AgroEscola |
| **Setor** | Educacao / campo |
| **Solicitacao** | Reorganizar controle de estoque do viveiro escolar antes da safra de plantio. |

## Estrutura de arquivos

```
121_refatoracao_script_longo/
├── README.md
├── main.py      # sua versao refatorada
└── legado.py    # script monolitico de referencia (~70 linhas)
```

## Enunciado

- Estude o comportamento do script monolitico em `legado.py` (nao altere a logica de negocio).
- Refatore em `main.py` separando responsabilidades:
  - `carregar_estoque()` — dados iniciais
  - `validar_movimentacao(item, qtd)` — regras antes de entrada/saida
  - `calcular_estoque_atual(estoque, movimentos)` — aplica entradas e saidas
  - `exibir_relatorio(estoque, resumo)` — saida formatada
- Inclua `main()` com menu textual (consultar, movimentar, relatorio, sair).
- Preserve regras: saida bloqueada se estoque insuficiente; alerta para estoque baixo (< 10).

## Como executar

```bash
cd "121_refatoracao_script_longo"
python legado.py    # referencia do comportamento
python main.py      # sua versao refatorada
```
