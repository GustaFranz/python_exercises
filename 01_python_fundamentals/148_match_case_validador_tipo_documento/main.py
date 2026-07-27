# EXERCICIO 148 - Validador de tipo de documento com match/case (contexto administrativo)
#
# OBJETIVO
# Aplicar match/case para validar tipos de documento em cadastros administrativos.
#
# CONCEITO - MATCH/CASE E EXCECOES CUSTOMIZADAS
## Combinar match/case com excecoes customizadas torna a validacao legivel:
## - case valido: return descricao ou dado processado
## - case _: raise DocumentoInvalidoError("mensagem clara")
## O try/except externo captura apenas a excecao de negocio, sem misturar
## regras de validacao com interface do usuario.
## Alternativas com | simplificam documentos equivalentes:
##   case "RG" | "CNH":
##       return "Documento com foto aceito"
## Padronizacao textual:
##   doc = entrada.strip().upper().replace(".", "").replace("-", "")
## remove formatacao antes de comparar no match.
## SRP aplicado:
## - validar_documento(): apenas match/case e raise
## - programa principal: input, try/except, print e loop
#
# PASSO A PASSO DETALHADO
## Passo 1: Crie DocumentoInvalidoError(Exception).
## Passo 2: Crie validar_documento(tipo) com match/case:
##     def validar_documento(tipo):
##         tipo_limpo = tipo.strip().upper()
##         match tipo_limpo:
##             case "RG":
##                 return "Registro Geral — identidade civil"
##             case "CNH":
##                 return "Carteira de Habilitacao — documento com foto"
##             case "CPF":
##                 return "Cadastro de Pessoa Fisica — numero unico"
##             case "OUTRO":
##                 return "Documento alternativo — requer conferencia manual"
##             case _:
##                 raise DocumentoInvalidoError(
##                     "Tipo invalido. Use RG, CNH, CPF ou OUTRO."
##                 )
## Explicacao:
## - cada case mapeia um tipo de documento permitido no cadastro
## - strip().upper() normaliza a entrada do usuario
## - case _ rejeita qualquer tipo nao previsto na lista
## Passo 3: Loop principal fora da funcao:
##     while True:
##         tipo = input("Tipo de documento (RG/CNH/CPF/OUTRO): ")
##         try:
##             descricao = validar_documento(tipo)
##             print(descricao)
##             break
##         except DocumentoInvalidoError as e:
##             print(f"Erro: {e}")
#
# ENUNCIADO
# Crie um validador de tipo de documento para cadastro na secretaria escolar.
# Tipos aceitos: RG, CNH, CPF, OUTRO.
# O sistema deve:
## solicitar o tipo de documento;
## exibir a descricao do documento aceito;
## recusar tipos invalidos sem encerrar o programa.
#
# ORIENTACOES
## match/case dentro da funcao; try/except fora da funcao.
## Use case _ para tipos nao reconhecidos.
#
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
