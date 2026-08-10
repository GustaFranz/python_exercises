# 74 - DESAFIO - Parse, validacao e relatorio

## Objetivo

Combinar regex, estrutura aninhada/recursao leve e closure num case de qualidade de dados.

## Conteudos cobertos

- Regex (`re`)
- Recursao ou percurso de estrutura aninhada
- Closure / fabrica de validadores
- Relatorio textual

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | QualiData Servicos |
| **Setor** | Qualidade de dados / backoffice |
| **Solicitacao** | Parsear payloads textuais, validar campos e gerar relatorio por cliente. |

## Enunciado

Linhas brutas do staging:
```python
linhas = [
    "cliente=Ana;telefone=11999998888;score=80",
    "cliente=Bruno;telefone=123;score=45",
    "cliente=Carla;telefone=21988887777;score=95",
    "cliente=;telefone=11977776666;score=70",
]
```

Arvore de configuracao:
```python
config = {
    "regras": {
        "telefone": {"min_digitos": 11},
        "score": {"minimo": 50, "maximo": 100},
    }
}
```

Padrao regex: `r"cliente=(.*?);telefone=(.*?);score=(\d+)"`

1) Com regex, extraia `cliente`, `telefone`, `score` de cada linha.
2) Crie fabrica `criar_validador_digitos(minimo)` (closure) para validar telefone.
3) Crie fabrica `criar_validador_faixa(minimo, maximo)` para validar score.
4) Percorra `config` recursivamente para ler limites e montar os validadores.
5) Classifique cada registro: `ok` ou `rejeitado` + motivos (cliente vazio, telefone invalido, score fora da faixa).
6) Gere um relatorio consolidado com:
   - total `ok` e total `rejeitado`
   - lista de aprovados (score >= 50 e telefone valido)

Exemplo de saida:

```
=== Relatorio consolidado ===
Total ok: 2
Total rejeitado: 2
Aprovados: Ana (score 80), Carla (score 95)
Rejeitados:
- Bruno: telefone invalido (3 digitos)
- (vazio): cliente vazio
```

## Como executar

```bash
cd "74_desafio_parse_validacao_relatorio"
python main.py
```
