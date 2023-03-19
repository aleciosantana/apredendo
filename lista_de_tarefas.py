import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="blog"
)

mycursor = mydb.cursor()

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
        descricao = input("Digite a Tarefa: ")
        mycursor.execute("INSERT INTO tarefas (descricao) VALUES (%s)", [descricao])
        mydb.commit()

    elif codigo == EXCLUIR:
        descricao = input("\nDigite a tarefa: ")

        mycursor.execute("DELETE FROM tarefas WHERE descricao = %s", [descricao])
        mydb.commit()

    elif codigo == EDITAR:

        descricao = input("Digite a tarefa: \n")
        nova_descricao = input("\nDigite a Nova tarefa: ")

        mycursor.execute("UPDATE tarefas SET descricao = %s WHERE descricao = %s", [nova_descricao, descricao])

        mydb.commit()

        print(mycursor.rowcount, "record(s) affected")

    elif codigo == LISTAR:
        print('----------------')
        mycursor.execute("SELECT * FROM tarefas")

        tarefas = mycursor.fetchall()

        for tarefa in tarefas:
            print(tarefa[1])

        print('----------------')

        total = len(tarefas)
        print(f'\nForam encontrados: {total}\n')
print("PROGRAMA FINALIZADO !!!")

