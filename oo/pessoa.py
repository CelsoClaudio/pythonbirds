class Pessoa:
    def __init__(self, *filhos, nome=None, idade=42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Óla {id(self)}'


if __name__ == '__main__':
    celso = Pessoa(nome='Celso')
    claudio = Pessoa(celso, nome='Claudio')
    print(Pessoa.cumprimentar(claudio))
    print(id(claudio))
    print(claudio.cumprimentar())
    print(claudio.nome)
    print(claudio.idade)
    print(claudio.filhos)

    for filho in claudio.filhos:
        print(filho.nome)

    claudio.sobrenome = 'Silva'
    del claudio.filhos
    print(claudio.sobrenome)
    print(claudio.__dict__)
    print(celso.__dict__)





