"""
Exercício 20: Faça um programa que após a entrada de uma determinada distância entre dois
pontos (em Km) e uma determinada velocidade (Km/h), diga qual o tempo médio
que levará para chegar a esse local e qual a velocidade em metros/segundos.
"""

# Entrada de dados
distancia = float(input("Informe a distância (Km) da onde você esta, até a onde você deseja chegar: "))
velocidade = int(input("Informe sua velocidade (Km/h): "))

# Computação 
tempo = round(distancia/velocidade)

  # O valor de 3,6 é para converter a velocidade que está em Km/h em m/s.
velocidadeEmMetrosPorSegundos = round(velocidade / 3.6, 2) 

concatenacao = (
  "O tempo médio será de: " + str(tempo) + " horas\n" + 
  "Sua velocidade em metros por segundos é de: " + str(velocidadeEmMetrosPorSegundos) + " m/s " 
  )

# Saída de dados
print(concatenacao)

# Exercício finalizado