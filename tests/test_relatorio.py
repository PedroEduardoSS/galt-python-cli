"""
Esse módulo testa cenários da função de gerar relatório do módulo gerar_relatorio.py.
Cenários:
    1 - Formatação do relatório gerado
    2 - Relatorio com duração em minutos
    3 - Relatorio com duração em horas
"""

from mathquiz import gerar_relatorio

def test_gerar_relatorio_formatacao():
    num_questoes = 5
    num_acertos = 3
    num_erros = 2
    duracao = 50  # segundos

    relatorio = gerar_relatorio(num_questoes, num_acertos, num_erros, duracao)
    assert "Relatório de Desempenho do MathQuiz" in relatorio
    assert "Total de questões: 5" in relatorio
    assert "Acertos: 3" in relatorio
    assert "Erros: 2" in relatorio
    assert "Porcentagem de acertos: 60.00%" in relatorio
    assert "Duração total: 00:00:50" in relatorio
    assert "Tempo médio por questão: 00:00:10" in relatorio

def test_gerar_relatorio_duracao_minutos():
    relatorio = gerar_relatorio(4, 2, 2, 125)  # 2m05s total, 31s por questão
    assert "Duração total: 00:02:05" in relatorio
    assert "Tempo médio por questão: 00:00:31" in relatorio

def test_gerar_relatorio_duracao_horas():
    relatorio = gerar_relatorio(2, 1, 1, 3661)  # 1h1s total, 30m30s por questão
    assert "Duração total: 01:01:01" in relatorio
    assert "Tempo médio por questão: 00:30:30" in relatorio