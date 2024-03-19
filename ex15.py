"""
Exercício 15: Escreva um programa que recebe o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de internet (em Mbps), calcula e informa o tempo
aproximado de download do arquivo usando este link (em minutos).
"""

# Entrada de dados
tamanhoArquivo = float(input("Insira o tamanho do arquivo em (MB)que deseja fazer download: "))
velocidadeInternet = float(input("Insira a velocidade de download da internet em (MBs): "))

"""
  Computação:
    => Para descobrir o tempo de download basta dividir o tamanho do arquivo pela velocidade da intenet.
    => Já para convertermos o tempo de download de MBps para MBpm basta dividirmos o  resultadao da divisão 
    do (tamanhoArquivo / velocidadeInternet) / 60
"""
tempoDeDownload = (tamanhoArquivo / velocidadeInternet) / 60

concatenacao = (
  "O tamanho do seu arquivo é de " + str(tamanhoArquivo) + " MB, e a velocidade de sua intenet é de " + 
  str(velocidadeInternet) + " MBs, logo a volocidade do seu download será de " + str(round(tempoDeDownload, 2)) + 
  " minutos."
)

# Saída de dados
print(concatenacao)

# Exercício finalizado