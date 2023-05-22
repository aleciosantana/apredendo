numero = int(input("digite um numero: "))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print (f"Analizando o Numero {numero}")
print ("Unidade: {}".format(u))
print ("Dezena: {}".format(d))
print ("centena: {}".format(c))
print ("Milhar: {}".format(m))