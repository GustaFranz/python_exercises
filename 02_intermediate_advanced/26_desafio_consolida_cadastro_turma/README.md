# 26 - DESAFIO - Consolida cadastro de turma

## Objetivo

Integrar list/dict comprehension, set, zip e CRUD em memoria num case de entrevista.

## Conteudos cobertos

- List comprehension e dict comprehension
- Conjuntos (`set`)
- `zip` entre estruturas
- CRUD com lista de dicionarios

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / operacoes academicas |
| **Solicitacao** | Prototipo para consolidar matriculas do dia, detectar duplicatas e gerar painel da turma. |

## Enunciado

Voce recebeu tres listas paralelas do staging (mesmo indice = mesmo aluno):

```python
ids = [1, 2, 3, 2, 4]
nomes = ["Ana", "Bruno", "Carla", "Bruno Dup", "Diego"]
notas = [7.5, 5.0, 8.0, 6.0, 4.5]
```

Checklist do case:

1) Use `zip` para montar registros `{id, nome, nota}`.
2) Implemente CRUD minimo em memoria:
   - `adicionar_aluno` (rejeite id duplicado)
   - `listar_alunos`
   - `buscar_por_id`
3) Ao importar o lote, ignore duplicatas e registre ids rejeitados em um `set`.
4) Com list/dict comprehension:
   - lista de nomes aprovados (nota >= 6)
   - `medias` nao precisa; monte `painel = {id: nota}` dos cadastrados
5) Relatorio final: total cadastrado, ids rejeitados (ordenados), aprovados, taxa de aprovacao %.

## Como executar

```bash
cd "26_desafio_consolida_cadastro_turma"
python main.py
```
