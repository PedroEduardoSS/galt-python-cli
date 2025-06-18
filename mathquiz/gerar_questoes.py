"""
Esse módulo organiza as operações matemáticas disponíveis para o jogo MathQuiz.
"""

import random
random.seed()

def gerar_questoes(
        num: int,
        ops: str,
        min_val: int | float,
        max_val: int | float,
        decimals: bool = False,
        places: int = 2
    ) -> list:
    """
    Gera uma lista de questões matemáticas baseadas nos parâmetros fornecidos.

    Args:
        num (int): Número de questões a serem geradas.
        ops (str): Operações a serem utilizadas (ex: "+-*/").
        min_val (int ou float): Valor mínimo para os números.
        max_val (int ou float): Valor máximo para os números.
        decimals (bool): Se ausente gera inteiros.
        places (int): Número de casas decimais se decimals for True.

    Returns:
        list: Lista de questões geradas.
    """
    
    questoes = []
    numeros = []
    ops = [op for op in ops if op in "+-*/"]
    if ops == []:
        ops = ['+', '-', '*', '/']

    if decimals:
        numeros = [round(num + random.random(), places) for num in range(int(min_val), int(max_val) + 1)]
        numeros.insert(0, min_val)
        numeros.insert(-1, max_val)
    else:
        numeros = [num for num in range(min_val, max_val + 1)]

    for questao in range(0, num):
        num1, num2 = random.choices(numeros, k=2)
        operation = random.choice(ops)
        questao = f"{num1} {operation} {num2}"
        questoes.append(questao)

    return questoes