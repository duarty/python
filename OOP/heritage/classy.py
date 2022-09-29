class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def obter_nome(self):
        return self.nome
    
    def tem_pedigree(self):
        return False
    
class Cachorro(Animal):
    def __init__(self, nome, idade, pelo, genero):
        # Não se esqueça de invocar o __init__ da classe pai
        super().__init__(nome, idade)
        self.pelo = pelo
        self.genero = genero

    def tem_pedigree(self): # Reescremos o método da função herdada
        return True

    def latir(self):
        return 'auau!'
    
bidu = Cachorro('Bidu', 5, 'curto', 'macho')
print(bidu.idade)
# 5
print(bidu.obter_nome())
# Bidu
print(bidu.tem_pedigree())
# True
print(bidu.latir())
# auau!