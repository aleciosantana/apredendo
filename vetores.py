# a = 3
# b = 5
# soma = a + b
# quadrado = soma**2
# print("A soma é :", soma, "\nO quadrado é :", quadrado, "\nSoma é igual a 10?",
#       soma == 10, "\nSoma é igual a 8?", soma == 8)
# print(b // 2)

# if soma == 8:
#   print("\n\n------Vc é muito inteligente--------")
# else:
#   print("\n\n\n\nEstuda Mais")

# for x in range(10):
#   print(x)

# print("\n\n")


# def letra_f():
#   frase = input("Digite uma frase:")
  
#   if "f" in frase: 
#     print("\nexite a letra F nessa frase\n")
#     return
    
#   print("\nNao existe letra F nessa frase\n")
    
#   letra_f()
#   return

# letra_f()




# frase = ""
# while "f" not in frase:
#   print("\n")

#   frase = input("Digite uma frase\n")
#   print("\n")
#   if "f" in frase:
#     print("\n")
#     print("exite a letra F nessa frase")
#     continue
#   print("\n")

#   print("Nao existe letra F nessa frase")

# print("\n\n")


# def junior():
#   print("                                 Vc tem o Dom")


# junior()

# print ("Aprendendo ")
# -----------------------------------------------------------------------------
# soma = 12 + 5 / 2 
# print ("a soma é:" , soma)

# n1 = ""
# n2 = ""
# n1 = input ("digite o primeiro numero:")
# n2 = input ("digite o segundo numero:")

# print ("\n")
# print ( "numero:" ,n1)
# print ( "numero:" ,n2)
# # --------------------------------------------------------------

# n1 = int (input ("digite o numero:"))
# ant = n1 -1
# suc = n1 +1
# print("O anterior é:" ,ant ,"O Sucesso é:" ,suc )
# # ---------------------

# nome = input("Digite um nome: ")
# endereco = input("Digite Endereço: ")
# tel = input("Digite Telefone: ")

# print("\n")
# print("Nome:",nome)
# print("endereço:",endereco)
# print("Telefone:" ,tel)

# ------------------------------------

# num = float (input("Digite um Numero com PONTO: "))
# print("\n")
# print ("A terça Parte É: ",num / 3)

# ---------------
# import math
# angulo = float (input("Digite o angulo:"))
# radiando = angulo * (math.pi / 180)
# print("\n Seno:", math.sin(radiando))
# print("\n Co-seno:", math.cos(radiando))
# print("\n Tangene:", math.tan(radiando))
# print("\n Co-Secante:", 1 / math.sin(radiando))
# print("\n Secante:", 1 / math.cos(radiando))
# print("\n Cotangente:", 1 / math.tan(radiando))

# _____________________________

# qtdsocio = 0
# qtdnaosocio = 0
# qtdtotal = 0
# tipo = ""
# qtd = 0
# qtd = int(input("\n Digite a Quantidade ou 2000 para terminar: "))
# while (qtd + qtdtotal <= 2000):
#   # qtd = int(input("\n Digite a Quantidade ou 2000 para terminar: "))
#   tipo = input("\n Digite o tipo de Ingresso S ou SN: ")
#   if (tipo =="S" or tipo =="s"):
#          qtdsocio = qtdsocio + qtd
#          qtdtotal = qtdtotal + qtd
#   else:
#       if (tipo =="NS" or tipo =="ns"):
#        qtdnaosocio = qtdnaosocio + qtd
#        qtdtotal = qtdtotal + qtd
#       else:
#         print("\n Tipo invalido")

# print("\n Socio: ", qtdsocio)
# print("\n Não Socio: ", qtdnaosocio)

# percsocio = qtdsocio * 100 / qtdtotal

# print("\n Percentual de Socio: ", percsocio)
# print("\n Valor Socio: ", qtdsocio * 10.00)
# print("\n Valor Não Socio: ", qtdnaosocio * 20.00)
# valtotal = qtdsocio * 10.00 + qtdnaosocio * 20.00
# print("\n Valor Total: ", valtotal)

# total = 0
# quantidade_socio = 0
# quantidade_nao_socio = 0

# TAXA_SOCIO = 10.00
# TAXA_NAO_SOCIO = 20.00

# def percentual(quantidade):
#   return quantidade * 100 / total

# while total <= 1999:
#   quantidade = int(input(f"\nDigite uma quantidade até {2000 - total}: "))
  
