class Pessoa: #class
    def __init__(self, nome=None, idade=34):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self): #método
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Marco')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Ferrari'
    print(p.nome)
    print(p.idade)