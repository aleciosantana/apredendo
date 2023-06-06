valor1 = int(input("Digite o primeiro numero: "))
valor2 = int(input("Digite o segundo numero: "))
valor3 = int(input("Digite o terceiro numero: "))
'''Buscando o Menor valor'''
if valor1 < valor2 and valor1 < valor3:
    print("O menor valor é o {}".format(valor1))
if valor2 < valor1 and valor2 < valor3:
    print("O menor valor é o {}".format(valor2))
if valor3 < valor1 and valor3 < valor2:
    print("O menor valor é o {}".format(valor3))
'''Buscando o Maior valor'''
if valor1 > valor2 and valor1 > valor3:
    print("O o maior valor é o {}".format(valor1))
if valor2 > valor1 and valor2 > valor3:
    print("O maior valor é o {}".format(valor2))
if valor3 > valor1 and valor3 > valor2:
    print("O maior valor é o {}".format(valor3))