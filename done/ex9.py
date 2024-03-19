"""
Exercício 9: Escreva um programa que leia três números inteiros e mostre como resultado a
soma desses três números e também a multiplicação desses três números. Faça a
simulação passo a passo da execução do programa.s
"""

# Entrada de dados
numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

# Computação
soma = numero1 + numero2 + numero3
multiplicacao = numero1 * numero2 * numero3

concatenacao = (
      "Os números inseridos foram " 
      + str(numero1) + ", " 
      + str(numero2) + " e " 
      + str(numero3) + ", e a soma desses números é (" 
      + str(soma) + "). Já o resultado de sua multiplicação é (" 
      + str( multiplicacao) + ")."
      )

# Saída de dados
print(concatenacao)

# Exercício finalizado