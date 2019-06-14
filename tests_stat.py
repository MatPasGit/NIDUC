from niduc import signalCompare
from niduc import signalDisruption
from niduc import fillArray
from niduc import signalReadrepeat
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import scipy.stats
import pylab
pylab.style.use('seaborn-whitegrid')


def tests(length, howmuch):
    
    averagelist=[] #lista do liczenia średniej

    ones=0  #ilość przekłamać na jedynki
    zeros=0 #ilosć przekłamań na zera
    falsebits = 0

    """
    try :
        length = (input('Ile powieleń:'))
    except ValueError:
        print("Not a number")

    length=int(length)   

    try:
        howmuch = (input('Ile bitów :'))
    except ValueError:
        print("Not a number")
    """
    
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

    average = round(average, 4)
    odchyl = round(odchyl, 6)
    return average, odchyl

def make_stats():
    tab_packets = []
    pack_average = []
    pack_odchyl = []

    tab_size = []
    size_average = []
    size_odchyl = []
    
    for x in range(5, 70):
        actual_result = tests(x, 50)
        pack_average.append(actual_result[0])
        pack_odchyl.append(actual_result[1])
        tab_packets.append(x)
        
        
    for y in range(10, 80):
        actual_result = tests(60, x)
        size_average.append(actual_result[0])
        size_odchyl.append(actual_result[1])
        tab_size.append(y)
        
    print(tab_packets)
    print(pack_average)
    print(pack_odchyl)
    print(tab_size)
    print(size_average)
    print(size_odchyl)

    plt.subplot(211)
    
    plt.title('Wykres sredniej ilosci błędów od ilości pakietów')
    plt.errorbar(tab_packets,pack_average, yerr=pack_odchyl, linestyle="solid", fmt='-', color='g', ecolor='xkcd:salmon', elinewidth=1.5, capsize=3, capthick=1)
    plt.xlabel("Liczba pakietów")
    plt.ylabel("Srednia ilosć błędów")
    plt.xticks(range(5, x+1))

    plt.subplot(212)
    plt.title('Wykres sredniej ilosci błędów od wielkosci pakietów')
    plt.errorbar(tab_size,size_average, yerr=size_odchyl, linestyle="solid", fmt='-', color='g', ecolor='xkcd:salmon', elinewidth=1.5, capsize=3, capthick=1)
    plt.xlabel("Wielkosć pakietów")
    plt.ylabel("Srednia ilosć błędów")

    plt.subplots_adjust(top=0.92, bottom=0.18, left=0.10, right=0.95, hspace=0.65,
                    wspace=0.35)

    plt.xticks(range(10, y+1))
    plt.show()
    
make_stats()    
"""      
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


    result = plt.hist(averagelist)
        
    mean = np.mean(averagelist)
    variance = np.var(averagelist)
    sigma = np.sqrt(variance)
    x = np.linspace(min(averagelist), max(averagelist), 100)
    dx = result[1][1] - result[1][0]
    scale = len(averagelist)*dx
    plt.plot(x, scipy.stats.norm.pdf(x, mean, sigma)*scale)

    plt.xlabel("Number of errors")
    plt.ylabel("Incidence of errors")
    
    #plt.show()

"""
    


    



