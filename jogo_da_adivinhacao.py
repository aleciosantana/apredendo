from random import randint
print("\n")
computador = randint(0,5) # faz computador pensar
print("--"*20)
print("Vou pensar em um numero entre 0 e 5. Tente Adivinhar!")
print("--"*20)
jogador = int(input("Em que número eu pensei? "))#Jogador tenta adivinhar
print("\n")
if jogador == computador:
    print("Parabem vc venceu!!!")
else:
    print("Errou! u pensei no número {} e vc no {}".format(computador, jogador))