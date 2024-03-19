"""
Exercício 4: Escreva um programa que recebe as 4 notas bimestrais de um aluno e mostra a
média dessas notas.
"""

# Entrada de dados
nota1 = float(input("Informe sua primeira nota do bimestre: ")) 
nota2 = float(input("Informe sua segunda nota do bimestre: ")) 
nota3 = float(input("Informe sua terceira nota do bimestre: ")) 
nota4 = float(input("Informe sua quarta nota do bimestre: ")) 

# Computação
  # A divisão foi feita por 4, pelo fato que é uma conta aritmética, ou seja, média = (n1 + n2 + ..)/ número de notas
media = (nota1 + nota2 + nota3 + nota4) / 4

concatenacao = "Sua média do bimestre foi: " + str(media)

# Saída de dados
print(concatenacao)

# Exercício finalizado