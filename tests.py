from niduc import signalCompare
from niduc import signalDisruption
from niduc import fillArray
from niduc import signalReadrepeat
import random



def tests():
    ones=0
    zeros=0
    try:
        lenght = (input('transmission lengh:'))
    except ValueError:
        print("Not a number")
       

    try:
        howmuch = (input('WIE VIELE TIMES:'))
    except ValueError:
        print("Not a number")
    #tablica testowa wypełniona losowo 
    testarray=[]    
    for i in range(1,howmuch):
        weighted_random = [1] * 50 + [0] * 50 
        if random.choice(weighted_random) == 1:
            testarray.append(1)
        else:
            testarray.append(0)
    #tablica z indeksami (do wykresu)
    indexarray=[]
    for i in range(1,howmuch):
        indexarray[i]=i
#tutaj zaczynamy testowanie 
#pętla sprawdza sto razy ileś bitów