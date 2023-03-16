c = ""
c1 = ""
d = ""
d1 = ""

c = input ("digite a palavra: ")
c1 = input ("digite a segunda palavra: ")

print("\nTamanho da primeira palavra: ",len(c))
print("\nConcatenando: ", c, c1)
d = c
print("\nO conteudo de D:", d)
d1 = (c, c1)
print("\nConcatenação D1: ",d1)
print("\nPrimeiro caracter: ",c[0])
print("\nUltimo caracter: ",c[-1])
print("\nTodos menos o primeiro: ",c[1:])
print("\nTerceiro elemento: ",c[3])
print("\nTres Primeiros: ",c[:3])
print("\nTres Ultimos: ",c[3:])
print("\n")
