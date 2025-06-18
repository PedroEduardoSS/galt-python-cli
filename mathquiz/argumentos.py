"""
Esse módulo define os argumentos de linha de comando para o jogo MathQuiz.
Ele utiliza a biblioteca argparse para facilitar a criação e o gerenciamento dos argumentos.
"""

import argparse

def get_parser() -> argparse.ArgumentParser:
    """
    Cria e retorna um objeto ArgumentParser configurado com os argumentos necessários para o jogo MathQuiz.
    
    Returns:
        argparse.ArgumentParser: O objeto ArgumentParser configurado.
    """
    class CustomArgumentParser(argparse.ArgumentParser):
        def error(self, message):
            print(f"\nErro nos argumentos: {message}\n")
            self.print_help()
            exit(2)
    
    # Criação do parser
    parser = CustomArgumentParser(description="MathQuiz - Um quiz de perguntas de matemática.")
    parser.add_argument(
        "--num",
        type=int,
        help="Número de questões",
        default=10
    )

    parser.add_argument(
        "--ops",
        type=str,
        help="Lista de operações a serem utilizadas no quiz entre dois sinas de igual '=' (ex: =+-*/=)",
        default="=+-*/="
    )

    parser.add_argument(
        "--min",
        help="Valor mínimo para os números",
        default=1
    )

    parser.add_argument(
        "--max",
        help="Valor máximo para os números",
        default=10
    )

    parser.add_argument(
        "--decimals",
        action="store_true",
        help="Se ausente, responda apenas com inteiros"
    )

    parser.add_argument(
        "--places",
        type=int,
        help="Número de casas decimais",
        default=2
    )

    return parser