# 109 - Heranca: usar super()

## Objetivo

Reutilizar construtor da classe pai com super().__init__.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Cadastrar funcionarios e estagiarios compartilhando dados base de pessoa. |

## Enunciado

Crie as classes:

**`Funcionario`**
- `__init__(self, nome, matricula)` — armazena `nome` e `matricula`
- `__str__(self)` — retorna nome e matricula

**`Estagiario(Funcionario)`**
- `__init__(self, nome, matricula, curso)` — chama `super().__init__(nome, matricula)` e define `self.curso`
- `__str__(self)` — inclui nome, matricula e curso

No `main`:

1) Instancie um estagiario (ex.: `"Lucas"`, matricula `"E2024"`, curso `"Administracao"`).
2) Exiba a instancia com `print()`.

Exemplo de saida:

```
Estagiario: Lucas | Matricula: E2024 | Curso: Administracao
```

## Como executar

```bash
cd "109_heranca_super"
python main.py
```
