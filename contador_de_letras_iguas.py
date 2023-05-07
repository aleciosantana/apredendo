nome = str(input("Digite o nome da Pessoa:")).strip().upper()
print ("A letra 'A' aparaece {} vezes neste nome.".format(nome.count('A')))
print ("A primeira letra 'A' aparaece na posição {}.".format(nome.find('A')))
print ("A Utima letra 'A' aparaece na posição {}.".format(nome.rfind('A')))