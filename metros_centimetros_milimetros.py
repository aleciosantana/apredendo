"""Crie um programa que leia um valor em metros e imprima
o valor em """
metros = int(input("\nQuantos metros: "))
quilometro = metros / 1000
hectometro = metros / 100
decametro = metros / 10

decimetro = metros * 10
centimetro = decimetro * 10
milimetro = centimetro * 10

print (f"Medida de emtrada {metros}, em CM: {centimetro}, em MM: {milimetro}, decimetro: {decimetro}")
print (f"E o Km: {quilometro}, Hectometro: {hectometro}, decametro: {decametro}")
