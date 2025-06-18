import pytest

def avaliar_resposta(questao, resposta, decimals=False, places=2):
    """Função auxiliar para simular a avaliação de uma resposta."""
    if decimals:
        gabarito = round(float(eval(questao)), places)
        try:
            resposta = round(float(resposta), places)
        except Exception:
            return False
        return gabarito == resposta
    else:
        gabarito = int(eval(questao))
        try:
            resposta = int(float(resposta))
        except Exception:
            return False
        return gabarito == resposta

@pytest.mark.parametrize("questao,resposta,esperado", [
    ("2 + 2", "4", True),
    ("5 - 3", "2", True),
    ("7 * 2", "15", False),
    ("10 / 2", "5", True),
    ("3 + 5", "oito", False),  # resposta inválida
    ("4 * 2", "", False),      # resposta vazia
])
def test_avaliacao_inteiros(questao, resposta, esperado):
    assert avaliar_resposta(questao, resposta) == esperado

@pytest.mark.parametrize("questao,resposta,esperado", [
    ("2.5 + 2.5", "5.00", True),
    ("1.1 + 2.2", "3.3", True),
    ("3.3 - 1.1", "2.1", False),  # erro proposital
    ("2.5 * 2", "5.0", True),
    ("5.0 / 2", "2.5", True),
    ("1.5 + 1.5", "três", False),  # resposta inválida
    ("2.0 + 2.0", "", False),      # resposta vazia
])
def test_avaliacao_decimais(questao, resposta, esperado):
    assert avaliar_resposta(questao, resposta, decimals=True, places=2) == esperado