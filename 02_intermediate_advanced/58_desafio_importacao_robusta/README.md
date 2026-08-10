# 58 - DESAFIO - Importacao robusta de leads

## Objetivo

Importar CSV/JSON com excecao customizada e try/except/finally em case de entrevista.

## Conteudos cobertos

- CSV e JSON
- Excecao customizada (`raise`)
- `try` / `except` / `finally`
- Validacao de payload

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GrowLeads Hub |
| **Setor** | Marketing / operacoes comerciais |
| **Solicitacao** | Importar lote de leads do staging sem derrubar o job; auditar falhas. |

## Enunciado

Crie `leads.csv` com linhas validas e invalidas:
```
nome,email,idade
Ana,ana@empresa.com,28
Bruno,bruno_sem_arroba,30
Carla,carla@escola.org,-2
Diego,diego@corp.com,41
```

Checklist:

1) Defina `LeadInvalidoError(Exception)`.
2) `validar_lead(nome, email, idade)`:
   - email deve conter `@`
   - idade int entre 18 e 100
   - se invalido: `raise LeadInvalidoError` com mensagem clara
3) Leia o CSV com `with open`; para cada linha use try/except:
   - sucesso -> lista `importados`
   - falha -> lista `rejeitados` com motivo
4) No `finally` de cada linha (ou do lote), registre em `importacao.log` se processou a linha.
5) Persista `importados` em `leads_ok.json` e imprima resumo (ok / rejeitados / taxa de sucesso %).

## Passo a passo

1. Importe `csv` e `json`; defina as constantes `ARQ_LEADS = "leads.csv"`, `ARQ_LOG = "importacao.log"`, `ARQ_SAIDA = "leads_ok.json"`, `IDADE_MIN = 18` e `IDADE_MAX = 100`.
2. Grave o `leads.csv` de exemplo no inicio do script com `with open(..., "w", encoding="utf-8")` usando exatamente as 4 linhas de dados do enunciado.
3. Defina `class LeadInvalidoError(Exception)` com docstring curta.
4. Defina `def validar_lead(nome, email, idade):`:
   - Se `"@" not in email`, levante `LeadInvalidoError(f"email invalido: {email}")`.
   - Se `not IDADE_MIN <= idade <= IDADE_MAX`, levante `LeadInvalidoError(f"idade fora de {IDADE_MIN}-{IDADE_MAX}: {idade}")`.
5. Crie as listas vazias `importados` e `rejeitados`.
6. Abra o log com `with open(ARQ_LOG, "w", encoding="utf-8") as log:` (modo `"w"` para zerar a cada execucao) e, dentro dele, abra o CSV com `with open(ARQ_LEADS, "r", encoding="utf-8", newline="") as f:` percorrendo `csv.DictReader(f)`.
7. Para cada linha, use `try/except/finally`:
   - No `try:`, converta `idade = int(linha["idade"])` (pode levantar `ValueError`), chame `validar_lead(...)` e adicione o dict `{"nome", "email", "idade"}` em `importados`.
   - No `except (LeadInvalidoError, ValueError) as e:`, adicione `{"nome": ..., "motivo": str(e)}` em `rejeitados` — nunca use bare `except`.
   - No `finally:`, grave no log `f"processado: {nome}\n"` — roda para toda linha, valida ou nao.
8. Grave `importados` em `leads_ok.json` com `json.dump(importados, f, ensure_ascii=False, indent=2)`.
9. Calcule `taxa = round(len(importados) / total * 100, 1)` onde `total = len(importados) + len(rejeitados)`.
10. Imprima o resumo: importados, rejeitados (com motivo de cada um) e taxa de sucesso %.

## Como executar

