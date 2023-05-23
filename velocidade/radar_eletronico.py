print("\n")
velocidade = float(input("\nQual a velocidade do carro: "))
if (velocidade > 80):
    print("\nMultado! Você passou de 80Km/h\n")
    multa = (velocidade - 80) * 7
    print("Você vai pagar multa de R${:.2f}!".format(multa))
else:
    print("\nParabens, você é um ótimo Motorista!\n")
