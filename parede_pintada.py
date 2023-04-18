"""Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""

print ("\n\n======PINTAR PAREDE=======")

altura = float(input("\nAltura da Parede: "))
largura = float(input("Largura da Parede: "))
area = altura * largura
litros_de_tinnta = area / 2

print ("Para pintar uma parede de {:.2f} metros, precisa de {:.2f} litros de tinta". format(area, litros_de_tinnta))
print ("\n")