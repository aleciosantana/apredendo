"""crie um programa q receba um preço e dé um desconto de 5 %"""

print ("\n========PRODUTO COM DESCONTO=== de 5 % ===")
preco = float(input("\nQual o preço do produto: "))
novo_preco = preco - (preco * 5 / 100) 
print ("O novo preço é de {:.2f}".format(novo_preco))
print ("\n")