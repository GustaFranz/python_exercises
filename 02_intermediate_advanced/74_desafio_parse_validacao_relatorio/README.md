# 74 - DESAFIO - Parse, validacao e relatorio

## Objetivo

Combinar regex, estrutura aninhada/recursao leve e closure num case de qualidade de dados.

## Conteudos cobertos

- Regex (`re`)
- Recursao ou percurso de estrutura aninhada
- Closure / fabrica de validadores
- Relatorio textual

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | QualiData Servicos |
| **Setor** | Qualidade de dados / backoffice |
| **Solicitacao** | Parsear payloads textuais, validar campos e gerar relatorio por cliente. |

## Enunciado

Linhas brutas do staging:
```python
linhas = [
    "cliente=Ana;telefone=11999998888;score=80",
    "cliente=Bruno;telefone=123;score=45",
    "cliente=Carla;telefone=21988887777;score=95",
    "cliente=;telefone=11977776666;score=70",
]
```

Arvore de configuracao:
```python
config = {
    "regras": {
        "telefone": {"min_digitos": 11},
        "score": {"minimo": 50, "maximo": 100},
    }
}
```

Padrao regex: `r"cliente=(.*?);telefone=(.*?);score=(\d+)"`

1) Com regex, extraia `cliente`, `telefone`, `score` de cada linha.
2) Crie fabrica `criar_validador_digitos(minimo)` (closure) para validar telefone.
3) Crie fabrica `criar_validador_faixa(minimo, maximo)` para validar score.
4) Percorra `config` recursivamente para ler limites e montar os validadores.
5) Classifique cada registro: `ok` ou `rejeitado` + motivos (cliente vazio, telefone invalido, score fora da faixa).
6) Gere um relatorio consolidado com:
   - total `ok` e total `rejeitado`
   - lista de aprovados (score >= 50 e telefone valido)

Exemplo de saida:

```
=== Relatorio consolidado ===
Total ok: 2
Total rejeitado: 2
Aprovados: Ana (score 80), Carla (score 95)
Rejeitados:
- Bruno: telefone invalido (3 digitos)
- (vazio): cliente vazio
```

## Passo a passo

1. Importe `re` e crie `linhas`, `config` e o padrao `PADRAO = r"cliente=(.*?);telefone=(.*?);score=(\d+)"` no topo.
2. Defina a fabrica `criar_validador_digitos(minimo)`:
   - funcao interna `validar(texto: str) -> bool` retorna `True` se `texto` for composto so de digitos (`texto.isdigit()`) e tiver `len(texto) >= minimo`;
   - retorne a funcao interna (closure captura `minimo`).
3. Defina a fabrica `criar_validador_faixa(minimo, maximo)`:
   - funcao interna `validar(valor: int) -> bool` retorna `minimo <= valor <= maximo`.
4. Defina a funcao recursiva `buscar_valor(no: dict, chave: str)`:
   - caso base: se `chave in no`, retorne `no[chave]`;
   - caso recursivo: percorra `no.values()`, e para cada valor que for `dict`, chame `buscar_valor` nele; se achar algo diferente de `None`, retorne;
   - se nada for encontrado, retorne `None`.
5. Monte os validadores lendo os limites da config com a funcao recursiva:
   - `validar_telefone = criar_validador_digitos(buscar_valor(config, "min_digitos"))`;
   - `validar_score = criar_validador_faixa(buscar_valor(config, "minimo"), buscar_valor(config, "maximo"))`.
6. Defina `classificar_linha(linha: str) -> dict`:
   - aplique `re.search(PADRAO, linha)` e extraia `cliente = match.group(1).strip()`, `telefone = match.group(2)`, `score = int(match.group(3))`;
   - crie uma lista `motivos = []`;
   - se `cliente` for vazio, adicione `"cliente vazio"`;
   - se `validar_telefone(telefone)` for `False`, adicione `f"telefone invalido ({len(telefone)} digitos)"`;
   - se `validar_score(score)` for `False`, adicione `f"score fora da faixa ({score})"`;
   - retorne dict com `cliente`, `telefone`, `score`, `status` (`"ok"` se `motivos` vazio, senao `"rejeitado"`) e `motivos`.
