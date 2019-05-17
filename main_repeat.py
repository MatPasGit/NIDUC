from niduc import signalCompare
from niduc import signalDisruption
from niduc import fillArray
from niduc import signalReadrepeat

length=5
def main():

    savefile = open('dane_humming.txt', 'w')
    errorfile = open('error_humming.txt','w')
    boolean=True
    count=0
    #appended=False
    while(boolean):
        count+=1
        #użyszkodnik
        print("ENTER YOUR BINARY MESSAGE")
        try:
            mode=(input('Input:'))
        except ValueError:
            print("Not a number")
            #fillarray
            #array=fillArray(12)
        
        mainarray = []
        sendarray = []   
        
        for i in mode:
            mainarray.append(int(i))
     #pętla ogarniająca przesył
        print(mainarray)
        for i in range(0,len(mainarray)) :
            bit=mainarray[i]
            array=fillArray(length,bit)
            print(array)
            disrupted=signalDisruption(array)
            print(disrupted)

            errorfile.write(str(i))
            errorfile.write(str(disrupted))
       
            number = signalReadrepeat(disrupted)
            sendarray.append(number)
    
        savefile.write(str(count))
        savefile.write(str(mainarray))
        savefile.write(str(sendarray))

        check=signalCompare(mainarray,sendarray)    

        print("send result:", check)  
        choice=input('Wanna stop? type yes:')
        if choice=='yes':
            boolean=False
        else: boolean==True      
   
    return 0
      
      
main()
      

      
      #tutaj jest źle XDDD  
    #if len(array)%2==1:
        #array.append(1)
        #appended=True
    #else: appended=False
    #disrupted=signalDisruption(array)
    #if appended==True:
        #del array[len(array-1)]
        #del disrupted[len(disrupted-1)]
    #comparison=signalCompare(array,disrupted)
    #if comparison==True
        #print("Message sent properly")
    #else: print ("not"
  
