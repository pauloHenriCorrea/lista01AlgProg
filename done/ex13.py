"""
Exercício 13: Escreva um programa que recebe uma temperatura em graus Fahrenheit, 
transforma e mostra a temperatura em graus Celsius.
"""

# Entrada de dados
fahrenheit = int(input("Informe a temperatura em °F em sua cidade: "))

# Computação
 # Fórmula para converter fahrenheit em celsius :
  # C = (F - 32) / 1,8
celsius = (fahrenheit - 32) / 1.8

concatenacao =  (
  "A temperatura na sua cidade em °F é de " + str(fahrenheit) + " °F" +
  ", e essa mesma temperatura em °C é de " + str(celsius) + " °C"
  )

# Saída de dados
print(concatenacao)

# Exercício finalizado