import numpy as np
#from numpy import *
import random

weighted_random = [1] * 60 + [0] * 40
def fillArray(i,elem):
    if i%2==0:
        i+=1
    #number = random.randint(0, 1)
    array = []
    for i in range(0,i):
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
        if rand[i]> 0.1 :
            if random.choice(weighted_random)== 1:
                newarray[i]='1'
            else:
                newarray[i]='0'
    
        #to juz final version XD
    for i in range(0,len(newarray)):
        newarray[i] = int(newarray[i])
    return newarray

#porównanie tablic 
def signalCompare(array0,array1):
    
    if array0==array1:
        return True
    else:
        return False
        

# odczytywanie bitu z powielenia po transmisji 
def signalReadrepeat(array0):
    sum=0
    for f in array0:
        sum += f
    num0=len(array0)
    
    if sum >(num0/2) :
        first_signal=1 
    else :
        first_signal=0
    return first_signal     


def parity(parity, array):
    parity1=[]
    for i in range(0, len(array)-1):
        for n in range(0, len(parity)-1):
            if parity[n] == i:
                parity1.append(array[i])

        sum1 = 0
        for i in parity1:
            sum1 = +i
        if+- sum1 % 2 == 0:
            parity11 = 0
        else: parity11 = 1

    return parity11 
    
def signalReadhamming(array):
    parity1=[2,4,6,8,10,12,14]
    parity11=parity(parity1,array)  
    parity2=[2,5,6,9,10,13,14]
    parity22=parity(parity2,array)
    parity3=[4,5,6,11,12,13,14]
    parity33 = parity(parity3,array)
    parity4=[8,9,10,11,12,13,14]
    parity44 = parity(parity4,array)

    false_bit=-1
    if array[0]==parity11:
        false_bit+=1
    
    if array[1]==parity22:
        false_bit+=2    
    
    if array[3] ==parity33:
        false_bit += 4
    
    if array[7] == parity44:
        false_bit += 8
    
    if false_bit == -1:
        print("everything correct")
    else: 
        if array[false_bit]==1:
               array[false_bit]=0
        else:
            array[false_bit]=1

    
    return array

def hammingCompare(array0,array1):
    binary_var=True 
    for i in range(0,14):
        if array0[i]!=array1[i]:
            binary_var=False
        
    return binary_var