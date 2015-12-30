#  Wzorowane na przykładzie Rona Zacharskiego
#

from math import sqrt

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

def pearson(rating1, rating2):
    korelacja=0

    Exy = 0
    Ex = 0
    Ey = 0
    Ex2 = 0
    Ey2 = 0
    n = 0
    for klucz in rating1.keys():
        if klucz in rating2.keys():
            n = n + 1
            x = rating1[klucz]
            y = rating2[klucz]
            Exy += x * y
            Ex += x
            Ey += y
            Ex2 += pow(x, 2)
            Ey2 += pow(y, 2)
    korelacja = (Exy - (Ex * Ey) / n) / (sqrt(Ex2 - pow(Ex, 2) / n) * sqrt(Ey2 - pow(Ey, 2) / n))
    return korelacja

def pearsonNumpy(rating1, rating2):

    korelacja=0
    x=[]
    y=[]
    for klucz in rating1.keys():
        if klucz in rating2.keys():
            x.append(rating1[klucz])
            y.append(rating2[klucz])
    korelacja = numpy.corrcoef(x,y)[0,1]
    return korelacja