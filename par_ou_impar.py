'''Crie um programa que leia um número inteiro e mostre
na tela se ele é PAR ou ÍMPAR.'''


print("=="*20)
numero = int(input("Digite um numero: "))
resultado = numero % 2
if (resultado == 0 ):
    print("Esse numero é Par")
else:
    print("esse numero é Impar")