class Pessoa: #class
    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self): #método
        return f'Olá {id(self)}'

if __name__ == '__main__':
    antonio = Pessoa(nome='Antonio', idade=12)
    marco = Pessoa(antonio, nome='Marco')
    print(Pessoa.cumprimentar(marco))
    print(id(marco))
    print(marco.cumprimentar())
    print(marco.nome)
    print(marco.idade)
    for filho in marco.filhos:
        print(filho.nome)
        print(filho.idade)
    marco.sobrenome = "Ferrari"
    del marco.filhos
    print(marco.__dict__)
    print(antonio.__dict__)
