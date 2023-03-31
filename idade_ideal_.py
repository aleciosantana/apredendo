idade = int(input("\nDigite a idade da pessoa: "))

if idade <=1:
    print ("\nRecém nascido")
elif idade < 13:  
        print ("\nCriança")
elif idade < 18:
    print ("\nAdolescente")
elif idade < 60:
    print ("\nAdulto")
elif idade < 80:
    print ("\nIdoso")
else:
    print ("\nLongevo")

print ("\nAcabou.")
