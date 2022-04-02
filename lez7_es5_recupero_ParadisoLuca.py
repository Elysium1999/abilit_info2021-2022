def prodotto_scalare(lista1,lista2):

    p_s=0

    if(len(lista1)!=len(lista2)):
        raise Exception("Errore: le liste hanno dimensione diversa")
    else:
        for i in range(0, len(lista1)):
            if type(lista1[i])==int or type(lista1[i])==float and type(lista2[i])==int or type(lista2[i])==float:
                p_s += lista1[i] * lista2[i]
            else:
                raise Exception("Errore: le componenti delle liste non sono numeri")
    return p_s
#considero anche il caso che un utente distratto possa decidere di fare il prodotto scalare tra due liste che non contengano numeri, magari un errore nel programma che genera la lista produce dei valori Nan

def crea_matrice(righe,colonne):
   matrice=[]
   for r in range(righe):
      riga=[]
      for c in range(colonne):
         riga.append(0)
      matrice.append(riga)
   return matrice

def prodotto_matrici(matrice1,matrice2):

    righe1 = len(matrice1)
    colonne1 = len(matrice1[0])
    righe2 = len(matrice2)
    colonne2 = len(matrice2[0])

    if(colonne1)!=righe2:
        raise Exception("Errore: le matrici non sono moltiplicabili")

    matrice_prodotto = crea_matrice(righe1, colonne2)
    for riga in range(righe1):
       for colonna in range(colonne2):
           somma = 0
           for i in range(colonne1):
               somma += matrice1[riga][i] * matrice2[i][colonna]
               matrice_prodotto[riga][colonna] = somma
    return matrice_prodotto






def main():
    lista1 = [2,0,0,1,-1]
    lista2 = [-2,2,1,0,0]

    print(prodotto_scalare(lista1,lista2))

    matrice1=[ [1,3], [2,0] ]
    matrice2=[ [1,-1], [-2,0] ]
    matrice3=[ [1,0,1], [2,0,-1], [-1,-1,-2]]

    print(prodotto_matrici(matrice3, matrice3))
    print(prodotto_matrici(matrice1, matrice2))
    print(prodotto_matrici(matrice3, matrice2))


main()