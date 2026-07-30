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

Arvore de pastas de configuracao (percorra recursivamente as chaves folha):
```python
config = {
    "regras": {
        "telefone": {"min_digitos": 11},
        "score": {"minimo": 50, "maximo": 100},
    }
}
```

Checklist:

1) Com regex, extraia `cliente`, `telefone`, `score` de cada linha.
2) Crie fabrica `criar_validador_digitos(minimo)` (closure) para telefone.
3) Crie fabrica `criar_validador_faixa(minimo, maximo)` para score.
4) Percorra `config` (recursivo ou aninhado) para ler os limites e montar os validadores.
5) Classifique cada registro: `ok` ou `rejeitado` + motivos.
6) Use closure `criar_relatorio(cliente_nome)` OU gere um unico relatorio consolidado
   com totais ok/rejeitado e lista de aprovados (score >= 50 e telefone valido).

## Como executar

```bash
cd "74_desafio_parse_validacao_relatorio"
python main.py
```
