# EXERCICIO 06 - Pathlib: criar pastas e gravar arquivo
#
# DEMANDA
# Criar pasta de relatorios e salvar um arquivo de resumo.
#
# TAREFAS
# 1. pasta_projeto = Path(__file__).resolve().parent
# 2. pasta_relatorios = pasta_projeto / "saidas" / "relatorios"
# 3. pasta_relatorios.mkdir(parents=True, exist_ok=True)
# 4. caminho = pasta_relatorios / "resumo.txt"
# 5. caminho.write_text("Relatorio gerado com sucesso.", encoding="utf-8")
# 6. Imprima f"Relatorio salvo em: {caminho}"
#
# CONCEITOS: mkdir(), write_text()
#
# --- Implemente sua solucao abaixo ---
