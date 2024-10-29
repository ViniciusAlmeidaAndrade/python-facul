# 1º Questão
lista=[1,4,6,10,12]
print(lista)
print()

# 2º Questão
lista=[]
for i in range(10):
    lista.append(i)
print(sum(lista))
print()

# 3º Questão
lista=[]
for i in range (0,100,4):
    lista.append(i)
maior=max(lista)
print(maior)
print()

# 4º Questão#
semana={}
semana['Segunda']=''
semana['Terça']='Paradigmas de linguagens de programação em python'
semana['Quarta']='Desenvolvimento web'
semana['Quinta']='Computação em nuvem'
semana['Sexta']='Banco de dados'
semana['Sabado']=''
semana['Domingo']=''
for i in semana:
    print(f"{i}: {semana[i]}")
print()

# 5º Questão

print("1-windows server\n2-Unix\n3-Linux\n4-netwware\n5- mac os\n6- outros") 


def votos():
    vetor= [0, 0, 0, 0, 0, 0, 0]

    while True:
        try:
            resp = int(input("Digite o numero ao seu Sistema operacional (1 a 6, ou 0 que encerrará a votação): "))
        except:
            print("Erro! Por favor, insira um numero existente nas opções. ")
            continue

        if resp == 0:
            break

        if 1 <= resp and resp <= 6:
            vetor[resp] += 1
        else:
            print("Erro! Por favor, insira um numero existente nas opções. ")

    tot_de_votos = sum(vetor)

    print()
    print("Sistema operacional     Votos        %")
    print("-------------------     -----     ------- \n")

    sistemas = ["Windows", "Unix", "Linux","Netware", "Mac OS", "Outro"]

    mais_votos = 0
    campeão = ""

    for i in range(1, 7):
        percentual = (vetor[i] / tot_de_votos) * 100 if tot_de_votos > 0 else 0
        print(f"{i} - {sistemas[i-1]}           {vetor[i]} votos   ({percentual:.2f}%)")
        

        if vetor[i] > mais_votos:
            mais_votos = vetor[i]
            campeão = sistemas[i-1]
    print("-------------------     -----     -------")        

    print(f"\nTotal de votos: {tot_de_votos}")
    if tot_de_votos > 0:
        print(f"O SO mais votado foi o {campeão}, com {mais_votos} votos, correspondendo a {(mais_votos / tot_de_votos) * 100:.2f}% dos votoscle")
    else:
        print("Nenhum voto registrado.")

votos()
