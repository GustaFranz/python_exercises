# 24 - CRUD de alunos com validacao

## Objetivo

Aplicar CRUD com regras de validacao em cadastro escolar.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Colegio Futuro Ativo |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Cadastro de alunos com validacao antes de gravar na base em memoria. |

## Enunciado

Implemente cadastro de alunos: id, nome, turma, nota.
Regras de validacao ao criar:
- id unico (nao repetir)
- nome nao vazio
- nota entre 0 e 10
Funcoes: adicionar_aluno, listar_alunos, buscar_por_id.
Teste: cadastro valido, id duplicado, nota invalida.
Exiba mensagens claras de sucesso ou erro.

## Como executar

```bash
cd "24_crud_alunos_validacao"
python main.py
```
