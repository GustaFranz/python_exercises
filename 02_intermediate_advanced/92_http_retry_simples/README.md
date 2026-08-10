# 92 - HTTP: retry simples

## Objetivo

Tentar novamente consulta HTTP simulada apos falha temporaria.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / integracoes |
| **Solicitacao** | Repetir consulta ao servico de monitoramento quando falhar na primeira tentativa. |

## Enunciado

Implemente simulacao e retry:

```python
def simular_servico(tentativa: int) -> dict:
    # tentativa 1 -> {"status": 0, "erro": "Timeout"}
    # tentativa >= 2 -> {"status": 200, "dados": "Servidor OK"}

def consultar_com_retry(max_tentativas: int = 3):
    # tenta de 1 ate max_tentativas
    # retorna dados quando status 200
    # se esgotar tentativas: retorna None e mensagem de falha
```

No `main`:

1) Chame `consultar_com_retry(3)`.
2) Exiba resultado — falha na 1a tentativa, sucesso na 2a.

Exemplo de saida:

```
Tentativa 1: falhou (Timeout)
Tentativa 2: sucesso
Dados: Servidor OK
```

## Passo a passo

1. Defina `simular_servico(tentativa)` que:
   - Se `tentativa == 1`, retorna `{"status": 0, "erro": "Timeout"}` — simula a falha temporaria.
   - Se `tentativa >= 2`, retorna `{"status": 200, "dados": "Servidor OK"}`.
2. Defina `consultar_com_retry(max_tentativas=3)` que:
   - Percorre as tentativas com `for tentativa in range(1, max_tentativas + 1):`.
   - Em cada volta, chama `resposta = simular_servico(tentativa)`.
   - Se `resposta["status"] == 200`: exibe `f"Tentativa {tentativa}: sucesso"` e retorna `resposta["dados"]` (o `return` encerra o loop).
   - Senao: exibe `f"Tentativa {tentativa}: falhou ({resposta['erro']})"` e o loop continua.
   - Se o loop terminar sem sucesso, exibe mensagem de falha definitiva e retorna `None`.
3. No fluxo principal:
   - Chame `dados = consultar_com_retry(3)`.
   - Se `dados` nao for `None`, exiba `f"Dados: {dados}"`.
4. Execute e confira a sequencia: falha na tentativa 1, sucesso na tentativa 2, dados exibidos.

## Como executar

```bash
cd "92_http_retry_simples"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def simular_servico(tentativa):
    # Primeira tentativa sempre falha, simulando instabilidade temporaria
    if tentativa == 1:
        return {"status": 0, "erro": "Timeout"}
    # Da segunda em diante o servico responde normalmente
    return {"status": 200, "dados": "Servidor OK"}


def consultar_com_retry(max_tentativas=3):
    # range(1, max+1) gera tentativas numeradas de 1 ate o limite
    for tentativa in range(1, max_tentativas + 1):
        resposta = simular_servico(tentativa)

        # Sucesso: informa e retorna os dados (o return encerra o loop)
        if resposta["status"] == 200:
            print(f"Tentativa {tentativa}: sucesso")
            return resposta["dados"]

        # Falha: informa o erro e deixa o loop tentar de novo
        print(f"Tentativa {tentativa}: falhou ({resposta['erro']})")

    # Loop terminou sem sucesso: esgotou as tentativas
    print("Falha definitiva: tentativas esgotadas")
    return None


dados = consultar_com_retry(3)
# So exibe os dados se a consulta deu certo
if dados is not None:
    print(f"Dados: {dados}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Consulta ao servico de monitoramento da MonitoraTI com retry simples."""

MAX_TENTATIVAS_PADRAO = 3


def simular_servico(tentativa: int) -> dict:
    """Simula o servico: falha na primeira tentativa, responde nas demais."""
    if tentativa == 1:
        return {"status": 0, "erro": "Timeout"}
    return {"status": 200, "dados": "Servidor OK"}


def consultar_com_retry(max_tentativas: int = MAX_TENTATIVAS_PADRAO) -> str | None:
    """Tenta consultar o servico ate obter sucesso ou esgotar as tentativas.

    Retorna os dados da resposta ou None em falha definitiva.
    """
    for tentativa in range(1, max_tentativas + 1):
        resposta = simular_servico(tentativa)

        # Guard clause invertida: trata a falha e segue para a proxima volta
        if resposta["status"] != 200:
            print(f"Tentativa {tentativa}: falhou ({resposta['erro']})")
            continue

        print(f"Tentativa {tentativa}: sucesso")
        return resposta["dados"]

    # Em producao, aqui tambem entraria um log de ERROR/alerta
    print("Falha definitiva: tentativas esgotadas")
    return None


def main() -> None:
    dados = consultar_com_retry()
    if dados is not None:
        print(f"Dados: {dados}")


if __name__ == "__main__":
    main()
```

</details>
