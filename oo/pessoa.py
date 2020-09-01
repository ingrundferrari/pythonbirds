class Pessoa: #class
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=34):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self): #método
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    antonio.olhos = 1
    del antonio.olhos
    print(marco.__dict__)
    print(antonio.__dict__)
    print(Pessoa.olhos)
    print(marco.olhos)
    print(antonio.olhos)
    print(id(Pessoa.olhos), id(marco.olhos), id(antonio.olhos))
    print(Pessoa.metodo_estatico(), marco.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), marco.nome_e_atributos_de_classe())