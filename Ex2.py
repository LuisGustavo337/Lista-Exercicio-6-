#Escreva um algoritmo que leia dois números inteiros e exiba a multiplicação entre eles seo primeiro número for par; 
# caso contrário, exiba a soma dos números. 

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if (num1 % 2 == 0):
    mult = num1 * num2
    print("A multiplicação é ",mult)
else:
    soma = num1 + num2
    print("A soma é ",soma)