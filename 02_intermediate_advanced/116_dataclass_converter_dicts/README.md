# 116 - Dataclass: converter dicts com validacao

## Objetivo

Converter dados brutos em objetos tipados, rejeitando linhas invalidas e reportando resultado.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LimpezaDados Servicos |
| **Setor** | Tratamento de dados |
| **Solicitacao** | Normalizar JSON de funcionarios importado, ignorando registros incompletos com relatorio. |

## Enunciado

- Crie `@dataclass Funcionario` com `nome`, `cargo`, `salario` e metodo `resumo()`.
- Implemente `converter(dados: list[dict])` retornando tupla `(convertidos, rejeitados)`.
- Linha invalida: falta campo obrigatorio ou `salario` nao numerico/negativo.
- Metodo `resumo()` retorna string curta (ex.: `"Ana — Analista — R$ 3500.00"`).
- Exiba quantidade convertida vs rejeitada e resumo de cada funcionario valido.

## Como executar

```bash
cd "116_dataclass_converter_dicts"
python main.py
```
