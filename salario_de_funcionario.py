'''7. Uma imobiliária paga aos seus corretores um salário base
de R$ 1.500,00. Além disso, uma comissão de R$ 200,00 por
cada imóvel vendido e 5% do valor de cada venda. Construa
um programa que solicite o nome do corretor, a quantidade
de imóveis vendidos e o valor total de suas vendas. Ao fim, o
programa deve calcular e escrever o salário final do corretor de
imóveis.'''

nome = input("\ndigite o nome: ")
imovel_vendidos = int(input("\nImoveis vendidos: "))
valor_total_vendas = int(input("\nValor total das vendas: "))
salario = 1500
comissao = 200 * imovel_vendidos + ( valor_total_vendas / 100 * 5 )
salario_final = salario + comissao

print(f"\nSalario Final de {nome}: {salario_final:.2f} ")
