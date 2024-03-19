"""
Exercício 24: Elabore um algoritmo para efetuar o cálculo da quantidade de combustível gasto
em uma viagem, utilizando-se um automóvel que faz 12 Kms por litro. Para
obter o cálculo, o usuário deverá fornecer o tempo gasto e a velocidade média
durante a viagem.
"""

# Entrada de dados 
velocidade = int(input("Informe sua velocidade em Km/h: "))
tempo = float(input("Informe quantas horas demorou a viagem: "))

#  Computação
  # Cálculo para achar a distância do ponto A ao ponto B
dintancia = velocidade / tempo

  # Cálculo pa descobrir quantos litros foram usados
quantidadeDeLitrosUsados = dintancia / 12 # É dividido por 12, pelo fato que a cada 12 km é consumido 1 litro do veículo

concatenacao = "A quantidade de combustível gasto durante a viagem foi de " + str(round(quantidadeDeLitrosUsados, 2)) + " litros."

# Saída de dados
print(concatenacao)