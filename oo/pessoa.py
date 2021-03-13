class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=42):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Óla {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    claudio.olhos = 1
    del claudio.olhos
    print(claudio.sobrenome)
    print(claudio.__dict__)
    print(celso.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(celso.olhos)
    print(claudio.olhos)
    print(id(Pessoa.olhos), id(celso.olhos), id(claudio.olhos))
    print(Pessoa.metodo_estatico(), celso.metodo_estatico(), claudio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), celso.nome_e_atributos_de_classe(), claudio.nome_e_atributos_de_classe())
