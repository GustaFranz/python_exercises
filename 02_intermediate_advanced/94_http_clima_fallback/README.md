# 94 - HTTP: consulta com fallback

## Objetivo

Consultar API simulada de clima com dados padrao em caso de falha.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | AgroEscola |
| **Setor** | Educacao / campo |
| **Solicitacao** | Exibir previsao do tempo para visita tecnica mesmo se API falhar. |

## Enunciado

Dados padrao (fallback):
```python
DADOS_PADRAO = {"cidade": "Campinas", "temp": 25, "fonte": "cache local"}
```

Implemente:

```python
def simular_clima_api(sucesso: bool = True) -> dict:
    # sucesso True  -> {"status": 200, "cidade": "Campinas", "temp": 28}
    # sucesso False -> {"status": 0, "erro": "Timeout"}

def obter_previsao(usar_api: bool = True) -> dict:
    # tenta API; se status 200 retorna dados com fonte "api"
    # senao retorna DADOS_PADRAO com aviso "Usando dados em cache"
```

No `main`:

1) Teste com API falhando (`usar_api=True`, simule falha).
2) Exiba fonte dos dados (`api` ou `cache local`).

Exemplo de saida:

```
Usando dados em cache
Cidade: Campinas | Temp: 25 | Fonte: cache local
```

## Passo a passo

1. Defina a constante `DADOS_PADRAO = {"cidade": "Campinas", "temp": 25, "fonte": "cache local"}` no topo — este e o plano B quando a API falha.
2. Defina `simular_clima_api(sucesso=True)` que:
   - Se `sucesso` for `True`, retorna `{"status": 200, "cidade": "Campinas", "temp": 28}`.
   - Senao, retorna `{"status": 0, "erro": "Timeout"}`.
3. Defina `obter_previsao(usar_api=True)` que:
   - Se `usar_api` for `True`, chama `resposta = simular_clima_api(sucesso=False)` — passe `False` para simular a falha pedida no teste.
   - Se `resposta["status"] == 200`: monta e retorna um dict com `cidade`, `temp` e `fonte: "api"`.
   - Em qualquer outro caso (falha ou `usar_api=False`): exibe o aviso `"Usando dados em cache"` e retorna `DADOS_PADRAO`.
4. No fluxo principal:
   - Chame `previsao = obter_previsao(usar_api=True)`.
   - Exiba `f"Cidade: {previsao['cidade']} | Temp: {previsao['temp']} | Fonte: {previsao['fonte']}"`.
5. Para conferir o caminho de sucesso, troque temporariamente o `sucesso=False` por `sucesso=True` e veja a fonte mudar para `api` com temp 28.

## Como executar

```bash
cd "94_http_clima_fallback"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Plano B: dados usados quando a API de clima nao responde
DADOS_PADRAO = {"cidade": "Campinas", "temp": 25, "fonte": "cache local"}


def simular_clima_api(sucesso=True):
    # Simula a API de clima: sucesso ou timeout, conforme o parametro
    if sucesso:
        return {"status": 200, "cidade": "Campinas", "temp": 28}
    return {"status": 0, "erro": "Timeout"}


def obter_previsao(usar_api=True):
    if usar_api:
        # sucesso=False forca a falha para testar o fallback
        resposta = simular_clima_api(sucesso=False)

        # API respondeu: monta o dict marcando a fonte como "api"
        if resposta["status"] == 200:
            return {
                "cidade": resposta["cidade"],
                "temp": resposta["temp"],
                "fonte": "api",
            }

    # API falhou (ou nem foi tentada): avisa e usa o cache local
    print("Usando dados em cache")
    return DADOS_PADRAO


previsao = obter_previsao(usar_api=True)
# Exibe a previsao com a fonte, provando de onde vieram os dados
print(f"Cidade: {previsao['cidade']} | Temp: {previsao['temp']} | Fonte: {previsao['fonte']}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Previsao do tempo da AgroEscola com fallback para cache local."""

# Constante imutavel do fallback; copia e feita ao retornar para
# evitar que o chamador altere o dict padrao por acidente
DADOS_PADRAO = {"cidade": "Campinas", "temp": 25, "fonte": "cache local"}


def simular_clima_api(sucesso: bool = True) -> dict:
    """Simula a API de clima: 200 com dados ou status 0 (timeout)."""
    if sucesso:
        return {"status": 200, "cidade": "Campinas", "temp": 28}
    return {"status": 0, "erro": "Timeout"}


def obter_previsao(usar_api: bool = True, api_disponivel: bool = False) -> dict:
    """Obtem a previsao da API; em falha, cai para os dados em cache.

    api_disponivel permite simular sucesso/falha sem editar a funcao.
    """
    # Guard clause: sem API, vai direto para o fallback
    if not usar_api:
        print("Usando dados em cache")
        return dict(DADOS_PADRAO)

    resposta = simular_clima_api(sucesso=api_disponivel)

    if resposta["status"] == 200:
        # Fonte "api" identifica dados frescos vindos do servico
        return {"cidade": resposta["cidade"], "temp": resposta["temp"], "fonte": "api"}

    # Falha na API: avisa o usuario e devolve copia do cache
    print("Usando dados em cache")
    return dict(DADOS_PADRAO)


def main() -> None:
    # api_disponivel=False reproduz o cenario de falha do enunciado
    previsao = obter_previsao(usar_api=True, api_disponivel=False)
    print(
        f"Cidade: {previsao['cidade']} | "
        f"Temp: {previsao['temp']} | "
        f"Fonte: {previsao['fonte']}"
    )


if __name__ == "__main__":
    main()
```

</details>
