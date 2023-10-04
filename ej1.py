class Matriz:
    def __init__(self, elementos):
        self.elementos = elementos

    def transponer(self):
        pass

    def imprimir(self):
        for fila in self.elementos:
            print(fila)

class Transpuesta:
    def __init__(self, matriz):
        self.matriz = matriz

    def transponer(self):
        return Matriz([[fila[i] for fila in self.matriz.elementos] for i in range(len(self.matriz.elementos[0]))])

class Lanzador:
    def __init__(self):
        self.elementos = []
        self.cantidad_filas = int(input('Ingrese la cantidad de filas: '))
        self.cantidad_columnas = int(input('Ingrese la cantidad de columnas: '))
        self.crear_matriz()
        self.matriz = Matriz(self.elementos)
        self.transpuesta = Transpuesta(self.matriz)

    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f'Ingrese el elemento ({i+1},{j+1}): ')))
            self.elementos.append(fila)

    def lanzar(self):
        print('La matriz transpuesta es:')
        self.matriz.imprimir()
        self.transpuesta.transponer().imprimir()

class Main:
    def __init__(self):
        self.lanzador = Lanzador()
        self.lanzador.lanzar()

if __name__ == '__main__':
    Main()

