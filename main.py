def calculadora():
    try:
        escolha = int(input(f" {nome}, escolha uma operação "))

        if escolha == 1:
            a = float(input("Digite o valor que quer somar\n ==> "))
            b = float(input("Digite o outro valor \n ==> "))
            resultado = a + b
            print("O Resultado é \n ==>", resultado)

        elif escolha == 2:
            a = float(input("Digite o valor que quer subratrair\n ==> "))
            b = float(input("Digite o outro valor\n ==> "))
            resultado = a - b
            print("O Resultado é \n ==>", resultado)

        elif escolha == 3:
            a = float(input("Digite o valor que quer multiplicar\n ==> "))
            b = float(input("Digite o outro valor\n ==> "))
            resultado = a * b
            print("O Resultado é \n ==>", resultado)

        elif escolha == 4:
            a = float(input("Digite o valor que quer dividir\n ==> "))
            b = float(input("Digite o outro valor\n ==> "))
            resultado = a / b
            print("O Resultado é \n ==>", resultado)

    except ValueError:
        print("Escolha um numero")
        pass

nome = input("Qual o seu nome ? \n ==> ")

while True:
    try:
        opcoes = int(input(f"{nome} Escolha um desses algoritmo : \n Calculadora: 1 \n Sair: 2 \n ==> "))

        if opcoes == 1:
            calculadora()

        elif opcoes == 2:
            break

    except ValueError:
        print("Escolha um numero")
        pass