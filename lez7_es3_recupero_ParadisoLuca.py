from math import sqrt

class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def to_string(self):
        return f"{self.x}, {self.y}"

class Punti2D:
    def __init__(self):
        self.list = []

    def aggiungi_punto(self, punto):
        self.list.append(punto)

    def baricentro(self):
        x_g, y_g = 0,0
        for p in self.list:
            x_g += p.get_x()
            y_g += p.get_y()
        return Punto2D(x_g / len(self.list), y_g/len(self.list))

    def stampa_baricentro(self):
        bar = self.baricentro()
        print(bar.to_string())





def main():
    fname = input("nome del file")
    punti = Punti2D()

    try:
        fin = open(fname, "r")

        for line in fin:
            x, y = line.split()
            x = float(x)
            y = float(y)
            punti.aggiungi_punto(Punto2D(x,y))

        punti.stampa_baricentro()
    except FileNotFoundError as e:
        print("Errore: File non trovato")
        exit(1)
    except IOError as e:
        print("Errore: Impossibile aprire il file")
        exit(2)



main()
            


