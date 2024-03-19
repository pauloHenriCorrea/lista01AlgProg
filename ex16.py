"""
Exercício 16: (Extensão do exercício 11) Faça um programa que pergunta quanto você ganha
por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu
salário no referido mês, sabendo-se que são descontados 11% para o imposto de
renda, 8% para o INSS e 5% para o sindicato. Seu programa deve mostrar para
o usuário as seguintes informações:
• Salário bruto;
• Quanto pagou ao INSS;
• Quando pagou ao sindicato;
• Salário líquido.
"""

# Entrada de dados 
quantidadeCobradaPorHora = int(input("\nInforme a quantidade ganha por hora: "))
quantidadeDeHorasTrabalhadaPorMes = int(input("Informe as horas trabalhadas por mês: "))

# Computação
  # Cálculo do salário bruto, sem desconto algum.
salarioMensalBruto = round(quantidadeCobradaPorHora * quantidadeDeHorasTrabalhadaPorMes, 2)

  # Cálculo do salário com desconto do INSS
valorPagoAoINSS = round(salarioMensalBruto * 0.11, 2) # 0,11 equivale a 11%% do salário que será descontado pelo INSS 
# salarioMensalComDescontoDoINSS = salarioMensalBruto - valorPagoAoINSS 

  # Cálculo do salário com denconto do sindicato
valorPagoAoSindicato = round(salarioMensalBruto * 0.05, 2) # 0,05 equivale a 5%% do salário que será descontado pelo sindicato 
# salarioMensalComDescontoDoSindicato = salarioMensalBruto - valorPagoAoSindicato

  # Cálculo do salário liquído, com todos os descontos aplicado.
dencontoTotal = round(valorPagoAoINSS + valorPagoAoSindicato, 2)
salarioMensalLiquido = salarioMensalBruto - dencontoTotal

concatenacao = (
  "\nSalário bruto: " + str(salarioMensalBruto) + "\n" +
  "Valor pago ao INSS: " + str(valorPagoAoINSS) + "\n" +
  "Valor pago ao sindicato: " + str(valorPagoAoSindicato) + "\n" +
  "Salário líquido: " + str(salarioMensalLiquido) + "\n\r" 
)

# Saída de dados 
print(concatenacao)

# Exercício finalizado