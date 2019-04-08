from niduc import signalCompare
from niduc import signalDisruption
from niduc import fillArray
from niduc import signalReadhamming
from niduc import hammingCompare

length=5
def main():

    savefile = open('hamming/dane.txt', 'w')
    errorfile = open('hamming/error.txt','w')
    boolean=True
    count=0
    #appended=False
    while(boolean):
        count+=1
        #użyszkodnik
        array_len=0
        while(array_len != 15):
            print("ENTER YOUR BINARY MESSAGE 15 BIT LONG")
            try:
                mode=(input('Input:'))
            except ValueError:
                print("Not a number")
            #fillarray
            #array=fillArray(12)
            arr=list.str(mode) #zamienić inty na tablice str albo jakkolwiek zbadać ich ilosć
            array_len=len(arr)
            if array_len != 15:
                print("15 BITS MAAAAN")
            else :
                break
        
        mainarray = []
        sendarray = []   
        
        for i in mode:
            mainarray.append(int(i))
     #pętla ogarniająca przesył
        print(mainarray)
        for i in range(0,len(mainarray)-1) :
            disrupted=signalDisruption(mainarray)
            print(disrupted)

            errorfile.write(str(i))
            errorfile.write(str(disrupted))
       
            sendarray = signalReadhamming(disrupted)
            
    
      
        savefile.write(str(mainarray))
        savefile.write(str(sendarray))

        check=hammingCompare(mainarray,sendarray)    

        print("send result:", check)  
        choice=input('Wanna stop? type yes:')
        if choice=='yes':
            boolean=False
        else: boolean==True      
   
    return 0
      
      
main()
      

