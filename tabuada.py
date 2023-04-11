# cria uma tabuada

numero = int(input("\nEntre com o numero: "))

def soma(numero, n):
    return '{0} + {1} = {2:>2}'.format(numero, n, (numero + n))

def dividir(numero, n):
    if n == 0:
        return '{0} / 0 = infinito'.format(numero)
    else:
        return '{0} / {1} = {2:.2f}'.format(numero, n, (numero / n))

print ("\nMULTIPLICAÇÃO       ADIÇÃO              SUBTRAÇÃO           DIVISÃO")
for n in range(10):
    print (f"{numero} x {n} = {(numero * n):>2} {'':<8} {soma(numero, n)} {'':<8} {numero} + {n} = {(numero + n):>2} {'':<8} {dividir(numero, n)}")

