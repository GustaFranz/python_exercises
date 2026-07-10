# DEMANDA
# Empresa: BigData Escolar
# Setor: Educacao / analytics
# Solicitacao: Script de linha de comando para processar exportacao de notas com parametros.

# EXERCICIO 76 - Introducao ao argparse (contexto corporativo)
#
# VISAO DO BLOCO — argparse (exercicios 76 a 80)
# Este bloco treina:
## 76 — Introducao: --arquivo e --limite
## 77 — Flags booleanas (--verbose, --dry-run)
## 78 — Subcomando simples (listar / exportar)
## 79 — CLI para gerar relatorio de notas
## 80 — Ferramenta com 3 operacoes integradas
#
# Conceitos basicos:
## import argparse
## parser = argparse.ArgumentParser(description="...")
## parser.add_argument("--arquivo", required=True)
## args = parser.parse_args()
## Rode com: python main.py --arquivo dados.csv --limite 10
#
# Crie CLI com argparse:
## --arquivo (str, obrigatorio): caminho do arquivo de entrada
## --limite (int, padrao 10): maximo de linhas a processar
# Ao executar, exiba:
## Arquivo: {args.arquivo}
## Limite: {args.limite}
# Teste mentalmente: python main.py --arquivo notas.csv --limite 5
#
# ORIENTACOES
## if __name__ == "__main__": chame funcao main() ou monte parser ali.
## parser.add_argument("--limite", type=int, default=10)

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
