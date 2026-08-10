# 106 - DESAFIO - Monitor de integracoes

## Objetivo

Case mais trabalhado: classes + Counter + HTTP simulado com cache e fallback.

## Conteudos cobertos

- Classes simples
- `Counter` / agregacoes
- Tratamento HTTP simulado (retry/fallback/cache)
- Logging de falhas
- Relatorio operacional

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Nexus Integracoes |
| **Setor** | Tecnologia / integracoes B2B |
| **Solicitacao** | Monitorar consultas a APIs parceiras com cache, fallback e painel de falhas. |

## Estrutura sugerida

```
106_desafio_monitor_integracoes/
├── main.py
├── monitor.py
└── README.md
```

## Enunciado

Simule um cliente HTTP instavel:

```python
def api_parceiro(endpoint: str, falhar: bool = False) -> dict:
    if falhar:
        raise ConnectionError(f"Falha ao consultar {endpoint}")
    return {"endpoint": endpoint, "payload": {"ok": True, "valor": 10}}
```

Checklist (trabalhado, ainda intermediario):

1) Classe `CacheSimples` com `get(chave)` e `set(chave, valor)`.
2) Classe `MonitorIntegracao`:
   - `consultar(endpoint, forcar_falha=False)`:
     - se cache hit -> retorna do cache e registra origem `"cache"`
     - senao chama `api_parceiro`
     - em sucesso: grava cache, origem `"api"`
     - em falha: registra erro (lista ou logging), tenta fallback `{"endpoint": endpoint, "payload": {"ok": False, "valor": 0}}`, origem `"fallback"`
3) Guarde historico de consultas: lista de dicts `{endpoint, origem, ok}`.
4) Com `Counter`, monte painel: contagem por `origem` e por `endpoint`.
5) Metodo `relatorio()` imprime:
   - total de consultas
   - taxa de fallback %
   - top endpoint mais consultado
   - lista de falhas
6) Em `main.py`, execute um roteiro: 2 sucessos no mesmo endpoint (2ª deve ser cache),
   1 falha com fallback, 1 sucesso em outro endpoint; depois imprima o relatorio.

## Passo a passo

1. Em `monitor.py`, implemente a funcao `api_parceiro(endpoint: str, falhar: bool = False) -> dict` exatamente como no enunciado (levanta `ConnectionError` quando `falhar=True`).
2. Implemente a classe `CacheSimples`:
   - `__init__(self)` inicia um dict interno vazio (`self._dados = {}`).
   - `get(self, chave)` retorna o valor guardado ou `None` (use `dict.get`).
   - `set(self, chave, valor)` grava `self._dados[chave] = valor`.
3. Implemente a classe `MonitorIntegracao` com `__init__(self)` criando: `self.cache = CacheSimples()`, `self.historico = []` (lista de dicts `{endpoint, origem, ok}`) e `self.falhas = []` (mensagens de erro).
4. Implemente `consultar(self, endpoint, forcar_falha=False)` nesta ordem:
   - Consulte o cache primeiro: se houver valor, registre `{endpoint, origem: "cache", ok: True}` no historico e retorne o valor.
   - Senao, chame `api_parceiro(endpoint, falhar=forcar_falha)` dentro de `try/except ConnectionError`.
   - Em sucesso: grave a resposta no cache, registre origem `"api"` com `ok=True` e retorne a resposta.
   - Em falha: guarde a mensagem do erro em `self.falhas`, monte o dict de fallback `{"endpoint": endpoint, "payload": {"ok": False, "valor": 0}}`, registre origem `"fallback"` com `ok=False` e retorne o fallback.
5. Implemente `relatorio(self)` usando `Counter`:
   - `Counter(c["origem"] for c in self.historico)` para contagem por origem.
   - `Counter(c["endpoint"] for c in self.historico)` para contagem por endpoint (use `.most_common(1)` para o top).
   - Imprima: total de consultas, taxa de fallback em % (`fallbacks / total * 100`), top endpoint e a lista de falhas.
