"""O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

print ("\n========SORTEIO DE ORDEM NA LISTA========")
import random
aluno1 = input("\nPrimeiro Aluno: ")
aluno2 = input("Segundo Aluno: ")
aluno3 = input("Terceiro Aluno: ")
lista = [aluno1, aluno2, aluno3]
random.shuffle(lista)
print ("Ordem sorteada foi: {}".format(lista))