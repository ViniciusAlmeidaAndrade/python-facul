# 1ª questão; Faça um Programa que peça dois números e imprima o maior deles:

n1 = float(input("Digite o 1º numero: "))
n2 = float(input("Digite o 2º numero: "))
if(n1>n2):
    print(n1)
else:
    print(n2)

#2ª questão; Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo:

pos_neg = float(input("Digite um numero positivo ou negativo: "))
if(pos_neg < 0):
    print("Negativo")
else:
    print("Positivo")

#3ª questão; Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido:

f_ou_m = input("Digite f para feminino e m para masculino: ")
if(f_ou_m == "f"):
    print("Feminino")
elif(f_ou_m == "m"):
    print("Masculino")
else:
    print("Sexo indefinido")

# Questão extra (Já tinha feito, mas tinha esquecido no github)

aluno = input("Nome do aluno: ")
nota_1 = float(input(f"nota 1 de ({aluno}): "))
nota_2 = float(input(f"Nota 2 de ({aluno}): "))
resultado = (nota_1 + nota_2) / 2
if (resultado > 7):
    print(resultado, "O aluno", aluno,"foi: APROVADO")
elif (resultado > 3 and resultado < 7):
    print(resultado, "O aluno", aluno,"está de: RECUPERAÇÃO")
else:
    print(resultado, "O aluno", aluno, "foi: REPROVADO")

#4ª questão; Faça um Programa que verifique se uma letra digitada é vogal ou consoante:

vog_cons = input("Digite uma letra para saber se ela é vogal ou consoante: ")
if (vog_cons == "a" or "e" or "i" or "o" or "u"):
    print("Vogal")
else:
    print("Consoante")

#5ª questão; Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações:

usu = input("Informe seu nome de usuário: ")
sen = input("Informe sua senha: ")
while(usu == sen):
    print("ERRO! INFORME UMA SENHA DIFERENTE DO SEU NOME DE USUÁRIO")
    usu = input("Informe seu nome de usuário: ")
    sen = input("Informe sua senha: ")

#6ª questão; Faça um programa que leia 5 números e informe o maior número:

maior = 0
for i in range(1,6):
    resp = int(input("Digite um numero: "))
    if(resp > maior):
        maior = resp
print (f"O maior numero é: {maior}")

#7ª questão; Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares:

par=0
imp=0
for i in range (1,10):
    par_imp = int(input(f"Digite o {i}º numero inteiro para listar os pares e impares: "))
    if(par_imp % 2 == 0):
        par = par + 1
    else: 
        imp = imp + 1 
print(f"Quantidade de números pares: {par}")
print(f"Quantidade de números impares: {imp}")

#8ª questão; Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos:

def argumentos(n1, n2, n3):
    return n1 + n2 + n3
num_1 = float(input("Digite o primeiro numero: "))
num_2 = float(input("Digite o segundo numero: "))
num_3 = float(input("Digite o terceiro numero: "))
print(argumentos(num_1, num_2, num_3))

#9ª questão; Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo:

def pos_neg(p_ou_n):
    if(p_ou_n > 0):
        print("P [positivo]")
    else:
        print("N [negativo]")
    return(print)

num = float(input("Digite um valor positivo ou negativo: "))
print(pos_neg(num))

#10ª questão; Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas:

def somaImposto(taxaimposto, custo):
    valor = (taxaimposto * custo) / 100
    valor = valor + custo
    print("o valor do produto com imposto é:",valor)
v_prod = float(input("Qual o valor do produto sem imposto: "))
v_impos = float(input("Qual o valor do imposto(Sem o caractere de porcentagem[%]): "))
print(somaImposto(v_impos, v_prod))