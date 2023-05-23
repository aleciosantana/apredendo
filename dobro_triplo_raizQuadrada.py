"""criando um algoritimo que leia o numero e imprima o 
seu dobro, o triplo e a raiz quadrada"""

n1 = int(input("\nDigite um numero: "))
dobro = n1 * 2
triplo = n1 * 3
raiz_quadrada = n1 ** (1/2)
print ("O dobro é: {}".format(dobro))
print ("O triplo é: {}".format(triplo))
print ("A raiz Quadrada é: {:.2f}".format(raiz_quadrada))