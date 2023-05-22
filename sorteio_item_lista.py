"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

import random
print ("\n============SORTEIO===========")
aluno1 = input("\nPrimeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
aluno5 = input("Quinto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
sorteio = random.choice(lista)
print ("\nO Aluno Sortiado foi: {}".format(sorteio))