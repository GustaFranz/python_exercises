"""Script monolitico de referencia — estudar e refatorar em main.py."""

# Cadastro fixo de estoque
itens = [
    {"nome": "Muda de tomate", "qtd": 50},
    {"nome": "Muda de alface", "qtd": 30},
    {"nome": "Substrato", "qtd": 100},
]

print("=== Viveiro Escolar — legado ===")
print("Estoque inicial:")
for item in itens:
    print(f"  {item['nome']}: {item['qtd']}")

# Saida manual simulada
saida_nome = "Muda de tomate"
saida_qtd = 10
for item in itens:
    if item["nome"] == saida_nome:
        if item["qtd"] >= saida_qtd:
            item["qtd"] -= saida_qtd
            print(f"Saida registrada: {saida_nome} -{saida_qtd}")
        else:
            print(f"Estoque insuficiente para {saida_nome}")

# Entrada manual simulada
entrada_nome = "Substrato"
entrada_qtd = 20
for item in itens:
    if item["nome"] == entrada_nome:
        item["qtd"] += entrada_qtd
        print(f"Entrada registrada: {entrada_nome} +{entrada_qtd}")

print("Estoque final:")
for item in itens:
    print(f"  {item['nome']}: {item['qtd']}")