6. Em `main.py`, importe `MonitorIntegracao` de `monitor` e execute o roteiro: `consultar("/notas")`, `consultar("/notas")` (deve vir do cache), `consultar("/clima", forcar_falha=True)` (fallback) e `consultar("/alunos")`; por fim chame `relatorio()`.

## Como executar

```bash
cd "106_desafio_monitor_integracoes"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

**`monitor.py`**

```python
from collections import Counter


def api_parceiro(endpoint: str, falhar: bool = False) -> dict:
    # Simula um cliente HTTP instavel: falha sob demanda para testes
    if falhar:
        raise ConnectionError(f"Falha ao consultar {endpoint}")
    return {"endpoint": endpoint, "payload": {"ok": True, "valor": 10}}


class CacheSimples:
    def __init__(self):
        # Dict interno guarda pares endpoint -> resposta
        self._dados = {}

    def get(self, chave):
        # dict.get retorna None quando a chave nao existe (cache miss)
        return self._dados.get(chave)

    def set(self, chave, valor):
        # Grava/atualiza o valor associado a chave
        self._dados[chave] = valor


class MonitorIntegracao:
    def __init__(self):
        self.cache = CacheSimples()
        # Historico: um dict {endpoint, origem, ok} por consulta feita
        self.historico = []
        # Lista de mensagens de erro para auditoria
        self.falhas = []

    def _registrar(self, endpoint, origem, ok):
        # Metodo auxiliar: centraliza o append no historico
        self.historico.append({"endpoint": endpoint, "origem": origem, "ok": ok})

    def consultar(self, endpoint, forcar_falha=False):
        # 1) Cache primeiro: evita chamada externa repetida
        resposta = self.cache.get(endpoint)
        if resposta is not None:
            self._registrar(endpoint, "cache", True)
            return resposta

        # 2) Cache vazio: tenta a API protegido por try/except
        try:
            resposta = api_parceiro(endpoint, falhar=forcar_falha)
        except ConnectionError as erro:
            # 3) Falha: registra o erro e devolve fallback sem derrubar o programa
            self.falhas.append(str(erro))
            fallback = {"endpoint": endpoint, "payload": {"ok": False, "valor": 0}}
            self._registrar(endpoint, "fallback", False)
            return fallback

        # 4) Sucesso: grava no cache para as proximas consultas
        self.cache.set(endpoint, resposta)
        self._registrar(endpoint, "api", True)
        return resposta

    def relatorio(self):
        total = len(self.historico)
        # Counter conta ocorrencias de cada origem e de cada endpoint
        por_origem = Counter(c["origem"] for c in self.historico)
        por_endpoint = Counter(c["endpoint"] for c in self.historico)

        # Taxa de fallback em percentual sobre o total de consultas
        taxa_fallback = por_origem["fallback"] / total * 100 if total else 0.0
        # most_common(1) devolve [(endpoint, contagem)] do mais consultado
        top_endpoint, qtd_top = por_endpoint.most_common(1)[0]

        print("=== RELATORIO DO MONITOR ===")
        print(f"Total de consultas: {total}")
        print(f"Por origem: {dict(por_origem)}")
        print(f"Taxa de fallback: {taxa_fallback:.1f}%")
        print(f"Top endpoint: {top_endpoint} ({qtd_top} consultas)")
        print(f"Falhas registradas: {self.falhas}")
```

**`main.py`**

```python
from monitor import MonitorIntegracao

# Cria o monitor que orquestra cache, API e fallback
monitor = MonitorIntegracao()

# Roteiro do enunciado:
monitor.consultar("/notas")                      # 1ª vez: vai na API
monitor.consultar("/notas")                      # 2ª vez: cache hit
monitor.consultar("/clima", forcar_falha=True)   # falha -> fallback
monitor.consultar("/alunos")                     # sucesso em outro endpoint

# Painel final com Counter
monitor.relatorio()
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

**`monitor.py`**

