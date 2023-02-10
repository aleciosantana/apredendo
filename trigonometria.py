import math

angulo = float (input("Digite o angulo:"))
radiando = angulo * (math.pi / 180)

print("\n Seno:", math.sin(radiando))
print("\n Co-seno:", math.cos(radiando))
print("\n Tangene:", math.tan(radiando))
print("\n Co-Secante:", 1 / math.sin(radiando))
print("\n Secante:", 1 / math.cos(radiando))
print("\n Cotangente:", 1 / math.tan(radiando))
