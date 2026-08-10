# 120 - Refatoracao: separar camadas

## Objetivo

Separar leitura de dados, regra de negocio e apresentacao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Organizar script de cobranca de mensalidades em camadas claras. |

## Enunciado

Cada registro e um dict: `{"aluno": str, "valor": float, "pago": bool}`.

Implemente 3 funcoes separadas:

1) `carregar_dados() -> list[dict]` — retorna lista fixa de exemplo (I/O simulada). Exemplo:
   ```python
   [
       {"aluno": "Ana", "valor": 350.0, "pago": True},
       {"aluno": "Bruno", "valor": 350.0, "pago": False},
       {"aluno": "Carla", "valor": 400.0, "pago": False},
   ]
   ```
2) `calcular_pendentes(dados) -> list[dict]` — retorna apenas registros com `pago == False` (regra de negocio; sem `print`).
3) `exibir_relatorio(pendentes) -> None` — imprime relatorio formatado (apenas apresentacao).

Crie `main()` que orquestra as tres camadas na ordem: carregar → calcular → exibir.

Regras:
- `carregar_dados` nao calcula.
- `calcular_pendentes` nao imprime.
- Cada funcao tem uma unica responsabilidade.

Exemplo de saida:

```
Mensalidades pendentes:
- Bruno: R$ 350.00
- Carla: R$ 400.00
Total pendente: R$ 750.00
```

## Como executar

```bash
cd "120_refatoracao_separar_camadas"
python main.py
```
