def shadoktodec(chaine):
    shadok =["GA" , "BU" , "ZO" , "MEU"] #shadok est une liste
    #GA=0. BU=1. ZO=2. MEU=3.
    chaine = chaine.split(" ") # les différents caractères sont séparés par des espaces.     
    resultat = 0
    rang = 0
    for i in reversed(chaine) : # reversed permet de prendre la liste à partir du dernier rang.
        print(i)
        for j in range(4) :
            print(j)
            if i == shadok[j] :
                resultat = resultat + j*4**rang
                rang += 1
    return (resultat)
print("Voila le résultat:   ", shadoktodec("MEU BU ZO ZO GA"))
#================================== DEJA COMPRIS+++++