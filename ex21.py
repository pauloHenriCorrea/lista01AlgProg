"""
Exercício 21: O custo de um carro novo ao consumidor é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos sobre o custo de fábrica, 
e depois a percentagem do distribuidor sobre o resultado). Supondo que a percentagem do distribuidor 
seja de 28% e os impostos 45%, escreva um programa que leia o custo de fábrica de um carro e informa 
o custo final ao consumidor.
"""

# Entrada de dados
custoFabrica = float(input("Informe o valor de fabrica do veículo: "))

# Computação
  # Cálculo do imposto em cima do valor do veículo
custoComImposto = custoFabrica * 0.45

  # Cálculo da porcentagem do distribuidor do veículo
custoDoDistribuidor = custoComImposto * 0.28

  # Cálculo do valor final do veículo
custoFinalVeiculo =  custoFabrica + custoComImposto + custoDoDistribuidor

concatenacao = ("O custo final do veículo é de: " + str(custoFinalVeiculo))

# Saída de dados
print(concatenacao)