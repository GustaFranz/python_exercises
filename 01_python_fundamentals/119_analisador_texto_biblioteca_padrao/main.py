# EXERCICIO 119 - Analisador de texto com biblioteca padrao (contexto de linguagem)
#
# ENUNCIADO
# Um sistema deve analisar uma frase e gerar estatisticas basicas.
# frase = "Python e uma linguagem poderosa para ciencia de dados"
# O programa deve:
## contar palavras;
## contar caracteres;
## identificar palavras unicas;
## converter texto para caixa alta e baixa.
#
# ORIENTACOES
## Utilize bibliotecas padrao como string (collections e opcional).
## Use split(), len(), set().
## Organize resultados em dicionario.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

frase = "Python e uma linguagem poderosa para ciencia de dados"
analisar_frase = frase.split()
num_palavras = len(analisar_frase)
num_caracteres = len(frase)
palavras_unicas = set(analisar_frase)
frase_upper = frase.upper()
frase_lower = frase.lower() 

print(f"//bold-magenta/===================== //bold-blue/ANALISADOR DE TEXTO //bold-magenta/=====================\n")
print(f"//green/Frase analisada: //underline-yellow/{frase}\n")
print(f"//green/Numero de palavras: //yellow/{num_palavras}/yellow")
print(f"//green/Numero de caracteres: //yellow/{num_caracteres}/yellow")
print(f"//green/Palavras unicas: //yellow/{', '.join(palavras_unicas)}/yellow")
print(f"//green/Frase em caixa alta: //yellow/{frase_upper}/yellow")
print(f"//green/Frase em caixa baixa: //yellow/{frase_lower}/yellow")
print(f"\n//bold-magenta/==============================================================//bold-magenta/\n")

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Analise de texto so com biblioteca padrao
# set() revela palavras unicas sem loop manual
# upper() e lower() padronizam caixa do texto
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
