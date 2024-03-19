"""
Exercício 17: 
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math

# Entrada de dados
areaParaPintar = int(input("\nInforme o tamanho em metros quadrados da área a ser pintada: "))

# Computação
  # Foi dividido neste caso por 3, porque toda vez que ter 3 m² será utilizado 1l de tinta
quantidadeDeLitros = areaParaPintar / 3 

  # Já para encortar a quantidade de latas, basta dividir por 18
quantidadeDeLatas = quantidadeDeLitros / 18

  # O preço total é a quantidade de latas * proço unitario do produto, que neste caso custa 80,00 R$
precoTotal = quantidadeDeLatas * 80

concatenacao = (
  "\nA quantidade de lata a ser comprada é de:  " + str(quantidadeDeLatas) + " l\n" +
  "Preço total: " + str(round(precoTotal, 2)) + " R$" + "\n"
)

# Saída de dados 
print(concatenacao)

# Exercício finalizado