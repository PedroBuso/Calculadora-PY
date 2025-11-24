while True:
    # Entrada do primeiro número
    num1 = float(input("Digite o primeiro número:\t"))

    # Exibição do menu de operações
    print("\nEscolha a operação:")
    print(" 1. Soma")
    print(" 2. Subtração")
    print(" 3. Multiplicação")
    print(" 4. Divisão")
    print(" 5. Sair")

    # Entrada da operação
    operacao = int(input("Digite o número da operação (1 a 5):\t"))

    if operacao == 5:
        print("Encerrando o programa. Até mais!")
        break  # Sai do loop e finaliza o programa

    # Entrada do segundo número
    num2 = float(input("Digite o segundo número:\t"))

    # Verificação da operação e cálculo
    if operacao == 1:
        resultado = num1 + num2
        print("Resultado da soma:", resultado)
    elif operacao == 2:
        resultado = num1 - num2
        print("Resultado da subtração:", resultado)
    elif operacao == 3:
        resultado = num1 * num2
        print("Resultado da multiplicação:", resultado)
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado da divisão:", resultado)
        else:
            print("Erro: divisão por zero!")
    else:
        print("Operação inválida.")

    print("\n" + "-"*30 + "\n")  # Linha de separação entre execuções
