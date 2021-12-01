#Escreva um algoritmo que receba o primeiro termo e a razão de uma PG. 
#No final mostre os 5 primeiros termos dessa progressão.

print("PROGREÇÃO GEOMETRICA")
numero= int(input("digite o primeiro termo: "))
razao= int(input("digite a razão: "))

for i in range(1,6):
    print("a",i,"....",numero)
    numero = numero * razao