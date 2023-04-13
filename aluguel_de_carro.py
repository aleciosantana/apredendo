"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

print ("\n=======ALUGUEL DE CARRO=======")
dias = int(input("\nInforme Quantos dias de aluguel: "))
km_rodados = float(input("Informe Quantos KM rodados: "))
custo_aluguel = (dias * 60) + (km_rodados * 0.15)
print ("\nO custo do aluguel foi de: {:.2f}".format(custo_aluguel))
print ("\n")