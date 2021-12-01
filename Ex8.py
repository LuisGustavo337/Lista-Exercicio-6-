# Escreva  um  algoritmo que  receba uma  média  (de  zero  a  10)  e  uma  frequência  (de  zero  a 100) de um(a) aluno(a)e:
# a)Se  o  aluno  possuir  frequência  menor  que  75%,  exiba  a  mensagem:  “Você  foi reprovado”; 
# b)Se o aluno possuir frequência maior que 75% e média menor que 7, exiba a mensagem “Você está de recuperação”;
# c)Se  o  aluno  possuir  frequência  maior  que  75%  e  médiamaior  ou  igual  que  7,  exiba  a mensagem “Você foi aprovado”.

med = int(input("digite sua média de notas(0 - 10): "))

freq = int(input("digite a sua frequencia de aulas (0 - 100): "))


if freq < 75:

    print ("Você foi reprovado") 

elif freq > 75 & med > 7:

    print ("Você foi aprovado")
    
if freq > 75 & med < 7:

    print ("Você esta de recuperação")


