"""
Exercício 12: Escreva um programa que recebe uma temperatura em graus Celsius, transforma
e mostra a temperatura em graus Fahrenheit.
"""

# Entrada de dados
celsius = int(input("Informe a temperatura em °C em sua cidade: "))

# Computação
  # Fórmula para converter celsius em fahrenheit:
  # F = (C * 1,8) + 32
fahrenheit = (celsius * 1.8) + 32

concatenacao =  (
  "A temperatura na sua cidade em °C é de " + str(celsius) + " °C" +
  ", e essa mesma temperatura em °F é de " + str(fahrenheit) + " °F"
  )

# Saída de dados
print(concatenacao)

# Exercício finalizado