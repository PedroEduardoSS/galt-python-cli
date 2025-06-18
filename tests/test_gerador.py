"""
Esse módulo testa cenários da função de gerar questões do módulo gerar_questoes.py.
Cenários:
    1 - Gerar questoes com inteiros
    2 - Gerar questoes com decimais
    3 - Gerar questoes com operacoes múltiplas
    4 - Gerar questoes com operacoes limitadas
    5 - Gerar questoes com operacoes inválidas
"""

from mathquiz import gerar_questoes

def test_gerar_questoes_inteiros_basico():
    questoes = gerar_questoes(5, "+-", 1, 10)
    assert len(questoes) == 5
    for q in questoes:
        assert any(op in q for op in "+-")
        partes = q.split()
        assert len(partes) == 3
        num1, op, num2 = partes
        assert op in "+-"
        assert 1 <= int(float(num1)) <= 10
        assert 1 <= int(float(num2)) <= 10

def test_gerar_questoes_decimais():
    questoes = gerar_questoes(3, "=+-=", 1.0, 2.0, decimals=True, places=3)
    assert len(questoes) == 3
    for q in questoes:
        partes = q.split()
        num1, op, num2 = partes
        assert op in "+-"
        # Testa se tem casas decimais
        assert "." in num1 and "." in num2
        assert len(num1.split(".")[1]) <= 3
        assert len(num2.split(".")[1]) <= 3

def test_gerar_questoes_operacoes_multiplas():
    questoes = gerar_questoes(10, "=+-*/=", 1, 5)
    assert len(questoes) == 10
    for q in questoes:
        partes = q.split()
        assert len(partes) == 3
        num1, op, num2 = partes
        assert op in "+-*/"

def test_gerar_questoes_limites():
    questoes = gerar_questoes(2, "=+=", 7, 7)
    assert len(questoes) == 2
    for q in questoes:
        partes = q.split()
        num1, op, num2 = partes
        assert num1 == "7"
        assert num2 == "7"
        assert op == "+"

def test_gerar_questoes_sem_operacoes_validas():
    questoes = gerar_questoes(3, "xyz", 1, 5)
    assert questoes != []
    # Se as operações não forem válidas o programa irá corrigir com os valores padrões