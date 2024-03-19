"""
Exercício 5:  Escreva um programa que recebe o raio de um círculo, calcula e mostra o valor
da área desse círculo.
"""


"""
Nessa biblioteca contém algumas funções matemáticas, como o PI, que neste caso é o que vamos utilizar 
"""
import math

# Entrada de dados
raio = float(input("Informe o raio do circulo: "))

# Computação
# A constante matemática π = 3.141592…
areaDoCirculo = math.pi * raio**2

concatenacao = "A área do seu circulo é de: " + str(round(areaDoCirculo, 2))

# Saída de dados
print(concatenacao)

# Exercício finalizado