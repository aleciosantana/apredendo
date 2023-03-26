# calcular distancia entre dois pontos

from math import sqrt

# entradas do ponto 1
x1 = int(input("\nintforme a cordenada para P1: "))
y1 = int(input("intforme a segunda cordenada para P1: "))
# entradas do ponto 2
x2 = int(input("\nintforme a cordenada para x2: "))
y2 = int(input("intforme a segunda cordenada para P2: "))

p1 = (x2 - x1) 
p2 = (y2 - y1)

distancia = sqrt((p1 * p1) + (p2 * p2)) 

print(F"\nA distancia entre os pontos é: {int(distancia):.2f}\n")     
