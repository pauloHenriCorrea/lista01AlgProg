"""
Exercício 19: Uma pessoa resolver fazer uma aplicação em uma poupança programada. 
Para  calcular seu rendimento, ela deverá fornecer o valor constante da aplicação 
mensal, a taxa e o número de meses. A fórmula usada para o cálculo do valor acumulado é a seguinte:

Valor acumulado = (P * (1 + i) ** n - 1) / i

Onde i = taxa, P = aplicação mensal e n é o número de meses.
"""

# Entrada de dados
P = float(input("Informe o dinheiro depositado mensalmente: "))
n = int(input("Informe por quantos meses será aplicado o dinheiro: "))
i = float(input("Informe a taxa: "))

# Computação
valorAcomulado = (P * (1 + i) ** n - 1) / i

# Saída de dados
print(valorAcomulado)

# Exercício finalizado