# DEMANDA
# Empresa: MonitoraTI
# Setor: Infraestrutura / suporte
# Solicitacao: Ler arquivo de log de servidor sem esquecer de fechar o arquivo.

# EXERCICIO 41 - Introducao ao with open (contexto corporativo)
#
# VISAO DO BLOCO — Context manager with open (exercicios 41 a 45)
# Este bloco treina:
## 41 — Introducao: ler log com with open
## 42 — Escrever arquivo de texto
## 43 — Append seguro em arquivo existente
## 44 — Copiar conteudo entre dois arquivos
## 45 — Ler arquivo grande em blocos (chunks)
#
# Conceitos basicos:
## with open(caminho, modo) as arquivo: fecha automaticamente
## Modos comuns: "r" leitura, "w" escrita, "a" append, encoding="utf-8"
## Evita vazamento de handle e erros se o programa interromper
## Preferir with em vez de open() + close() manual
#
# Crie o arquivo servidor.log com 4 linhas de exemplo no inicio do script:
## [INFO] Servidor iniciado
## [INFO] Conexao aceita
## [WARN] Memoria em 80%
## [INFO] Backup concluido
# Leia todo o conteudo com with open(..., "r", encoding="utf-8").
# Exiba o conteudo na tela e a quantidade de linhas lidas.
#
# ORIENTACOES
## Use with open("servidor.log", "r", encoding="utf-8") as f:
## Leia com .read() ou .readlines() e conte as linhas.
## Nao chame .close() manualmente — o with faz isso.
## Crie o arquivo antes de ler (modo "w") se ele nao existir.

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
