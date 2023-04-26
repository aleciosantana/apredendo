"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa."""

from math import hypot
cateto = float(input("\nDigite o Cateto Oposto: "))
cateto_adjacente = float(input("Digite o Cateto Adjacente: "))
# hipotenusa = (cateto_adjacente ** 2 + cateto ** 2) ** (1/2)
hipotenusa = hypot(cateto, cateto_adjacente)
print ("\nO comprimento da hipotenusa é {:.2f}".format(hipotenusa))
print ("\n")