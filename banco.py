
saldo = 0
retira = 0
valor = 0
deposito = 0
codigo = 1

FINALIZAR = 0
SACAR = 10
DEPOSITAR = 33
CHEQUE = 4

def digite_codigo():
  print('\n_________________Digite o Codigo_______________\n\n')
  print(f'Saque em Dinheiro   ({SACAR})')
  print(f'Deposito            ({DEPOSITAR})')
  print(f'Pagamento de Cheque ({CHEQUE})')
  print(f'Finalizar           ({FINALIZAR})')

  return int (input('\nCodigo: '))

print("\n\n-------------SEMPRE VERMELH0-------------\n")
  
saldo = float (input("Digite o Saldo: "))

codigo = digite_codigo()

while codigo != FINALIZAR:
  if (codigo == SACAR):
    retira = float(input("\nDigite o Valor do Saque: "))
    saldo = saldo - retira
    print ("\nSaldo Atual: ",saldo)
    
  elif (codigo == DEPOSITAR):
    deposito = float(input("\nDigite o Valor do Deposito: "))
    saldo = saldo + deposito
    print ("\nSaldo Atual: ",saldo)
        
  elif (codigo == CHEQUE):
    valor = float(input("\nEntre com o Valor do Cheque: "))
    saldo = saldo - valor
    print (f'\nSaldo Atual: {saldo}')

  codigo = digite_codigo()

print ("\nSaldo Atual: ",saldo)
