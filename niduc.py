import numpy as np
import random

def fillArray(i):
    if i%2==1:
        i+=1
    number = random.randint(0, 1)
    array = []
    for i in range(0,i-1):
        array.append(number)
    return array

def signalDisruption(array):
    newarray=array
    for f in array :
    
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


