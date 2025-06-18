"""
Esse módulo gera relatórios de desempenho do jogo MathQuiz.
Ele contará as questões respondidas corretamente e incorretamente,
calculará a porcentagem de acertos e tempo médio por questão.
"""

import time

def gerar_relatorio(
        num_questoes: int,
        num_acertos: int,
        num_erros: int,
        duracao: int
    ) -> str:
    """
    Gera um relatório de desempenho do jogo MathQuiz.

    Returns:
        str: Relatório formatado com o desempenho do jogador.
    """
    porcentagem_acertos = (num_acertos / num_questoes) * 100 if num_questoes > 0 else 0
    tempo_medio = duracao / num_questoes if num_questoes > 0 else 0
    
    relatorio = (
        f"Relatório de Desempenho do MathQuiz\n"
        f"-------------------------------\n"
        f"Total de questões: {num_questoes}\n"
        f"Acertos: {num_acertos}\n"
        f"Erros: {num_erros}\n"
        f"Porcentagem de acertos: {porcentagem_acertos:.2f}%\n"
        f"Duração total: {time.strftime("%H:%M:%S", time.gmtime(duracao))}\n"
        f"Tempo médio por questão: {time.strftime("%H:%M:%S", time.gmtime(tempo_medio))}\n"
    )

    return relatorio