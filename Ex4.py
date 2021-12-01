#Escreva um algoritmo para imprimir na tela a tabuada de um número informado pelo usuário

tab = int(input("Digite um número: "))

x = 1
while x <= 10:
    tabuada = tab * x
    print(tab,"x",x, "=",tabuada)
    x = x + 1 