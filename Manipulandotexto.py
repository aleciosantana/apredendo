"""Analizador de texto"""
print ("")
nome = str(input("Digite o nome completo: ")).strip()

print ("O nome digitado foi: {}".format(nome))

print ("Transformando em letras maiuscula: {}".format(nome.upper()))
print ("Transformando em letras minusculas: {}".format(nome.lower()))
print ("Quantas letras tem: {}".format(len(nome) - nome.count(" ")))
print ("Quantas letras tem o primeiro nome: {}".format(nome.find(" ")))
