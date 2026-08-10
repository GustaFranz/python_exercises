# 15 - Set: auditoria de acesso

## Objetivo

Auditar permissoes com operacoes de conjuntos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | TechSecure Solutions |
| **Setor** | Seguranca da informacao |
| **Solicitacao** | Auditar divergencia entre permissoes autorizadas e permissoes ativas. |

## Enunciado

autorizados = {"leitura", "escrita", "exportar", "admin"}
ativos = {"leitura", "escrita", "imprimir"}
Identifique:
- permissoes_ok (intersecao)
- nao_autorizadas (em ativos mas nao em autorizados)
- revogadas (em autorizados mas nao em ativos)
Exiba relatorio de auditoria.

## Passo a passo

1. Crie os conjuntos `autorizados = {"leitura", "escrita", "exportar", "admin"}` e `ativos = {"leitura", "escrita", "imprimir"}`.
2. Calcule `permissoes_ok` com a intersecao: `autorizados & ativos` (permissoes ativas e devidamente autorizadas).
3. Calcule `nao_autorizadas` com a diferenca: `ativos - autorizados` (ativas sem autorizacao — risco de seguranca).
4. Calcule `revogadas` com a diferenca inversa: `autorizados - ativos` (autorizadas mas nao ativas).
5. Exiba o relatorio de auditoria de seguranca com as tres categorias, cada conjunto com `sorted(...)` para leitura estavel.

## Como executar

```bash
cd "15_set_auditoria_acesso"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Permissoes cadastradas x permissoes em uso no sistema (enunciado)
autorizados = {"leitura", "escrita", "exportar", "admin"}
ativos = {"leitura", "escrita", "imprimir"}

# Intersecao: ativas E autorizadas ao mesmo tempo — situacao regular
permissoes_ok = autorizados & ativos

# Ativas que NAO constam nas autorizadas — alerta de seguranca
nao_autorizadas = ativos - autorizados

# Autorizadas que NAO estao ativas — provavelmente revogadas ou nao usadas
revogadas = autorizados - ativos

# Relatorio de auditoria no formato de seguranca
print("=== AUDITORIA DE PERMISSOES ===")
print("Permissoes ok:   ", sorted(permissoes_ok))
print("Nao autorizadas: ", sorted(nao_autorizadas))
print("Revogadas:       ", sorted(revogadas))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Auditoria de divergencia entre permissoes autorizadas e ativas."""


def auditar_permissoes(autorizados: set[str], ativos: set[str]) -> dict[str, set[str]]:
    """Compara os dois conjuntos e devolve as tres categorias da auditoria.

    Cada categoria e uma operacao de conjunto direta — sets sao a
    estrutura natural para comparar colecoes de permissoes.
    """
    return {
        "ok": autorizados & ativos,             # regulares
        "nao_autorizadas": ativos - autorizados,  # risco: ativas sem cadastro
        "revogadas": autorizados - ativos,        # cadastradas sem uso
    }


def main() -> None:
    # Dados de entrada do enunciado
    autorizados = {"leitura", "escrita", "exportar", "admin"}
    ativos = {"leitura", "escrita", "imprimir"}

    # Executa a auditoria
    resultado = auditar_permissoes(autorizados, ativos)

    # Relatorio: destaca o alerta quando ha permissao ativa sem autorizacao
    print("=== AUDITORIA DE PERMISSOES ===")
    print(f"Permissoes ok:    {sorted(resultado['ok'])}")
    print(f"Nao autorizadas:  {sorted(resultado['nao_autorizadas'])}")
    print(f"Revogadas:        {sorted(resultado['revogadas'])}")
    # Alerta explicito ajuda o time de seguranca a agir rapido
    if resultado["nao_autorizadas"]:
        print("ALERTA: existem permissoes ativas sem autorizacao!")


if __name__ == "__main__":
    main()
```

</details>