#   if quantidade + total > 2000: continue

#   tipo = input("Digite o tipo de ingresso S ou NS: ")

#   if (tipo =="S" or tipo =="s"):
#     quantidade_socio = quantidade_socio + quantidade
#     total = total + quantidade

#   elif (tipo =="NS" or tipo =="ns"):
#     quantidade_nao_socio = quantidade_nao_socio + quantidade
#     total = total + quantidade

#   else:
#     print("\nTipo invalido")

# print('\n-------------------------------------\n')

# print(f"Socio:                   {quantidade_socio}")
# print(f"Não Socio:               {quantidade_nao_socio}\n")

# print(f"Percentual de Socio:     {percentual(quantidade_socio)} %")
# print(f"Percentual de Não Socio: {percentual(quantidade_nao_socio)} %\n")

# print(f"Valor Socio:             {quantidade_socio * TAXA_SOCIO}")
# print(f"Valor Não Socio:         {quantidade_nao_socio * TAXA_NAO_SOCIO}\n")

# valor_total = (quantidade_socio * TAXA_SOCIO) + (quantidade_nao_socio * TAXA_NAO_SOCIO)
# print(f"Valor Total:             {valor_total}\n")

# Atividade do banco.

# saldo = 0
# retira = 0
# valor = 0
# deposito = 0
# codigo = 0

# print("\n\n-------------SEMPRE VERMELH0-------------\n\n")
  
# saldo = float (input("Digite o Saldo: "))

# codigo = int (input("\n_________________Digite o Codigo_______________\n\nSaque em Dinheiro (10): \nDeposito (33): \nPagamento de Cheque (4): \n\n          Finalizar (0): \n"))

# while saldo >= 1:
  
#   if (codigo == 10):
    
#       retira = float(input("\nDigite o Valor do Saque: "))
#       saldo = saldo - retira
#       print ("\nSaldo Atual: ",saldo)
    
#   else:
    
#       if (codigo == 33):
#         deposito = float(input("\n Digite o Valor do Deposito: "))
#         saldo = saldo + deposito
#         print ("\nSaldo Atual: ",saldo)
        
#       else:
        
#         if (codigo == 4):
#           valor = float(input("\nEntre com o Valor do Cheque: "))
#           saldo = saldo - valor
#           print ("\nSaldo Atual: ",saldo)

#   if (saldo <= 0):
    
#     print ("\nSaldo Negativo de: ",saldo)
#   codigo = int (input("\nDigite o Codigo_______________\nSaque em Dinheiro (10): \nDeposito (33): \nPagamento de Cheque (4): \nFinalizar (0): \n\n"))

# print ("\nSaldo Atual: ",saldo)

# Atividade do banco.

# saldo = 0
# retira = 0
# valor = 0
# deposito = 0
# codigo = 1

# FINALIZAR = 0
# SACAR = 10
# DEPOSITAR = 33
# CHEQUE = 4

# def digite_codigo():
#   print('\n_________________Digite o Codigo_______________\n\n')
#   print(f'Saque em Dinheiro   ({SACAR})')
#   print(f'Deposito            ({DEPOSITAR})')
#   print(f'Pagamento de Cheque ({CHEQUE})')
#   print(f'Finalizar           ({FINALIZAR})')

#   return int (input('\nCodigo: '))

# print("\n\n-------------SEMPRE VERMELH0-------------\n")
  
# saldo = float (input("Digite o Saldo: "))

# codigo = digite_codigo()

# while codigo != FINALIZAR:
#   if (codigo == SACAR):
#     retira = float(input("\nDigite o Valor do Saque: "))
#     saldo = saldo - retira
#     print ("\nSaldo Atual: ",saldo)
    
#   elif (codigo == DEPOSITAR):
#     deposito = float(input("\nDigite o Valor do Deposito: "))
#     saldo = saldo + deposito
#     print ("\nSaldo Atual: ",saldo)
        
#   elif (codigo == CHEQUE):
#     valor = float(input("\nEntre com o Valor do Cheque: "))
#     saldo = saldo - valor
#     print (f'\nSaldo Atual: {saldo}')

#   codigo = digite_codigo()

# print ("\nSaldo Atual: ",saldo)

# --------------------------------------------
# restaurante taxa garson

# cres = 0
# comgorg = 0

