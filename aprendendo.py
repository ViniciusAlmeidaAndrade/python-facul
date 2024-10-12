Nome=str(input("Escreva seu nome: "))
while( len(Nome) <= 3 ):
    Nome=str(input("Escreva seu nome: "))
    
idade=int(input("escrema uma idade entre 0 e 150: "))
while(idade < 0 or idade > 150):
    idade=int(input("escrema uma idade entre 0 e 150: "))

salario=float(input("escreva seu salário: "))
while(salario < 0):
    salario=float(input("escreva seu salário: "))

sexo=str(input("Qual seu genero?: [f,m]"))

# DUVIDA
while sexo != ("f" or "Feminino") and sexo != ("m" or "masculino"):
    sexo=str(input("Qual seu genero?: [f,m]"))

estado_civil=str(input("Qual seu estado civil?: [Solteiro(S), Casado(C), Viuvo(V), Divorciado(D)]"))
while estado_civil != ("Solteiro" or "S") or estado_civil != ("Casado" or "C") or estado_civil != ("Viuvo" or "V") or estado_civil != ("Divorciado" or "D"):
    estado_civil=str(input("Qual seu estado civil?: [Solteiro(S), Casado(C), Viuvo(V), Divorciado(D)]"))    