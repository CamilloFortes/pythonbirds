class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=38):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

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