"""
Exercício 14: Tendo como dado de entrada a altura (h) de uma pessoa, escreva um programa
que mostre o peso recomendado para essa pessoa utilizando as seguintes fórmulas:
• Homens: (72.7*h) - 58
• Mulheres: (62.1*h) - 44.7
"""

# Entrada de dados
altura = float(input("Informe sua altura em metros (m): "))

# Computação
pesoRecomendadoParaHomem = (72.7 * altura) - 58
pesoRecomendadoParaMulher = (62.1 * altura) - 44.7

concatenacao = (
  "Para sua altura o peso recomendado se você for homem é de " + 
  str(round(pesoRecomendadoParaHomem, 2)) + " kg, mas caso você for mulher o peso recomendaddo é de " + 
  str(round(pesoRecomendadoParaMulher, 2)) + " kg."
  )

# Saída de dados
print(concatenacao)

# Exercício finalizado