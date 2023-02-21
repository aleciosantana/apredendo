
total = 0
quantidade_socio = 0
quantidade_nao_socio = 0

TAXA_SOCIO = 10.00
TAXA_NAO_SOCIO = 20.00

def percentual(quantidade):
  return quantidade * 100 / total

while total <= 1999:
  quantidade = int(input(f"\nDigite uma quantidade até {2000 - total}: "))
  
  if quantidade + total > 2000: continue

  tipo = input("Digite o tipo de ingresso S ou NS: ")

  if (tipo =="S" or tipo =="s"):
    quantidade_socio = quantidade_socio + quantidade
    total = total + quantidade

  elif (tipo =="NS" or tipo =="ns"):
    quantidade_nao_socio = quantidade_nao_socio + quantidade
    total = total + quantidade

  else:
    print("\nTipo invalido")

print('\n-------------------------------------\n')

print(f"Socio:                   {quantidade_socio}")
print(f"Não Socio:               {quantidade_nao_socio}\n")

print(f"Percentual de Socio:     {percentual(quantidade_socio)} %")
print(f"Percentual de Não Socio: {percentual(quantidade_nao_socio)} %\n")

print(f"Valor Socio:             {quantidade_socio * TAXA_SOCIO}")
print(f"Valor Não Socio:         {quantidade_nao_socio * TAXA_NAO_SOCIO}\n")

valor_total = (quantidade_socio * TAXA_SOCIO) + (quantidade_nao_socio * TAXA_NAO_SOCIO)
print(f"Valor Total:             {valor_total}\n")
