import operator

class campionato_sportivo:
    def __init__(self, squadre):
        self.squadre = squadre

    def get_nome_squadre(self):
        return self.squadre.keys()

    def get_punteggio_squadra(self, nome_squadra):
        return self.squadre[nome_squadra]

    def stampa_squadre(self):
        print(self.squadre)

    def aggiungi_squadra(self, nome_squadra, punteggio_squadra):

        if nome_squadra in self.get_nome_squadre():
            print(f"Squadra {nome_squadra} già presente")
        else:
            self.squadre[nome_squadra] = punteggio_squadra


    def cancella_squadra(self, nome_squadra):

        if nome_squadra in self.get_nome_squadre():
            del self.squadre[nome_squadra]
        else:
            print("La squadra non esiste")

    def squadra_vincitrice(self):
        punteggio_max=0
        squadra_max=''
        for s, p in self.squadre.items():
            if p > punteggio_max:
                punteggio_max = p
                squadra_max = s
        print(f"La squadra {squadra_max} vince il campionato con {punteggio_max} punti")

    def ultime_squadre(self):
        sortedSquadre = sorted(self.squadre.items(), key=operator.itemgetter(1))

        for i in range(0, len(sortedSquadre)):
            if i < 3:
                print(f"Le squadre {sortedSquadre[i][0]} arrivano {i} ultime con {sortedSquadre[i][1]} punti")
            else:
                break





def main():
    squadre = {'Milan': 24, 'Torino': 29, 'Juventus' : 30, 'Lazio' : 20, 'Inter' : 25}
    campionato = campionato_sportivo(squadre)

    campionato.aggiungi_squadra('Roma', 35)

    campionato.stampa_squadre()

    print(f"Punteggio Roma: {campionato.get_punteggio_squadra('Roma')}")

    campionato.squadra_vincitrice()

    campionato.ultime_squadre()


main()
