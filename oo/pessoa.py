class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'







if __name__ == '__main__':
    camillo = Pessoa(nome='Camillo')
    hugo = Pessoa(camillo, nome='Hugo')
    print(Pessoa.cumprimentar(hugo))
    print(id(hugo))
    print(hugo.cumprimentar())
    print(hugo.nome)
    print(hugo.idade)
    for filho in hugo.filhos:
        print(filho.nome)
    hugo.sobrenome = 'Barbosa'
    del hugo.filhos
    hugo.olhos = 1
    del hugo.olhos
    print(hugo.__dict__)
    print(camillo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(hugo.olhos)
    print(camillo.olhos)
    print(id(Pessoa.olhos), id(hugo.olhos), id(camillo.olhos))
    print(Pessoa.metodo_estatico(), hugo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), hugo.metodo_estatico())