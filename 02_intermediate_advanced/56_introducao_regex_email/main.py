# DEMANDA
# Empresa: MktEscolar
# Setor: Marketing / comunicacao
# Solicitacao: Validar e-mails de responsaveis antes de enviar campanha.

# EXERCICIO 56 - Introducao a regex e e-mail (contexto corporativo)
#
# VISAO DO BLOCO — Regex com re (exercicios 56 a 60)
# Este bloco treina:
## 56 — Introducao: validar e-mail simples
## 57 — Extrair numeros de um texto
## 58 — Mascarar CPF parcialmente
## 59 — Parsear linhas com separador ;
## 60 — Limpar base de telefones e padronizar
#
# Conceitos basicos:
## import re
## re.search(padrao, texto) encontra primeira ocorrencia
## re.findall(padrao, texto) retorna todas as ocorrencias
## Padroes comuns: \d digitos, \w palavra, + uma ou mais, * zero ou mais
#
# Valide e-mails com padrao simples: texto + @ + texto + . + texto
# Sugestao de padrao: r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
# Teste:
## ana@escola.com -> valido
## ana.escola.com -> invalido
## bruno@mail -> invalido
# Exiba resultado de cada teste (Valido / Invalido).
#
# ORIENTACOES
## import re
## Use re.match ou re.fullmatch com o padrao.
## Funcao validar_email(email) retorna bool.

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
