"""
Exercício 22: Elabore um algoritmo e leia do teclado uma quantidade de segundos e transforme
esse tempo em dias, horas e minutos.
"""

# Entrada de dados 
segundos = int(input("Informe uma quantidade de segundos: "))

# Computação
minutos = segundos / 60
horas = segundos / 3600
dias = segundos / 86400

# Saída de dados
print(segundos)
print(minutos)
print(horas)
print(dias)

# Exercício finalizado