import numpy as np
import random

weighted_random = [1] * 60 + [0] * 40
#ta funkcja okazała sie bez sensu ale ok XD
def fillArray(i):
    if i%2==1:
        i+=1
    number = random.randint(0, 1)
    array = []
    for i in range(0,i-1):
        array.append(number)
    return array

def signalDisruption(array):
    #prawdopodobieństwo 0 -40%  prawdopodobieństwo 1 -60%
    #prawdopodobienstwo zakłócenia zwiększa sie wraz  z długością tablicy 
    newarray=array
    #elementy tablicy iterowane dalej by zwiększyć lambde
    n=array.length()
    #prawd
    p=0.05
    for i in range(1,n):
    #l to lambda rozkładu poissona
        l=p*i
        rand = np.random.poisson(l, i)
        if rand> 0.1 :
            if random.choice(weighted_random)== 1:
                newarray[i-1]=1
            else:
                newarray[i-1]=0
    
        #to jeszcze nie final version XD
    
    return newarray

def signalCompare(array0,array1):
    for f in array0:
        f+=array0
    num0=array0.len()
    num1=array1.len()
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


