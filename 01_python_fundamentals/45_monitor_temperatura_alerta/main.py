# EXERCICIO 45 - Monitor de temperatura com alerta
#
# ENUNCIADO
# Um sistema monitora temperaturas de uma máquina.
# O programa deve:
## receber temperaturas continuamente;
## exibir se está normal ou crítica;
## parar quando a temperatura for menor que 0 (falha no sensor).
#
# ORIENTACOES
## Use while
## Use condição dentro do loop
## Classifique:
## até 70 = normal
## acima de 70 = crítico
## Temperatura negativa encerra o sistema
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

import easyansi
easyansi.activate()

print("=" * 70)
print("//bold-cyan/MONITOR DE TEMPERATURA/bold-cyan")
print("=" * 70)

while True:
    temperatura = float(input("Temperatura registrada: ").replace(",", "."))

    if temperatura > 70:
        print(f"//bold-red/Sistema em estado crítico!/bold-red Temperatura: //red/{temperatura} ºC/red")

    elif 0 <= temperatura <= 70:
        print(f"//bold-green/Sistema em equilíbrio./bold-green Temperatura: //green/{temperatura} ºC/green")

    else:
        print("//bold-yellow/Sistema em desequilíbrio. Falha no sensor!/bold-yellow")
        print("//bold-red/Monitoramento encerrado./bold-red")
        break










# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================
# 
# Durante o desenvolvimento deste exercício, tive a oportunidade de:
# 
# Relembrar a utilização do laço de repetição while True para manter um sistema em execução contínua até que uma condição de parada seja atendida.
# Consolidar a aplicação da estrutura condicional if / elif / else para classificar diferentes estados de um sistema.
# Relembrar o uso do comando break para encerrar a execução do laço de forma controlada quando ocorre uma condição específica.
# Consolidar a construção de condições compostas, utilizando comparações como 0 <= temperatura <= 70 para tornar o código mais legível e preciso.
# Relembrar o tratamento de entradas numéricas por meio do método .replace(',', '.'), permitindo que o usuário informe valores utilizando vírgula ou ponto decimal.
# Relembrar a utilização da biblioteca EasyANSI para melhorar a apresentação das mensagens no terminal, tornando a saída do programa mais organizada e intuitiva.

# 🔗 Link do repositório da biblioteca EasyAnsi:
# https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
