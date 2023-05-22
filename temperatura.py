"""Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit."""

print ("\n======TEMPERATURA EM GRAUS=======")
ceLsius = float(input("\nInforme a temperatura em graus CELSIUS: "))
fahrenheit = (9 * ceLsius) / 5 + 32
print ("\nEm FAHRENHEIT é: {:.2f}".format(fahrenheit))
print ("\n")