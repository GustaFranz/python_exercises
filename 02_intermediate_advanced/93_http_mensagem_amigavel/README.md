# 93 - HTTP: mensagem amigavel

## Objetivo

Traduzir erros tecnicos HTTP em mensagens para o usuario final.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / atendimento |
| **Solicitacao** | Exibir mensagens claras quando o portal de notas estiver fora do ar. |

## Enunciado

Mapeamento tecnico → amigavel:

| status | mensagem |
|--------|----------|
| `404` | `"Nao encontramos seu cadastro. Verifique a matricula."` |
| `500` | `"Estamos com instabilidade. Tente em alguns minutos."` |
| `0` (timeout) | `"Sem conexao com o servidor. Verifique sua internet."` |

Implemente:

```python
def mensagem_para_usuario(resposta: dict) -> str:
    # recebe dict com campo "status"
    # retorna string amigavel (sem detalhes tecnicos)
```

No `main`, teste os 3 status:

```python
{"status": 404}
{"status": 500}
{"status": 0}
```

Exemplo de saida:

```
404: Nao encontramos seu cadastro. Verifique a matricula.
500: Estamos com instabilidade. Tente em alguns minutos.
0: Sem conexao com o servidor. Verifique sua internet.
```

## Passo a passo

1. Crie no topo do arquivo um dict constante `MENSAGENS` que mapeia cada status para sua mensagem amigavel:
   - `404` → `"Nao encontramos seu cadastro. Verifique a matricula."`
   - `500` → `"Estamos com instabilidade. Tente em alguns minutos."`
   - `0` → `"Sem conexao com o servidor. Verifique sua internet."`
2. Defina `mensagem_para_usuario(resposta)` que:
   - Le o status com `resposta["status"]`.
   - Busca a mensagem no dict com `.get(status, mensagem_padrao)` — o segundo argumento cobre qualquer status inesperado sem quebrar o programa.
   - Retorna a string (a funcao nao imprime nada — funcao pura, quem chama decide o que fazer).
3. No fluxo principal:
   - Crie a lista de respostas de teste: `[{"status": 404}, {"status": 500}, {"status": 0}]`.
   - Percorra com `for` e exiba `f"{resposta['status']}: {mensagem_para_usuario(resposta)}"`.
4. Confira que a saida bate com o exemplo do enunciado.

## Como executar

```bash
cd "93_http_mensagem_amigavel"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Mapeamento status tecnico -> mensagem amigavel, definido uma unica vez
MENSAGENS = {
    404: "Nao encontramos seu cadastro. Verifique a matricula.",
    500: "Estamos com instabilidade. Tente em alguns minutos.",
    0: "Sem conexao com o servidor. Verifique sua internet.",
}


def mensagem_para_usuario(resposta):
    # Funcao pura: recebe o dict e devolve a string, sem imprimir nada
    status = resposta["status"]
    # .get com padrao: status desconhecido nao quebra o programa
    return MENSAGENS.get(status, "Ocorreu um erro inesperado. Tente novamente.")


# Respostas simuladas dos tres cenarios de falha
respostas = [{"status": 404}, {"status": 500}, {"status": 0}]

for resposta in respostas:
    # Exibe o status tecnico e a traducao amigavel lado a lado
    print(f"{resposta['status']}: {mensagem_para_usuario(resposta)}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Traducao de erros HTTP do portal de notas em mensagens amigaveis."""

from types import MappingProxyType

# MappingProxyType torna o mapeamento somente leitura (imutavel na pratica)
MENSAGENS_POR_STATUS = MappingProxyType({
    404: "Nao encontramos seu cadastro. Verifique a matricula.",
    500: "Estamos com instabilidade. Tente em alguns minutos.",
    0: "Sem conexao com o servidor. Verifique sua internet.",
})

MENSAGEM_PADRAO = "Ocorreu um erro inesperado. Tente novamente."


def mensagem_para_usuario(resposta: dict) -> str:
    """Converte a resposta tecnica em mensagem clara para o usuario final.

    Nunca expoe detalhes tecnicos; status desconhecido recebe mensagem padrao.
    """
    return MENSAGENS_POR_STATUS.get(resposta["status"], MENSAGEM_PADRAO)


def main() -> None:
    respostas = [{"status": 404}, {"status": 500}, {"status": 0}]
    for resposta in respostas:
        print(f"{resposta['status']}: {mensagem_para_usuario(resposta)}")


if __name__ == "__main__":
    main()
```

</details>
