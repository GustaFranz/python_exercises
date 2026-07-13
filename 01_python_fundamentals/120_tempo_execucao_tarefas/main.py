# EXERCICIO 120 - Tempo de execucao de tarefas (contexto de produtividade)
#
# ENUNCIADO
# Um programador deseja medir o tempo de execucao de diferentes tarefas.
# O sistema deve:
## executar funcoes simuladas;
## medir o tempo de execucao de cada uma;
## exibir ranking das tarefas mais rapidas.
#
# ORIENTACOES
## Utilize time.
## Use time.perf_counter().
## Simule funcoes com sleep.
## Organize resultados em lista ou dicionario.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

def medir_tempo_execucao(funcao, *args, **kwargs):
    """Mede o tempo de execucao de uma funcao"""
    import time
    inicio = time.perf_counter()
    resultado = funcao(*args, **kwargs)
    fim = time.perf_counter()
    tempo_execucao = fim - inicio
    return tempo_execucao, resultado

def tarefa_simulada_1():
    """Simula uma tarefa com tempo de execucao de 1 segundo"""
    import time
    time.sleep(1)
    return "Tarefa 1 concluida"

def tarefa_simulada_2():
    """Simula uma tarefa com tempo de execucao de 2 segundos"""
    import time
    time.sleep(2)
    return "Tarefa 2 concluida" 

def tarefa_simulada_3():
    """Simula uma tarefa com tempo de execucao de 0.5 segundos"""
    import time
    time.sleep(0.5)
    return "Tarefa 3 concluida"

def main():
    tarefas = [
        ("Tarefa 1", tarefa_simulada_1),
        ("Tarefa 2", tarefa_simulada_2),
        ("Tarefa 3", tarefa_simulada_3)
    ]


    resultados = []
    for nome, funcao in tarefas:
        tempo, resultado = medir_tempo_execucao(funcao)
        resultados.append((nome, tempo, resultado))

    # Ordena resultados pelo tempo de execucao
    resultados.sort(key=lambda x: x[1])

    print(f"//magenta/===============================================================")
    print(f"     //blue/TEMPO DE EXECUCAO DE TAREFAS - RANKING")
    print(f"//magenta/===============================================================")
    for nome, tempo, resultado in resultados:
        print(f"//green/{nome}: //yellow/{tempo:.4f} //green/segundos - //red/{resultado}")
    print(f"\n//magenta/==============================================================//magenta/\n")


if __name__ == "__main__":
    main()



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro contato com time.perf_counter()
# Funcao medidora recebe outra funcao como parametro
# Ranking com sort(key=lambda) pelo tempo gasto
# Interessante demais essas funcionalidades para medir desempenho de tarefas simuladas
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
