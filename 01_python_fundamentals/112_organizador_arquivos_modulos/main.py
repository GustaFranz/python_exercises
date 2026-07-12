# EXERCICIO 112 - Organizador de arquivos por modulos (contexto de produtividade)
#
# ENUNCIADO
# Crie um sistema que simula organizacao de arquivos usando modulos separados para cada tipo de operacao.
# O sistema deve permitir:
## listar arquivos;
## filtrar arquivos por tipo;
## renomear arquivos (simulado).
#
# ORIENTACOES
## Cada funcionalidade deve estar em um modulo separado.
## O main.py deve apenas chamar funcoes.
## Simule arquivos com listas de strings.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import listar
import filtrar
import renomear
import easyansi
easyansi.activate()

tamanhos = [320, 150, 980, 210, 450]


arquivos = [
    "prova.pdf",
    "notas.xlsx",
    "foto.jpg",
    "atividade.docx",
    "grafico.png"
]

listar.listar_arquivos(arquivos)

print(f'//green/Tamanhos dos arquivos:/green //yellow/{tamanhos}/yellow')
print()
filtrar.filtrar_por_tipo(arquivos, ".pdf")

print()

renomear.renomear_arquivo(
    arquivos,
    "foto.jpg",
    "imagem.jpg"
)

print()

listar.listar_arquivos(arquivos)

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Tres modulos: listar, filtrar e renomear
# Lista de strings simula arquivos no disco
# main chama funcoes sem repetir logica
# renomear_arquivo altera a lista em memoria
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
