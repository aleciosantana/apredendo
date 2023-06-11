"""Desenvolver um programa que leia as duas notas e mostre a media"""
nota1 = int(input("\nPrimeira Nota: "))
nota2 = int(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print ("A media é: {:.1f}".format(media))