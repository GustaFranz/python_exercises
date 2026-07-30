"""Script monolitico de referencia — estudar e refatorar em main.py."""

# === Viveiro Escolar — controle de estoque (legado) ===
# Cadastro fixo — mistura dados, regras e impressao no mesmo fluxo

itens = [
    {"nome": "Muda de tomate", "qtd": 50, "minimo": 10},
    {"nome": "Muda de alface", "qtd": 30, "minimo": 10},
    {"nome": "Substrato", "qtd": 100, "minimo": 20},
    {"nome": "Adubo organico", "qtd": 8, "minimo": 10},
]

movimentos = [
    {"tipo": "saida", "nome": "Muda de tomate", "qtd": 10},
    {"tipo": "saida", "nome": "Muda de pepino", "qtd": 5},
    {"tipo": "entrada", "nome": "Substrato", "qtd": 20},
    {"tipo": "saida", "nome": "Adubo organico", "qtd": 3},
    {"tipo": "entrada", "nome": "Muda de alface", "qtd": 15},
    {"tipo": "saida", "nome": "Muda de alface", "qtd": 40},
]

print("=== Viveiro Escolar — legado ===")
print("Estoque inicial:")
for item in itens:
    print(f"  {item['nome']}: {item['qtd']} un (min: {item['minimo']})")

alertas = []
erros = []
total_saidas = 0
total_entradas = 0

for mov in movimentos:
    tipo = mov["tipo"]
    nome = mov["nome"]
    qtd = mov["qtd"]

    if qtd <= 0:
        erros.append(f"Movimento invalido: {tipo} {nome} qtd={qtd}")
        continue

    encontrou = False
    for item in itens:
        if item["nome"] == nome:
            encontrou = True
            if tipo == "saida":
                if item["qtd"] >= qtd:
                    item["qtd"] -= qtd
                    total_saidas += qtd
                    print(f"Saida registrada: {nome} -{qtd}")
                else:
                    msg = f"Estoque insuficiente para {nome} (disp: {item['qtd']}, pedido: {qtd})"
                    erros.append(msg)
                    print(msg)
            elif tipo == "entrada":
                item["qtd"] += qtd
                total_entradas += qtd
                print(f"Entrada registrada: {nome} +{qtd}")
            else:
                erros.append(f"Tipo desconhecido: {tipo}")
            break

    if not encontrou:
        msg = f"Item nao encontrado: {nome}"
        erros.append(msg)
        print(msg)

for item in itens:
    if item["qtd"] < item["minimo"]:
        alertas.append(f"{item['nome']} abaixo do minimo ({item['qtd']}/{item['minimo']})")

print("\n--- Resumo de movimentacoes ---")
print(f"Total entradas: +{total_entradas}")
print(f"Total saidas: -{total_saidas}")

if erros:
    print("\nErros registrados:")
    for e in erros:
        print(f"  ! {e}")

if alertas:
    print("\nAlertas de estoque baixo:")
    for a in alertas:
        print(f"  * {a}")
else:
    print("\nNenhum alerta de estoque baixo.")

print("\nEstoque final:")
for item in itens:
    status = "OK" if item["qtd"] >= item["minimo"] else "BAIXO"
    print(f"  {item['nome']}: {item['qtd']} [{status}]")

print("\nFim do script legado.")