```bash
cd "58_desafio_importacao_robusta"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import csv
import json

# Arquivos e regras de negocio centralizados no topo
ARQ_LEADS = "leads.csv"
ARQ_LOG = "importacao.log"
ARQ_SAIDA = "leads_ok.json"
IDADE_MIN = 18
IDADE_MAX = 100

# CSV de staging do enunciado: 2 validos e 2 invalidos
CSV_EXEMPLO = """nome,email,idade
Ana,ana@empresa.com,28
Bruno,bruno_sem_arroba,30
Carla,carla@escola.org,-2
Diego,diego@corp.com,41
"""


# Excecao de negocio da importacao
class LeadInvalidoError(Exception):
    pass


def validar_lead(nome, email, idade):
    # Regra 1: email precisa conter @
    if "@" not in email:
        raise LeadInvalidoError(f"email invalido: {email}")
    # Regra 2: idade dentro da faixa aceita
    if not IDADE_MIN <= idade <= IDADE_MAX:
        raise LeadInvalidoError(f"idade fora de {IDADE_MIN}-{IDADE_MAX}: {idade}")


# Gera o arquivo de staging para o exercicio ser self-contained
with open(ARQ_LEADS, "w", encoding="utf-8") as f:
    f.write(CSV_EXEMPLO)

importados = []
rejeitados = []

# Log em modo "w": zera a cada execucao para saida reproduzivel
with open(ARQ_LOG, "w", encoding="utf-8") as log:
    with open(ARQ_LEADS, "r", encoding="utf-8", newline="") as f:
        for linha in csv.DictReader(f):
            nome = linha["nome"]
            try:
                # int() pode levantar ValueError se a idade nao for numerica
                idade = int(linha["idade"])
                validar_lead(nome, linha["email"], idade)
                # Linha valida entra na lista de importados
                importados.append(
                    {"nome": nome, "email": linha["email"], "idade": idade}
                )
            except (LeadInvalidoError, ValueError) as e:
                # Nunca bare except: captura apenas os erros esperados
                rejeitados.append({"nome": nome, "motivo": str(e)})
            finally:
                # Auditoria: TODA linha processada gera registro no log
                log.write(f"processado: {nome}\n")

# Persiste os leads aprovados em JSON legivel
with open(ARQ_SAIDA, "w", encoding="utf-8") as f:
    json.dump(importados, f, ensure_ascii=False, indent=2)

# Resumo do job com taxa de sucesso
total = len(importados) + len(rejeitados)
taxa = round(len(importados) / total * 100, 1)

print(f"Importados: {len(importados)}")
print(f"Rejeitados: {len(rejeitados)}")
for r in rejeitados:
    print(f"  - {r['nome']}: {r['motivo']}")
print(f"Taxa de sucesso: {taxa}%")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Importacao robusta de leads: valida, separa rejeitados e audita cada linha."""

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path

ARQ_LEADS = Path("leads.csv")
ARQ_LOG = Path("importacao.log")
ARQ_SAIDA = Path("leads_ok.json")
IDADE_MIN, IDADE_MAX = 18, 100

CSV_EXEMPLO = """nome,email,idade
Ana,ana@empresa.com,28
Bruno,bruno_sem_arroba,30
Carla,carla@escola.org,-2
Diego,diego@corp.com,41
"""


class LeadInvalidoError(Exception):
    """Lead fora das regras de negocio da importacao."""


@dataclass
class Lead:
    """Lead validado, pronto para persistencia."""

    nome: str
    email: str
    idade: int

    @classmethod
    def de_linha_csv(cls, linha: dict[str, str]) -> "Lead":
        """Converte e valida uma linha crua do CSV.

        Toda falha vira LeadInvalidoError: quem importa trata um unico
        tipo de erro, sem conhecer os detalhes da validacao.
        """
        try:
            idade = int(linha["idade"])
        except ValueError as exc:
            # from exc preserva a causa original no traceback
            raise LeadInvalidoError(f"idade nao numerica: {linha['idade']!r}") from exc
        if "@" not in linha["email"]:
            raise LeadInvalidoError(f"email invalido: {linha['email']}")
        if not IDADE_MIN <= idade <= IDADE_MAX:
            raise LeadInvalidoError(f"idade fora de {IDADE_MIN}-{IDADE_MAX}: {idade}")
        return cls(nome=linha["nome"], email=linha["email"], idade=idade)


def importar_leads(origem: Path, log: Path) -> tuple[list[Lead], list[dict]]:
    """Processa o CSV linha a linha sem derrubar o job em falhas pontuais."""
    importados: list[Lead] = []
    rejeitados: list[dict] = []

    with log.open("w", encoding="utf-8") as arq_log:
        with origem.open(encoding="utf-8", newline="") as f:
            for linha in csv.DictReader(f):
                try:
                    importados.append(Lead.de_linha_csv(linha))
                except LeadInvalidoError as erro:
                    rejeitados.append({"nome": linha["nome"], "motivo": str(erro)})
                finally:
                    # Auditoria por linha: roda em sucesso e em falha
                    arq_log.write(f"processado: {linha['nome']}\n")

    return importados, rejeitados


def main() -> None:
    # Gera o staging de exemplo (self-contained)
    ARQ_LEADS.write_text(CSV_EXEMPLO, encoding="utf-8")

    importados, rejeitados = importar_leads(ARQ_LEADS, ARQ_LOG)

    # asdict converte cada dataclass em dict serializavel
    ARQ_SAIDA.write_text(
        json.dumps([asdict(lead) for lead in importados], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    total = len(importados) + len(rejeitados)
    taxa = round(len(importados) / total * 100, 1)

    print(f"Importados: {len(importados)}")
    print(f"Rejeitados: {len(rejeitados)}")
    for rejeitado in rejeitados:
        print(f"  - {rejeitado['nome']}: {rejeitado['motivo']}")
    print(f"Taxa de sucesso: {taxa}%")


if __name__ == "__main__":
    main()
```

</details>
