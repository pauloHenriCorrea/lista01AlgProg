"""
Exercício 11: Escreva um programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas por mês. Seu programa deve calcular e mostrar o total do seu
salário no referido mês.
"""

# Entrada de dados 
quantidadeCobradaPorHora = float(input("Informe a quantidade ganha por hora: "))
quantidadeDeHorasTrabalhadaPorMes = float(input("Informe as horas trabalhadas por mês: "))

# Computação
salarioMensal = round(quantidadeCobradaPorHora * quantidadeDeHorasTrabalhadaPorMes, 2)

concatenacao = (
  "A quantidade cobrada por horas é de " + str(quantidadeCobradaPorHora) +
  " R$, e o usuário trabalhou por " + str(quantidadeDeHorasTrabalhadaPorMes) +
  " horas durante o mês. Seu salário do mês é de " + str(salarioMensal) +  " R$."
  )

# Saída de dados 
print(concatenacao)

# Exercício finalizado