# EXERCICIO 114 - Analise de vendas com modulos (contexto de comercio)
#
# ENUNCIADO
# Crie um sistema dividido em modulos para analise de vendas.
# vendas = [120, 340, 89, 560, 230, 410]
# O sistema deve calcular:
## total de vendas;
## media;
## maior venda;
## menor venda.
#
# ORIENTACOES
## Cada calculo deve estar em um modulo separado.
## main.py apenas importa e exibe resultados.
## Mantenha funcoes puras (apenas return).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
from min import obter_minimo
from max import obter_maximo
from soma import obter_soma
from media import obter_media
from total_vendas import total_vendas
import easyansi
easyansi.activate()


vendas = [120, 340, 89, 560, 230, 410]

def main():
    print(f'\n//green/------------------ RELATÓRIO DE VENDAS ------------------/green \n')
    print(f'//green/Total de vendas:/green '
          f'//yellow/{total_vendas(vendas)}/yellow')
    print(f'//green/Media de vendas:/green '    
          f'//yellow/{obter_media(vendas)}/yellow')
    print(f'//green/Maior venda:/green '
          f'//yellow/{obter_maximo(vendas)}/yellow')
    print(f'//green/Menor venda:/green '
          f'//yellow/{obter_minimo(vendas)}/yellow')
    print(f'//green/Soma de vendas:/green '
          f'//yellow/{obter_soma(vendas)}/yellow')
    print(f'//green/Vendas:/green '
          f'//yellow/{vendas}/yellow\n')

if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# from min import obter_minimo: import direto da funcao
# Cada calculo de vendas em modulo separado
# Funcoes puras com return, sem alterar a lista
# Animado em montar relatorio so importando modulos
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
