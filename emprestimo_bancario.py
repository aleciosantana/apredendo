print("\n\n         ______________BANCO BOM______________      ")
print("\nNão = 0 e Sim = 1")
nome_negativado = int(input("\nPossui nome Negativado?: "))

if nome_negativado == 1:
    print("\nNão pode realizar o empréstimo\n")
else:
    carteira_assinada = int(input("Possui carteira Assinada?: "))
    if carteira_assinada == 0:
            print("Não pode realizar o empréstimo ")
    else:
            possuicasa = int(input("Possui casa?: "))
            if possuicasa == 0:
                print("Não pode realizar o empréstimo")
            else:
                print("\nConceder Empréstimo")