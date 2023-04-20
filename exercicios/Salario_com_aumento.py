"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

print ("\n=====ACRECIMO DE 15 % NO SALARIO======")
salario = float(input("\nSalario Atual: "))
acreimo = salario + (salario * 15 / 100)
print ("Novo salario com acrecimo de 15 % : {:.2f}".format(acreimo))
print ("VC estar Rico !!!\n")