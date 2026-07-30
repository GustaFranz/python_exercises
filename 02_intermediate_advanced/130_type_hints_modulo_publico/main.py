# DEMANDA
# Empresa: FinEdu Carteira
# Setor: Financeiro educacional
# Solicitacao: Expor modulo de calculo de mensalidades com hints, docstrings e estrutura de retorno tipada.

# EXERCICIO 130 - Type hints: modulo publico tipado (nivel entrevista junior)
#
# Em mensalidades.py implemente API publica:
## calcular_desconto(valor: float, percentual: float) -> float
## somar_valores(valores: List[float]) -> float
## resumo_mensalidades(alunos: List[Dict[str, float]]) -> Dict[str, float]
##   cada dict de aluno: {"nome": str, "valor": float}  # hint no docstring
##   retorno: {"total": ..., "media": ..., "maior": ..., "menor": ...}
#
# Dados de exemplo para main.py:
## [
##   {"nome": "Ana", "valor": 850.0},
##   {"nome": "Bruno", "valor": 920.0},
##   {"nome": "Carla", "valor": 780.0},
## ]
#
# main.py:
## import mensalidades
## aplique desconto de 5% em cada valor (opcional)
## chame resumo_mensalidades e exiba resultado formatado
#
# ORIENTACOES
## Use from typing import List, Dict, Optional.
## Toda funcao publica: hints + docstring (Args / Returns).
## main.py apenas orquestra — logica fica em mensalidades.py.
## Pergunta de entrevista: por que tipar retorno de resumo_mensalidades?

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
