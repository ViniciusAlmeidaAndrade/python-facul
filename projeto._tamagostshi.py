class tamagostshi :
    def __init__(self, nome, fome, saude, idade ):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alteraNome(self, novoNome):    
        self.nome = novoNome

    def fome_tamagostshi(self, fome_gostshi ) :
        self.fome = fome_gostshi

    def saude_tamagotshi(self, saude_gostshi):     
        self.saude = saude_gostshi

    def idade_tamagotshi(self, idade_gostshi):
        self.idade = idade_gostshi



    def humor (self, alimentacao, bem_estar ):  
        self.fome = alimentacao
        self.saude = bem_estar 
        if alimentacao < 9:  
            print(f"alimente {self.nome}")
            if bem_estar < 8:
                print(f"Dê medicamento para {self.nome}")
        media = (alimentacao + bem_estar)/2

        return(f'O humor do(a) {self.nome} está em: {media}')
    
    def __str__(self):
        return(f'Nome: {self.nome}  fome: {self.fome}  saude: {self.saude}  idade: {self.idade}')

bichinho_eletronico = tamagostshi("cirilo", 8, 10, 2)
print(bichinho_eletronico)

humor = bichinho_eletronico.humor(bichinho_eletronico.fome, bichinho_eletronico.saude)
print(humor)
print()

tamagostshi_01 = tamagostshi("cirilo", 8, 10, 2)
tamagostshi_02 = tamagostshi("maria joaquina",5,9,2)

tamagostshi_01.fome_tamagostshi(10)
tamagostshi_01.saude_tamagotshi(9)
tamagostshi_01.idade_tamagotshi(3)

print(tamagostshi_01)
print(tamagostshi_01.humor(tamagostshi_01.fome, tamagostshi_01.saude))

print()
tamagostshi_02.fome_tamagostshi(8)
tamagostshi_02.saude_tamagotshi(5)
tamagostshi_02.idade_tamagotshi(3)

print(tamagostshi_02)
print(tamagostshi_02.humor(tamagostshi_02.fome, tamagostshi_02.saude))
print()