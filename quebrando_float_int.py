"""Crie um programa que leia um número Real qualquer pelo 
teclado e mostre na tela a sua porção Inteira."""

import math
numero = float(input("\nDigite um numero Real: "))
print ("O numero inteiro é: {}".format(math.trunc(numero)))

# ou

print ("O numero inteiro é: {}".format(int(numero)))
