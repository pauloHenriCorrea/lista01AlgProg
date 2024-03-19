"""
Exercício 10: Escreva um programa que leia um número inteiro e mostre o resultado do quociente da divisão desse número por 2 e por 3. 
Faça a simulação passo a passo da execução do programa.
"""

# Entrada de dados
numero = int(input("Insira um número inteiro: "))

# Computação
divisaoPor2 = numero/2
divisaoPor3 = numero/3

concatenacao = (
  "O número inserido foi (" + str(numero) + "), e o resultado do seu quociente dividido por 2 é: (" +
  str(round(divisaoPor2, 2)) + "), já dividido por 3 seu quociente é: (" + str(round(divisaoPor3, 2)) + ")."
  )

# Saída de dados
print(concatenacao)

# Exercício finalizado