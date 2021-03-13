class Pessoa:
    def __init__(self, nome=None, idade=42):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Óla'


if __name__ == '__main__':
    p = Pessoa('Celso')
    # p.nome = 'Celso'
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
