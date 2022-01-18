def loop(pstart, pend):
    """Ceci est le commentaire de boucle"""
    a = "chaine"
    for i in range(pstart, pend):
        if (i % 2) == 0:
            a = a + str(i)
            assert isinstance(a, object)
            print(a)


def firstfunction(ptexte):
    """Ceci est la chaine de commentaire"""
    print(ptexte)


def essai_dictionnaire():
    """" Ceci est un essai de dictionnaire"""
    mon_dico = {3: "Premiere Valeur", 4: "Seconde Valeur"}  # initializing data
    for k, v in mon_dico.items():
        print(k, v)