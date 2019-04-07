from niduc import signalCompare
from niduc import signalDisruption
from niduc import fillArray
from niduc import signalRead

length=5
def main():

    savefile = open('dane.txt', 'w')
    errorfile = open('error.txt','w')
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
            mainarray.append(i)
     #pętla ogarniająca przesył
       
        for i in range(0,len(mainarray)-1) :
            bit=mainarray[i]
            array=fillArray(length,bit)
            disrupted=signalDisruption(array)
        
            errorfile.write(i)
            errorfile.write(disrupted)
       
            number=signalRead(disrupted)
            sendarray.append(number)
    
        savefile.write(count)
        savefile.write(mainarray)
        savefile.write(sendarray)

        check=signalCompare(mainarray,sendarray)    

        print("send result:", check)  
        choice=input('Wanna stop? type yes:')
        if choice=='y':
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
  
