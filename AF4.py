#1) Escreva um Algoritmo que leia um número e o imprima caso ele seja maior que 20
#2) Construa um Algoritmo que leia dois valores numéricos inteiros e efetue a adição; caso o
#resultado seja maior que 10, apresentá-lo
#3) Construa um Algoritmo que determine (imprima) se um dado número N inteiro (recebido
#por meio do teclado) é PAR OU IMPAR
#4) Escreva um Algoritmo para determinar se um dado número N (recebido por meio do
#teclado) é POSITIVO, NEGATIVO ou NULO
#5) Escreva um Algoritmo que leia um número e imprima a raiz quadrada do número caso ele
#seja positivo ou igual a zero e o quadrado do número caso ele seja negativo
#6) Escreva um Algoritmo que leia um número e informe se ele é ou não divisível por 5
#7) Construir um Algoritmo que leia um número e imprima se ele é igual a 5, a 200, a 400, se
#esta no intervalo entre 500 e 1000, inclusive, ou se ela está fora dos escopos anteriores
import numpy as np

escolha = int(input("Escolha a atividade (1-7):"))
if(escolha>7 or escolha<1):
    exit("Atividade não existente")
else:

    if(escolha==1):
        numeroum = int(input("Digite um numero inteiro qualquer:"))
        if(numeroum>20):
            print(numeroum,"É MAIOR QUE 20")

    if(escolha==2):
        numeroum = int(input("Digite um numero inteiro qualquer:"))
        numerodois = int(input("Digite outro numero inteiro qualquer:"))
        numeroSoma = numeroum + numerodois
        if(numeroSoma>10):
            print(numeroSoma,"É MAIOR QUE 10")

    if(escolha==3):
        numeroum = int(input("Digite um numero inteiro qualquer:"))
        if((numeroum%2) != 0):
            print(numeroum,"É IMPAR")
        else:
            print(numeroum,"É PAR")

    if(escolha==4):
        numeroum = int(input("Digite um numero inteiro qualquer (negativo ou positivo):"))
        if(numeroum > 0):
            print(numeroum,"É POSITIVO")
        else:
            print(numeroum,"É NEGATIVO")
        if(numeroum==0):
            print(numeroum,"É NULO")

    if(escolha==5):
        numeroum = int(input("Digite um numero inteiro qualquer:"))
        if(numeroum>=0):
            print("A RAIZ DE",numeroum,"É:",np.sqrt(numeroum))
        else:
            print("O QUADRADO DE",numeroum,"É:",numeroum**2)
            
    if(escolha==6):
        numeroum = int(input("Digite um numero inteiro qualquer:"))
        if((numeroum%5) == 0):
            print(numeroum,"É DIVISIVEL POR 5")

    if(escolha==7):
        numeroum = int(input("Digite um numero inteiro qualquer:"))
        if(numeroum==5):
            print("É igual a 5")
        else:
            if(numeroum==20):
                print("É igual a 20")
            else:
                if(numeroum==400):
                    print("É igual a 400")
        if(numeroum>500 and numeroum<1000):
            print("Ta entre 500 e 1000")
        else:
            print("Não ta entre 500 e 1000")