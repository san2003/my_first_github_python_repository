
print ("\n \t Que tipo de operação você deseja realizar?")
oper = str (input(" \t Operações disponiveis:  Bhaskara  Operações \n  \t Operação desejada:   "))

if (oper=="bhaskara"):
    a = float (input("\n\t Digite o valor do seu x** aqui :\t"))
    b =  float (input("\t Digite o valor do seu x aqui :\t"))
    c = float(input("\t Digite o valor do seu numero aqui :\t"))
    delta= b**2 -4*a*c
    print ("\t  Seu delta é :", delta)
    x1 = (-b + delta ** (1/2))/2*a
    x2 = (-b - delta ** (1 / 2)) / 2 * a
    print("\t Seu x1 é :  ", x1, "Seu x2 é :  ", x2  )

elif (oper=="operações"):
    n1 = float(input("\n\tDigite seu primeiro numero: "))
    n2 = float(input("\tDigite seu segundo numero: "))
    s = str(input("\tDigite o sinal da equação que você deseja realizar:"))

    if (s == "+"):
        r = n1 + n2
        print("\n\t Seu resultado é: ", r)

    elif (s == "-"):
        r = n1 - n2
        print("\n\t Seu resultado é: ", r)

    elif (s == "/"):
        r = n1 / n2
        print("\n\t Seu resultado é: ", r)

    elif (s == "*"):
        r = n1 * n2
        print("\n\t Seu resultado é: ", r)

    elif (s == "**"):
        r = n1 ** n2
        print("\n\t Seu resultado é: ", r)

    elif (s == "%"):
        r = n1 % n2
        print("\n\t Seu resultado é: ", r)

    else:
        print("\n\t Isso que você digitou não é uma variável valida")

else:
    print ("\t\t A operação desejada não esta disponível!!")
