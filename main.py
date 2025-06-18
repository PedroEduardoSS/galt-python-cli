from mathquiz import get_parser, gerar_relatorio, gerar_questoes
import time

def main():
    """
    Função principal do MathQuiz.
    Inicia o programa, processa os argumentos de linha de comando e executa o loop
    de questões.
    O usuário deve respoder a cada questão e o programa irá validar as respostas.
    """
    parser = get_parser()
    args = parser.parse_args()
    
    loop = True

    num_acertos = 0
    num_erros = 0
    
    while loop:
        if args.decimals:
            questoes = gerar_questoes(
                int(args.num),
                str(args.ops),
                float(args.min),
                float(args.max),
                args.decimals,
                args.places
            )
            tempo_inicio = time.time()
            
            for questao in questoes:
                print(f"Questão: {questao}")
                gabarito = round(float(eval(questao)), int(args.places))
                try:
                    resposta = round(float(input("Resposta: ")), int(args.places))
                except:
                    print("Tipo da resposta inválida e será considerado um erro", end="\n\n")
                    num_erros += 1
                    continue

                if gabarito == float(resposta):
                    print("Certo", end="\n\n")
                    num_acertos += 1
                else:
                    print(f"Errado. A resposta é: {gabarito}", end="\n\n")
                    num_erros += 1
            
            tempo_fim = time.time()

            duracao = tempo_fim - tempo_inicio
            relatorio = gerar_relatorio(args.num, num_acertos, num_erros, duracao)
            print(relatorio)
            loop = False

        else:
            questoes = gerar_questoes(
                int(args.num),
                str(args.ops),
                int(args.min),
                int(args.max)
            )
            tempo_inicio = time.time()
            
            for questao in questoes:
                print(f"Questão: {questao}")
                gabarito = int(eval(questao))

                try:
                    resposta = float(input("Resposta: "))
                except:
                    print("Tipo da resposta inválida e será considerado um erro", end="\n\n")
                    num_erros += 1
                    continue

                if gabarito == int(resposta):
                    print("Certo", end="\n\n")
                    num_acertos += 1
                else:
                    print(f"Errado. A resposta é: {gabarito}", end="\n\n")
                    num_erros += 1
            
            tempo_fim = time.time()

            duracao = tempo_fim - tempo_inicio
            relatorio = gerar_relatorio(args.num, num_acertos, num_erros, duracao)
            print(relatorio)
            loop = False


if __name__ == "__main__":
    main()