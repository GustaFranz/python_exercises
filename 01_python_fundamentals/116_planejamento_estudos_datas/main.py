# EXERCICIO 116 - Planejamento de estudos com datas (contexto educacional)
#
# ENUNCIADO
# Um aluno deseja organizar seu cronograma de estudos ate a data de uma prova.
# data_prova = "2026-02-15"
# O programa deve:
## calcular dias restantes ate a prova;
## sugerir revisoes semanais;
## exibir datas importantes do cronograma.
#
# ORIENTACOES
## Utilize a biblioteca datetime.
## Converta strings em datas.
## Use timedelta para calculos.
## Gere uma lista de datas de revisao.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

from datetime import datetime, timedelta

import easyansi

easyansi.activate()


def calcular_dias_restantes(data_prova):
    hoje = datetime.now().date()
    data_prova = datetime.strptime(data_prova, "%Y-%m-%d").date()
    dias_restantes = (data_prova - hoje).days
    return dias_restantes, data_prova


def sugerir_revisoes(data_prova, dias_restantes):
    """Gera cronograma estratégico de revisões"""
    revisoes = []
    hoje = datetime.now().date()

    # Cronograma inteligente baseado em dias restantes
    if dias_restantes > 0:
        # 1ª revisão: em 1 semana
        if dias_restantes >= 7:
            revisoes.append(("1ª Revisão (conceitos)", hoje + timedelta(days=7)))

        # 2ª revisão: em 2 semanas
        if dias_restantes >= 14:
            revisoes.append(("2ª Revisão (aprofundamento)", hoje + timedelta(days=14)))

        # 3ª revisão: 1 mês antes
        if dias_restantes >= 30:
            revisoes.append(("3ª Revisão (prática)", data_prova - timedelta(days=30)))

        # 4ª revisão: 1 semana antes
        if dias_restantes >= 7:
            revisoes.append(("4ª Revisão (final)", data_prova - timedelta(days=7)))

        # Última revisão: 2 dias antes
        if dias_restantes >= 2:
            revisoes.append(("Revisão de véspera", data_prova - timedelta(days=2)))

    return revisoes


def main():
    data_prova = "2026-12-10"  # Data realista (futura)
    dias_restantes, data_prova_obj = calcular_dias_restantes(data_prova)
    revisoes = sugerir_revisoes(data_prova_obj, dias_restantes)

    print(f"//magenta/=============/magenta 📅 Data da prova: {data_prova_obj.strftime('%d/%m/%Y')} //magenta/============/magenta")
    print(f"⏰ Dias restantes: //yellow/{dias_restantes}/yellow dias\n")

    if dias_restantes > 0:
        print("📋 //blue/Cronograma de Revisões:/blue")
        print("-" * 50)
        for descricao, data_revisao in revisoes:
            dias_ate = (data_revisao - datetime.now().date()).days
            print(f"{descricao}:")
            print(f"   //green/Data: {data_revisao.strftime('%d/%m/%Y')}/green (//yellow/{dias_ate}/yellow dias a partir de hoje)")
    else:
        print("⚠️  A data da prova já passou!")


if __name__ == "__main__":
    main()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Voltando a ter contato com biblioteca datetime desde o início dos estudos. Estudando muito pra ficar bom nisso!
# strptime converte string em data; timedelta soma dias
# Cronograma de revisoes com datas calculadas
# Animado para desenvolver projetos com planejamento de prova com calendario real 
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
