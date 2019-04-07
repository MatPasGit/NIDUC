from niduc import signalCompare
from niduc import signalDisruption
from niduc import fillArray

def main():
    boolean=True
    appended=False
    while(boolean):
        #użyszkodnik
        print("ENTER YOUR BINARY MESSAGE")
        try:
            mode=(input('Input:'))
        except ValueError:
            print("Not a number")
            #fillarray
            #array=fillArray(12)
    array = []   
    for i in mode:
        array.append(i)
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      #tutaj jest źle XDDD  
    if len(array)%2==1:
        array.append(1)
        appended=True
    else: appended=False    
    
    disrupted=signalDisruption(array)
    if appended==True:
        del array[len(array-1)]
        del disrupted[len(disrupted-1)]
    comparison=signalCompare(array,disrupted)
    if comparison==True
        print("Message sent properly")
    else: print ("not")




    

main()
