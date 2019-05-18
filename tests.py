from niduc import signalCompare
from niduc import signalDisruption
from niduc import fillArray
from niduc import signalReadrepeat
import random
import numpy as np
import matplotlib.pyplot as plt


def tests():
    ones=0  #ilość przekłamać na jedynki
    zeros=0 #ilosć przekłamań na zera
  
    try :
        length = (input('Ile powieleń:'))
    except ValueError:
        print("Not a number")

    length=int(length)   

    try:
        howmuch = (input('Ile bitów :'))
    except ValueError:
        print("Not a number")
    
    howmuch=int(howmuch)
    indexarray = []  # tablica indeksów do wykresu
    #tablica testowa wypełniona losowo 
    howmuch=int(howmuch)
    testarray=[]    
    for i in range(1,howmuch):
        weighted_random = [1] * 50 + [0] * 50 
        if random.choice(weighted_random) == 1:
            testarray.append(1)
        else:
            testarray.append(0)
    #tablica z indeksami (do wykresu)
    for i in range(0,howmuch-1):
        indexarray[i]=i

    subindexarray=indexarray    
    #tutaj zaczynamy testowanie 
    #pętla sprawdza sto razy ileś bitów
    for m in range(0,99):
        stoparray = []
        for i in range(0,len(testarray)):
            bit=testarray[i]
            onebitarray = fillArray(length, bit)
            onebitarray=signalDisruption(onebitarray)
            newbit=signalReadrepeat(onebitarray)
            stoparray.append(newbit)            #symulacja przesyłu i dopisanie do tablicy przesłanej

        for i in range(0,howmuch):
            if testarray[i] != stoparray[i]:
                indexarray[i]+=1
                if testarray[i] == 0 :
                    ones+=1
                else : zeros +=1        #porównanie tablic i analityka 

    plt.plot(subindexarray, indexarray, 'ro')
    plt.axis([0, howmuch, 0, howmuch])
    plt.show()



tests()





