tarefas = []
codigo = 1

FINALIZAR = 0
ADICIONAR = 1
EXCLUIR = 2
EDITAR = 3
LISTAR = 4

while codigo != FINALIZAR:
    codigo = int(input("digite o codigo: "))

    if codigo == ADICIONAR:
        tarefa = input("Digite a Tarefa: ")
        tarefas.append(tarefa)
        print(tarefas)

    elif codigo == EXCLUIR:
        tarefa = input("\nDigite a tarefa: ")
        tarefas.remove(tarefa)
        print(tarefas)

    elif codigo == EDITAR:

        tarefa = input("Digite a tarefa: \n")
        nova_tarefa = input("\nDigite a Nova tarefa: ")
    
        index = tarefas.index(tarefa)
        tarefas[index] = nova_tarefa
        print(tarefas)

    elif codigo == LISTAR:
        print('----------------')
        n = len(tarefas)
        for i in range(n):
            print(tarefas[i])

        total = len(tarefas)
        print(f'\nForam encontrados: {total}\n')
print("PROGRAMA FINALIZADO !!!")

