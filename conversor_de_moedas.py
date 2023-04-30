"""Crie um plrograma para converter moedas"""

real = float(input("\nValor a ser convertido R$:"))
dolar = real * 5.44
euro = real * 5.99
print ("\nEm Dolar fica: {:.2f}".format(dolar))
print ("\nEm Euro fica: {:.2f}".format(euro))