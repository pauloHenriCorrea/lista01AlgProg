"""
Exercício 23: Um hotel deseja fazer uma promoção especial de final de semana, concecendo
um desconto de 25% na diária. Sendo informados, através do teclado, o número
de apartamentos do hotel e o valor da diária por apartamento para o final de
semana completo, elabore um programa para calcular:

• Valor promocional da diária;

• Valor total a ser arrecadado caso a ocupação neste final de semana atinja 100%;

• Valor total a ser arrecadado caso a ocupação neste final de semana atinja 70%;

• Valor que o hotel deixará de arrecadar em virtude da promoção, caso a ocupação atinja 100%.
"""

# Entrada de dados
numeroDeApartamentos = int(input("Informe o número de apartamestos: "))
diariaNormal = int(input("Informe o valor da diária: "))

# Computação
  # Valor promocional da diária;
diariaPromocional = round(diariaNormal * 0.75, 2)

  # Valor total a ser arrecadado caso a ocupação neste final de semana atinja 100%
valorTotalArrecado = numeroDeApartamentos * diariaPromocional

  # Valor total a ser arrecadado caso a ocupação neste final de semana atinja 70%;
valorSetenta = valorTotalArrecado * 0.70

  # Valor que o hotel deixará de arrecadar em virtude da promoção, caso a ocupação atinja 100%.
valorDePerda = (numeroDeApartamentos * diariaNormal) - valorTotalArrecado

concatenacao = (
  "• Valor promocional da diária: " + str(diariaPromocional) + " R$\n" +

  "• Valor total a ser arrecadado caso a ocupação neste final de semana atinja 100%: " + str(valorTotalArrecado) + " R$\n" +

  "• Valor total a ser arrecadado caso a ocupação neste final de semana atinja 70%: " + str(valorSetenta) + " R$\n" +

  "• Valor que o hotel deixará de arrecadar em virtude da promoção, caso a ocupação atinja 100%: " + str(valorDePerda) + " R$"
)

# Saída de dados
print(concatenacao)