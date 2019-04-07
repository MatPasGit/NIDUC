import numpy as np
#from numpy import *
import random

weighted_random = [1] * 60 + [0] * 40
def fillArray(i,elem):
    if i%2==1:
        i+=1
    #number = random.randint(0, 1)
    array = []
    for i in range(0,i-1):
        array.append(elem)
    return array

def signalDisruption(array):
    #prawdopodobieństwo 0 -40%  prawdopodobieństwo 1 -60%
    #prawdopodobienstwo zakłócenia zwiększa sie wraz  z długością tablicy 
    newarray=array
    #elementy tablicy iterowane dalej by zwiększyć lambde
    n=len(array)
    #prawd
    p=0.05

    l = p*n
    rand = np.random.poisson(l, n)
    for i in range(0,n):
    #l to lambda rozkładu poissona
       # l=p*i
        #print(l)
        #rand = np.random.poisson(l, i)
 
        #print(rand)
        #niżej wywala błąd
        if rand[i]> 0.1 :
            if random.choice(weighted_random)== 1:
                newarray[i]=1
            else:
                newarray[i]=0
    
        #to jeszcze nie final version XD
    
    return newarray

def signalCompare(array0,array1):
    for f in array0:
        f+=array0
    num0=len(array0)
    num1=len(array1)
    if f>(num0/2) :
        first_signal=1 
    else :
        first_signal=0

    for c in array1:
        c += array1

    if c > (num1/2):
        second_signal = 1
    else:
        second_signal = 0
    
    if first_signal == second_signal:
        return True
    else:
        return False    


def signalRead(array0):
    sum=0
    for f in array0:
        sum+=int(f)
    num0=len(array0)
    
    if f>(num0/2) :
        first_signal=1 
    else :
        first_signal=0
    return first_signal     