# cres = float(input("\n\nEntre com o Valor da Conta: "))
# comgorg = cres * 1.1
# print("\n\nO Valor da compra com Gorgeta Será:",comgorg,)

# -----------------------------------
# horas em minutos

# hora = 0
# minuto = 0
# tminutos = 0

# hora = int(input("\n\nEnforme a hora Atual: "))
# minuto = int(input("\n\nEnforme com Minutos: "))
# tminutos = hora * 60 + minuto

# print("Ate agora se passaram: ",tminutos,"minutos!")

# --------------------------------------------------

# op = 0
# pterra = 0

# print("\nPlanetas q podem se Analizados: ")
# print("\n1 Mercurio     2 Venos     3 Marte")
# print("\n4 Jupter:     5 Saturno:     6 Urano")

# op = int(input("\nEscolha o Planeta a ser Analizado: "))
# pterra = float(input("\nEntre com o peso na terra: "))

# match op:
#   case 1:
#     print("\nSeu peso no Planeta Mercurio é: ",(pterra/10)*0.37)
#   case 2:
#     print("\nSeu peso no Planeta Venos é: ",(pterra/10)*0.88)
#   case 3:
#     print("\nSeu peso no Planeta Marte é: ",(pterra/10)*0.38)
#   case 4:
#     print("\nSeu peso no Planeta Jupter é: ",(pterra/10)*2.64)
#   case 5:
#     print("\nSeu peso no Planeta Saturno é: ",(pterra/10)*1.15)
#   case 6:
#     print("\nSeu peso no Planeta Urano é: ",(pterra/10)*1.17)
#   case _:
#     print("\nOpção Ivalida! ")

# =============================

# --------------------------------------------------

# opicao = 0
# peso_terra = 0
# planetas = ['Mercurio', 'Venos', 'Marte', 'Jupter', 'Saturno', 'Urano']
# gravidades = [0.37, 0.88, 0.38, 2.64, 1.15, 1.17]

# print("\nPlanetas q podem se Analizados: ")
# print("\n1 Mercurio     2 Venos     3 Marte")
# print("\n4 Jupter:     5 Saturno:     6 Urano")

# opicao = int(input("\nEscolha o Planeta a ser Analizado: "))

# if (opicao < 1 or opicao  len(planetas)):
#   print("\nOpção Ivalida! ")
# else:
#   peso_terra = float(input("\nEntre com o peso na terra: "))
  
#   planeta = planetas[opicao - 1]
#   gravidade = gravidades[opicao - 1]

#   peso_planeta = (peso_terra/10) * gravidade
  
#   print(f"\nSeu peso no Planeta {planeta} é: {peso_planeta}")

# =============================

# voltalagoa = 0
# abdominais = 0
# for voltalagoa 1, voltalagoa <= 3, voltalagoa ++
#   print("\n",voltalagoa,"a volta na lagoa")
#      for (abdominais == 1, abdominais <= 5, abdominais++)
#         print("\n",abdominais,"Abidominais")
# print("\n")


          # Nao resolvida

# c = 0

# for c in c (""):
#   c == 2, c <= 10, c == c + 2
#   print("\n",c)

  # -----------
  
# idade = int(input("Digite a idade da pessoa: "))

# if idade <=1:
#     print ("Recém nascido")
# elif idade < 13:  
#         print ("Criança")
# elif idade < 18:
#     print ("Adolescente")
# elif idade < 60:
#     print ("Adulto")
# elif idade < 80:
#     print ("Idoso")
# else:
#     print ("Longevo")

# print ("Acabou.")

# ==================

nome = ""
l = 0
nomes = ["Sophia","Emma" ,"Olivia" ,"Ava" ,"Isabella" ,"Mia" ,"Charlotte" ,"Amelia"]
end = ["rua1", "rua2", "rua3", "rua4", "rua5", "rua6","rua7", "rua8"]
fone = [1, 2, 3, 4, 5, 6, 7, 8]

# for l in l ( l == 0, l <= 29, l+1):

nomes = input("\nNome")
end = input("\nEnd: ")
fone = input("\nFone:")

nomes = input("\nDigite Nome para procura: ")

l = 0

while (l <= 29 and nomes != nomes[l]):
    l+1
    if nomes == nomes[l]:
        print ("\nNome: ",nomes[l])
        print ("\nEndereço: ",end[l])
        print ("\nFone: ",fone[l])
    else:
        print ("\nNão encontrei:")

        n1 = int(input("Digita um numero : "))

