"""
Exercício 8:  Escreva um programa que leia um número inteiro e mostre o seu quadrado e seu
cubo. Por exemplo, se o número de entrada é 3, a saída deve ser 9 e 27. Faça a
simulação passo a passo da execução do programa.
"""

# Entrada de dados
numero = int(input("Informe um número inteiro: "))

# Computação
quadrado = numero**2
cubo = numero**3

concatenacao = "O núemero informado foi (" + str(numero) + ") e o seu quadrado é (" + str(quadrado) + ") e o seu cubo é (" + str(cubo) + ")."

# Saída de dados
print(concatenacao)

# Exercício finalizado