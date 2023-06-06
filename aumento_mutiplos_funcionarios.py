salario = float(input("\nDigite o salario Atual:  "))
if salario > 1250:
    aumento = salario + (salario / 100 * 10) 
else:
    aumento = salario + (salario /100 * 15)
print("O Salario antigo era {:.2f}, o atual é: {:.2f}".format(salario, aumento))
