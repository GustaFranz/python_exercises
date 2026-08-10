# 91 - Introducao a tratamento HTTP

## Objetivo

Tratar respostas simuladas 200, 404 e timeout em cliente HTTP.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / integracoes |
| **Solicitacao** | Consumir API de matriculas com tratamento correto de falhas. |

## Visao do bloco (exercicios 91 a 95)

Topico **API com tratamento HTTP**: lidar com sucesso, erro e indisponibilidade.

| # | Foco |
|---|------|
| 91 | Introducao + 200 vs 404 vs timeout |
| 92 | Retry simples |
| 93 | Mensagem amigavel ao usuario |
| 94 | Consulta clima com fallback |
| 95 | Cliente HTTP com cache e log de falhas |

## Enunciado

Implemente `simular_api(codigo) -> dict` com respostas simuladas:

- `200` → `{"status": 200, "dados": {"aluno": "Ana", "turma": "7B"}}`
- `404` → `{"status": 404, "erro": "Matricula nao encontrada"}`
- `0` ou `"timeout"` → `{"status": 0, "erro": "Timeout"}`

Implemente `consultar_matricula(codigo)` que chama `simular_api` e trata cada caso:

- **200** — exibe dados do aluno (nome e turma)
- **404** — exibe erro amigavel
- **timeout (status 0)** — exibe `"Servico indisponivel, tente mais tarde"`

Teste no `main` com codigos **200**, **404** e **"timeout"**.

## Passo a passo

1. Defina `simular_api(codigo)` que:
   - Se `codigo == 200`, retorna `{"status": 200, "dados": {"aluno": "Ana", "turma": "7B"}}`.
   - Se `codigo == 404`, retorna `{"status": 404, "erro": "Matricula nao encontrada"}`.
   - Para qualquer outro valor (incluindo `"timeout"`), retorna `{"status": 0, "erro": "Timeout"}` — simula o servico que nao respondeu.
2. Defina `consultar_matricula(codigo)` que:
   - Chama `resposta = simular_api(codigo)`.
   - Le o status com `resposta["status"]`.
   - Se `status == 200`: extrai `dados = resposta["dados"]` e exibe `f"Aluno: {dados['aluno']} | Turma: {dados['turma']}"`.
   - `elif status == 404`: exibe o erro amigavel com `resposta["erro"]`.
   - `else` (status 0): exibe `"Servico indisponivel, tente mais tarde"`.
3. No fluxo principal, chame `consultar_matricula` tres vezes: com `200`, `404` e `"timeout"`.
4. Confira que cada chamada gera a mensagem correta do seu caso.

## Como executar

```bash
cd "91_introducao_http_tratamento"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def simular_api(codigo):
    # Simula as respostas de uma API real, sem depender de rede
    if codigo == 200:
        return {"status": 200, "dados": {"aluno": "Ana", "turma": "7B"}}
    if codigo == 404:
        return {"status": 404, "erro": "Matricula nao encontrada"}
    # Qualquer outro codigo (ex.: "timeout") vira status 0 = sem resposta
    return {"status": 0, "erro": "Timeout"}


def consultar_matricula(codigo):
    resposta = simular_api(codigo)
    status = resposta["status"]

    # Sucesso: exibe os dados retornados pela API
    if status == 200:
        dados = resposta["dados"]
        print(f"Aluno: {dados['aluno']} | Turma: {dados['turma']}")
    # Nao encontrado: mensagem clara para quem consultou
    elif status == 404:
        print(f"Erro: {resposta['erro']}")
    # Status 0 (timeout): servico fora do ar, orienta a tentar depois
    else:
        print("Servico indisponivel, tente mais tarde")


# Testa os tres cenarios: sucesso, nao encontrado e timeout
consultar_matricula(200)
consultar_matricula(404)
consultar_matricula("timeout")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Cliente simulado da API de matriculas da Edutech Brasil."""

from http import HTTPStatus


def simular_api(codigo: int | str) -> dict:
    """Simula respostas da API de matriculas (sem rede)."""
    # match/case cobre cada cenario de forma explicita
    match codigo:
        case 200:
            return {"status": 200, "dados": {"aluno": "Ana", "turma": "7B"}}
        case 404:
            return {"status": 404, "erro": "Matricula nao encontrada"}
        case _:
            # Timeout: convencionamos status 0 para "sem resposta"
            return {"status": 0, "erro": "Timeout"}


def consultar_matricula(codigo: int | str) -> None:
    """Consulta a API simulada e exibe mensagem adequada a cada status."""
    resposta = simular_api(codigo)

    match resposta["status"]:
        # HTTPStatus.OK documenta a intencao melhor que o numero solto
        case HTTPStatus.OK:
            dados = resposta["dados"]
            print(f"Aluno: {dados['aluno']} | Turma: {dados['turma']}")
        case HTTPStatus.NOT_FOUND:
            print(f"Erro: {resposta['erro']}")
        case _:
            print("Servico indisponivel, tente mais tarde")


def main() -> None:
    # Percorre os tres cenarios exigidos pelo enunciado
    for codigo in (200, 404, "timeout"):
        consultar_matricula(codigo)


if __name__ == "__main__":
    main()
```

</details>
