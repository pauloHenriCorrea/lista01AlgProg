"""
Exercício 18: (Extensão do exercício 17) 
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros
(que custam R$ 80,00) ou em galões de 3,6 litros (que custam R$ 25,00). Informe ao usuário as quantidades de tinta a serem
compradas e os respectivos preços em 3 situações:
• Comprar apenas latas de 18 litros;
• Comprar apenas galões de 3,6 litros;
• Misturar latas e galões. Não é permitido sobrar tinta nos galões de 18 litros, mas é permitido sobrar tinta nos galões de 3,6 litros.
"""

import math

# Entrada de dados
areaParaPintar = float(input("\nInforme o tamanho em metros quadrados da área a ser pintada: "))

# Computação
  # Foi dividido neste caso por 3, porque toda vez que ter 3 m² será utilizado 1l de tinta
quantidadeDeLitros = areaParaPintar / 3 

  # Já para encortar a quantidade de latas, basta dividir por 18
quantidadeDeLatas = quantidadeDeLitros / 18
quantidadeDeGaloes = math.ceil(( quantidadeDeLitros % 18) / 3.6)

concatenacao = (
  "\nA quantidade de lata a ser comprada é de:  " + str(int(quantidadeDeLatas)) + "\n" +
  "A quantidade de galão para ser comprado é de: " + str((quantidadeDeGaloes)) + "\n"
)

# Saída de dados 
print(concatenacao)

# Exercício finalizado