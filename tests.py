from niduc import signalCompare
from niduc import signalDisruption
from niduc import fillArray
from niduc import signalReadrepeat
import random
import numpy as np
import matplotlib.pyplot as plt


def tests():
    averagelist=[] #lista do liczenia średniej

    ones=0  #ilość przekłamać na jedynki
    zeros=0 #ilosć przekłamań na zera
    falsebits =0
    try :
        length = (input('Ile powieleń:'))
    except ValueError:
        print("Not a number")

    length=int(length)   

    try:
        howmuch = (input('Ile bitów :'))
    except ValueError:
        print("Not a number")
    
    
    indexarray = []  # lista indeksów do wykresu
    subindexarray = []    #lista ilo10ści przekłamań na bicie
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
    for i in range(0,howmuch):
        indexarray.append(i)

    for i in range(0, howmuch):
        subindexarray.append(0)

    #print(subindexarray)
    #tutaj zaczynamy testowanie 
    #pętla sprawdza sto razy ileś bitów
    for m in range(0,99):
        stoparray = []
        averagelist.append(0)
        for i in range(0,len(testarray)):
            bit=testarray[i]
            onebitarray = fillArray(length, bit)
            onebitarray=signalDisruption(onebitarray)
            newbit=signalReadrepeat(onebitarray)
            stoparray.append(newbit)     #symulacja przesyłu i dopisanie do tablicy przesłanej
        
        
        for i in range(0,howmuch-1):
            if testarray[i] != stoparray[i]: 
                averagelist[m]+=1 
                falsebits+=1
                #subindexarray[i] +=1
                if testarray[i] == 0 :
                    ones+=1              
                else : zeros +=1        #porównanie tablic i analityka  

    average=0
    ind=0
    avsum=0
    for i in averagelist:
        ind+=1
        avsum+=i
       
    average=avsum/ind
    odchyl=0 
    for i in averagelist:
        odchyl += (i-average)**2
        odchyl /= len(averagelist)
       #ilość błędów dla zestawu danych liczyć dla przesłania parenaście razy
       

        

    plt.hist(averagelist, normed=True, bins=30)
    print("faslebits")   
    print(falsebits)
    #print("subindex")
    #print(subindexarray)
    #print(indexarray)  
    print("ones and zeros")
    print(ones)
    print(zeros)         
    print("średnia ilości błedów na próbę")
    print(average)
    print ('Wariancja to: ', odchyl)
    #plt.plot(indexarray, subindexarray)
    #plt.axis([0, howmuch, 0, howmuch/2])

    #TU PRÓBUJCIE WRZUCIĆ GAUSSA NA HISTOGRAM
    def gauss(x, *p):
        A, mu, sigma = p
        return A*np.exp(-(x-mu)**2/(2.*sigma**2))



    plt.show()



tests()





