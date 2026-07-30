# 132 - DESAFIO - Mini sistema de RH

## Objetivo

Case final mais trabalhado: heranca/dataclass, refatoracao, asserts e type hints.

## Conteudos cobertos

- Heranca e/ou dataclass
- Refatoracao em funcoes/modulos
- Testes com `assert` em arquivo separado
- Type hints basicos
- Relatorio de folha simplificado

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | PeopleFirst RH Tech |
| **Setor** | Recursos humanos / sistemas internos |
| **Solicitacao** | Mini modulo de colaboradores com calculo de pagamento, tipagem e suite de testes. |

## Estrutura obrigatoria

```
132_desafio_mini_sistema_rh/
├── main.py
├── models.py
├── calculos.py
├── testes.py
└── README.md
```

## Enunciado

Checklist:

1) Em `models.py` (type hints + docstring):
   - dataclass ou classes `Colaborador` (nome, cargo, salario_base)
   - `Gerente(Colaborador)` com bonus fixo (ex.: +15%)
   - `Vendedor(Colaborador)` com comissao (ex.: +10% sobre salario_base * meta_atingida)
   - metodo `pagamento() -> float` polimorfico
2) Em `calculos.py`:
   - `folha_total(colaboradores: list) -> float`
   - `resumo_por_cargo(colaboradores: list) -> dict[str, float]`
   - `filtrar_acima_de(colaboradores, limite: float) -> list`
3) Em `testes.py`:
   - asserts para pagamento de Gerente e Vendedor
   - assert de folha_total
   - caso de borda: lista vazia -> folha 0
4) Em `main.py`:
   - monte 3 colaboradores
   - imprima pagamento individual e resumo por cargo
   - opcional: chame/lembre de rodar `python testes.py`
5) Codigo limpo: nomes claros, funcoes curtas (refatoracao consciente).

Nao e um ERP completo: foque no nucleo tipado + testes + polimorfismo.

## Como executar

```bash
cd "132_desafio_mini_sistema_rh"
python testes.py
python main.py
```
