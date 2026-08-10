# 21 - Introducao a CRUD com lista de dicionarios

## Objetivo

Conhecer CRUD em lista de dicionarios e o mapa dos exercicios 21 a 25.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Cadastro minimo de funcionarios para piloto do sistema interno. |

## Visao do bloco (exercicios 21 a 25)

Topico **CRUD com lista de dicionarios**: simular banco de dados em memoria.

| # | Foco |
|---|------|
| 21 | Introducao + cadastro minimo |
| 22 | Listar e buscar por ID |
| 23 | Atualizar e remover |
| 24 | CRUD com validacao |
| 25 | Menu + relatorio por turma |

## Enunciado

Cadastre 3 funcionarios em uma lista de dicionarios.
Cada funcionario deve ter: id, nome, cargo.
Dados iniciais sugeridos:
- {"id": 1, "nome": "Ana Silva", "cargo": "Analista"}
- {"id": 2, "nome": "Bruno Costa", "cargo": "Suporte"}
- {"id": 3, "nome": "Carla Mendes", "cargo": "Coordenadora"}
Exiba a lista completa formatada (um funcionario por linha).

## Passo a passo

1. Crie uma lista vazia chamada `funcionarios` — ela vai simular a tabela do banco em memoria.
2. Use `funcionarios.append(...)` tres vezes, uma para cada dicionario do enunciado, com as chaves `"id"`, `"nome"` e `"cargo"`.
3. Exiba um cabecalho simples, por exemplo `print("=== Funcionarios cadastrados ===")`.
4. Percorra a lista com `for funcionario in funcionarios:`.
5. Dentro do loop, monte a linha com f-string acessando as chaves do dicionario: `f"{funcionario['id']} | {funcionario['nome']} | {funcionario['cargo']}"`.
6. Ao final, exiba o total de registros usando `len(funcionarios)`.

## Como executar

```bash
cd "21_introducao_crud_lista_dict"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Lista vazia que simula a tabela de funcionarios em memoria.
funcionarios = []

# Create: cada append insere um "registro" (dicionario) na "tabela" (lista).
funcionarios.append({"id": 1, "nome": "Ana Silva", "cargo": "Analista"})
funcionarios.append({"id": 2, "nome": "Bruno Costa", "cargo": "Suporte"})
funcionarios.append({"id": 3, "nome": "Carla Mendes", "cargo": "Coordenadora"})

# Cabecalho para organizar a saida no terminal.
print("=== Funcionarios cadastrados ===")

# Read: percorre a lista e exibe um funcionario por linha.
for funcionario in funcionarios:
    # f-string acessa cada chave do dicionario pelo nome.
    print(f"{funcionario['id']} | {funcionario['nome']} | {funcionario['cargo']}")

# len() informa quantos registros existem na "tabela".
print(f"Total: {len(funcionarios)} funcionarios")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Cadastro minimo de funcionarios em memoria (piloto GestaoPro RH)."""

from dataclasses import dataclass


@dataclass
class Funcionario:
    """Representa um registro de funcionario com tipos explicitos."""

    id: int
    nome: str
    cargo: str


def formatar_linha(funcionario: Funcionario) -> str:
    """Monta a linha de exibicao de um funcionario."""
    # Acesso por atributo (funcionario.nome) e mais seguro que por chave:
    # um erro de digitacao vira AttributeError claro, nao KeyError generico.
    return f"{funcionario.id} | {funcionario.nome} | {funcionario.cargo}"


def main() -> None:
    # Dados iniciais do piloto; em producao viriam de um banco ou API.
    funcionarios = [
        Funcionario(id=1, nome="Ana Silva", cargo="Analista"),
        Funcionario(id=2, nome="Bruno Costa", cargo="Suporte"),
        Funcionario(id=3, nome="Carla Mendes", cargo="Coordenadora"),
    ]

    print("=== Funcionarios cadastrados ===")
    # Exibe um registro por linha reutilizando a funcao de formatacao.
    for funcionario in funcionarios:
        print(formatar_linha(funcionario))

    print(f"Total: {len(funcionarios)} funcionarios")


# Executa main() apenas quando o arquivo e rodado diretamente,
# permitindo importar as funcoes em testes sem efeitos colaterais.
if __name__ == "__main__":
    main()
```

</details>
