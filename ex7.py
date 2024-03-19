"""
Exercício 7: Escreva um programa que leia três números inteiros a, b e c, calcule a ∗ b + c e
mostre o resultado na saída padrão para o(a) usuário(a). Faça a simulação passo
a passo da execução do programa.
"""

# Entrada de dados
a = int(input("Informe o valor de a: ")) 
b = int(input("Informe o valor de b: "))
c = int(input("Informe o valor de c: "))

# Computação
calculo = a * b + c

concatenacao = "O resultado do cálculo de a * b + c é de: " + str(calculo)

# Saída de dados
print(concatenacao)

# Exercício finalizado