7. Percorra `linhas` classificando cada registro e separe em duas listas: `aprovados` e `rejeitados`.
8. Gere o relatorio consolidado: totais de `ok` e `rejeitado`, aprovados no formato `Nome (score N)` unidos por virgula, e rejeitados um por linha com os motivos (use `(vazio)` quando o cliente for vazio).

## Como executar

```bash
cd "74_desafio_parse_validacao_relatorio"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import re

# Linhas brutas vindas do staging
linhas = [
    "cliente=Ana;telefone=11999998888;score=80",
    "cliente=Bruno;telefone=123;score=45",
    "cliente=Carla;telefone=21988887777;score=95",
    "cliente=;telefone=11977776666;score=70",
]

# Arvore de configuracao com as regras de validacao
config = {
    "regras": {
        "telefone": {"min_digitos": 11},
        "score": {"minimo": 50, "maximo": 100},
    }
}

# Grupos: (1) cliente, (2) telefone, (3) score
PADRAO = r"cliente=(.*?);telefone=(.*?);score=(\d+)"


def criar_validador_digitos(minimo):
    # Closure: minimo fica capturado para uso nas validacoes
    def validar(texto):
        # Valido se e composto so de digitos e atinge o tamanho minimo
        return texto.isdigit() and len(texto) >= minimo

    return validar


def criar_validador_faixa(minimo, maximo):
    # Closure: faixa capturada uma unica vez
    def validar(valor):
        return minimo <= valor <= maximo

    return validar


def buscar_valor(no, chave):
    # Caso base: a chave esta neste nivel do dict
    if chave in no:
        return no[chave]

    # Caso recursivo: procura dentro de cada sub-dict
    for valor in no.values():
        if isinstance(valor, dict):
            achado = buscar_valor(valor, chave)
            if achado is not None:
                return achado

    # Nao encontrou em lugar nenhum
    return None


# Monta os validadores lendo os limites da config recursivamente
validar_telefone = criar_validador_digitos(buscar_valor(config, "min_digitos"))
validar_score = criar_validador_faixa(
    buscar_valor(config, "minimo"), buscar_valor(config, "maximo")
)


def classificar_linha(linha):
    # Extrai os 3 campos com regex
    match = re.search(PADRAO, linha)
    cliente = match.group(1).strip()
    telefone = match.group(2)
    score = int(match.group(3))

    # Acumula todos os motivos de rejeicao encontrados
    motivos = []
    if not cliente:
        motivos.append("cliente vazio")
    if not validar_telefone(telefone):
        motivos.append(f"telefone invalido ({len(telefone)} digitos)")
    if not validar_score(score):
        motivos.append(f"score fora da faixa ({score})")

    # Sem motivos = registro ok; com motivos = rejeitado
    status = "ok" if not motivos else "rejeitado"
    return {"cliente": cliente, "score": score, "status": status, "motivos": motivos}


# Classifica todas as linhas e separa em aprovados e rejeitados
registros = [classificar_linha(linha) for linha in linhas]
aprovados = [r for r in registros if r["status"] == "ok"]
rejeitados = [r for r in registros if r["status"] == "rejeitado"]

# Relatorio consolidado
print("=== Relatorio consolidado ===")
print(f"Total ok: {len(aprovados)}")
print(f"Total rejeitado: {len(rejeitados)}")

# Aprovados em uma linha: Nome (score N), Nome (score N)
lista_aprovados = ", ".join(f"{r['cliente']} (score {r['score']})" for r in aprovados)
print(f"Aprovados: {lista_aprovados}")

print("Rejeitados:")
for r in rejeitados:
    # Cliente vazio aparece como (vazio) no relatorio
    nome = r["cliente"] if r["cliente"] else "(vazio)"
    print(f"- {nome}: {'; '.join(r['motivos'])}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Pipeline de qualidade de dados: parse (regex) + validacao (closures) + relatorio.

Estrutura tipica de mercado: constantes e configuracao no topo, fabricas de
validadores reutilizaveis, um dataclass para o registro classificado e um
main que apenas orquestra e apresenta.
"""

import re
from collections.abc import Callable
from dataclasses import dataclass, field

LINHAS = [
    "cliente=Ana;telefone=11999998888;score=80",
    "cliente=Bruno;telefone=123;score=45",
    "cliente=Carla;telefone=21988887777;score=95",
    "cliente=;telefone=11977776666;score=70",
]

CONFIG = {
    "regras": {
        "telefone": {"min_digitos": 11},
        "score": {"minimo": 50, "maximo": 100},
    }
}

# Grupos nomeados documentam o payload esperado
PADRAO = re.compile(r"cliente=(?P<cliente>.*?);telefone=(?P<telefone>.*?);score=(?P<score>\d+)")


@dataclass
class Registro:
    """Resultado da classificacao de uma linha do staging."""

    cliente: str
    telefone: str
    score: int
    motivos: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        # Registro aprovado quando nenhum motivo de rejeicao foi acumulado
        return not self.motivos


def criar_validador_digitos(minimo: int) -> Callable[[str], bool]:
    """Fabrica de validador: texto so com digitos e tamanho minimo."""

    def validar(texto: str) -> bool:
        return texto.isdigit() and len(texto) >= minimo

    return validar


def criar_validador_faixa(minimo: int, maximo: int) -> Callable[[int], bool]:
    """Fabrica de validador de faixa numerica fechada [minimo, maximo]."""

    def validar(valor: int) -> bool:
        return minimo <= valor <= maximo

    return validar


def buscar_valor(no: dict, chave: str):
    """Busca recursiva de uma chave em dict aninhado; None se ausente."""
    if chave in no:
        return no[chave]

    for valor in no.values():
        if isinstance(valor, dict):
            achado = buscar_valor(valor, chave)
            if achado is not None:
                return achado

    return None


def classificar(linha: str, validar_telefone, validar_score) -> Registro:
    """Parseia a linha e acumula os motivos de rejeicao aplicaveis."""
    match = PADRAO.search(linha)
    cliente = match.group("cliente").strip()
    telefone = match.group("telefone")
    score = int(match.group("score"))

    registro = Registro(cliente=cliente, telefone=telefone, score=score)

    # Cada regra adiciona seu motivo — o registro pode falhar em mais de uma
    if not cliente:
        registro.motivos.append("cliente vazio")
    if not validar_telefone(telefone):
        registro.motivos.append(f"telefone invalido ({len(telefone)} digitos)")
    if not validar_score(score):
        registro.motivos.append(f"score fora da faixa ({score})")

    return registro


def main() -> None:
    # Limites vem da config aninhada, lidos via busca recursiva
    validar_telefone = criar_validador_digitos(buscar_valor(CONFIG, "min_digitos"))
    validar_score = criar_validador_faixa(
        buscar_valor(CONFIG, "minimo"), buscar_valor(CONFIG, "maximo")
    )

    registros = [classificar(linha, validar_telefone, validar_score) for linha in LINHAS]

    # Particiona em aprovados e rejeitados em uma passada logica
    aprovados = [r for r in registros if r.ok]
    rejeitados = [r for r in registros if not r.ok]

    print("=== Relatorio consolidado ===")
    print(f"Total ok: {len(aprovados)}")
    print(f"Total rejeitado: {len(rejeitados)}")

    resumo_aprovados = ", ".join(f"{r.cliente} (score {r.score})" for r in aprovados)
    print(f"Aprovados: {resumo_aprovados}")

    print("Rejeitados:")
    for registro in rejeitados:
        # "or" devolve o rotulo (vazio) quando o nome e string vazia
        nome = registro.cliente or "(vazio)"
        print(f"- {nome}: {'; '.join(registro.motivos)}")


if __name__ == "__main__":
    main()
```

</details>
