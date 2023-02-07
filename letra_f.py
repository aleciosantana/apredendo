def letra_f():
  
  frase = input("Digite uma frase:")
  
  if "f" in frase: 
    print("\nExite a letra F nessa frase\n")
    return
    
  print("\nNão existe letra F nessa frase\n")
    
  letra_f()
  return

letra_f()