```python
import logging
from collections import Counter
from dataclasses import dataclass

# Logger do modulo: falhas vao para o log em vez de print espalhado
logger = logging.getLogger(__name__)


def api_parceiro(endpoint: str, falhar: bool = False) -> dict:
    """Simula cliente HTTP instavel de um parceiro B2B."""
    if falhar:
        raise ConnectionError(f"Falha ao consultar {endpoint}")
    return {"endpoint": endpoint, "payload": {"ok": True, "valor": 10}}


class CacheSimples:
    """Cache chave -> valor em memoria, sem expiracao."""

    def __init__(self) -> None:
        self._dados: dict[str, dict] = {}

    def get(self, chave: str) -> dict | None:
        return self._dados.get(chave)

    def set(self, chave: str, valor: dict) -> None:
        self._dados[chave] = valor


# frozen: o registro de consulta e um fato historico, nao deve mudar
@dataclass(frozen=True)
class Consulta:
    """Registro de uma consulta feita pelo monitor."""

    endpoint: str
    origem: str  # "api", "cache" ou "fallback"
    ok: bool


class MonitorIntegracao:
    """Consulta APIs parceiras com cache, fallback e painel de falhas."""

    # Fallback padrao como constante de classe: um unico lugar para mudar
    PAYLOAD_FALLBACK = {"ok": False, "valor": 0}

    def __init__(self) -> None:
        self.cache = CacheSimples()
        self.historico: list[Consulta] = []
        self.falhas: list[str] = []

    def consultar(self, endpoint: str, forcar_falha: bool = False) -> dict:
        """Retorna a resposta do endpoint: cache > api > fallback."""
        # Guard clause: cache hit resolve a consulta imediatamente
        if (resposta := self.cache.get(endpoint)) is not None:
            self._registrar(endpoint, origem="cache", ok=True)
            return resposta

        try:
            resposta = api_parceiro(endpoint, falhar=forcar_falha)
        except ConnectionError as erro:
            # Falha vai para o log (auditoria) e para a lista do relatorio
            logger.error("Consulta falhou: %s", erro)
            self.falhas.append(str(erro))
            self._registrar(endpoint, origem="fallback", ok=False)
            return {"endpoint": endpoint, "payload": dict(self.PAYLOAD_FALLBACK)}

        # Sucesso: alimenta o cache antes de devolver
        self.cache.set(endpoint, resposta)
        self._registrar(endpoint, origem="api", ok=True)
        return resposta

    def _registrar(self, endpoint: str, origem: str, ok: bool) -> None:
        self.historico.append(Consulta(endpoint, origem, ok))

    def relatorio(self) -> None:
        """Imprime o painel operacional das consultas realizadas."""
        total = len(self.historico)
        if total == 0:
            print("Nenhuma consulta registrada.")
            return

        por_origem = Counter(c.origem for c in self.historico)
        por_endpoint = Counter(c.endpoint for c in self.historico)
        taxa_fallback = por_origem["fallback"] / total * 100
        top_endpoint, qtd_top = por_endpoint.most_common(1)[0]

        print("=== RELATORIO DO MONITOR ===")
        print(f"Total de consultas: {total}")
        print(f"Por origem: {dict(por_origem)}")
        print(f"Taxa de fallback: {taxa_fallback:.1f}%")
        print(f"Top endpoint: {top_endpoint} ({qtd_top} consultas)")
        print("Falhas registradas:")
        for falha in self.falhas:
            print(f"  - {falha}")
```

**`main.py`**

```python
import logging

from monitor import MonitorIntegracao


def main() -> None:
    # Configura o logging uma unica vez, no ponto de entrada do programa
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

    monitor = MonitorIntegracao()

    # Roteiro do enunciado: api, cache, fallback e novo endpoint
    monitor.consultar("/notas")
    monitor.consultar("/notas")
    monitor.consultar("/clima", forcar_falha=True)
    monitor.consultar("/alunos")

    monitor.relatorio()


if __name__ == "__main__":
    main()
```

</details>
