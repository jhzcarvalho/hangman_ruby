'''
- Lista de Palavras
    - Input do usuário ou lista de palavras geradas automáticamente
- Criar Tabela/grid
    - Tamanho da tabela
    - Tabela quadrada ou retangular
- Inserir lista de palavras
    - Gerar posição aleatória para a primeira letra da palavra
    - escolher uma direção para continuar a palavra
- Inserir letras aleátórias até preencher a tabela
'''
import random


class Grid:

    def __init__(self, linhas, colunas) -> None:
        self.grid = []
        self.linhas = linhas
        self.colunas = colunas

        for l in range(linhas):
            self.grid.append([])

            for c in range(colunas):
                self.grid[l].append(' ')

        '''
        linha = []
        for i in range(colunas):
            linha.append('')

        for i in range(linhas):
            self.grid.append(linha)
        '''

        self.imprimeGrid()

    def imprimeGrid(self) -> None:

        for i in self.grid:
            print(i)

        print()

    def alteraValor(self, linha, coluna, valor) -> None:
        self.grid[linha][coluna] = valor

        self.imprimeGrid()

    def escolheDirecao(self) -> None:
        self.direcao = (random.randint(-1, 1), random.randint(-1, 1))

    def inserePalavra(self, palavra) -> None:

        # Escolhendo a posição inicial da palavra
        pos = (random.randint(0, self.linhas), random.randint(0, self.colunas))
        while pos != (' ', ' '):
            pos = (random.randint(0, self.linhas),
                   random.randint(0, self.colunas))

        print()

        self.escolheDirecao()

        for i in range(len(palavra)):
            self.alteraValor(pos[0] + (i.), pos[1] + i, palavra[i])

        self.imprimeGrid()


if __name__ == '__main__':
    x = Grid(10, 10)

    listaPalavras = ['valor', 'futebol', 'laranja']

    x.alteraValor(1, 2, 'A')

    x.escolheDirecao()
