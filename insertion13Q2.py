def insertionSort(tmpList, boolean=False, dbg=True):
    # Insertion Sort​
    # 1. Initialise an unsorted list​
    tmpList= [9,2,3,1,5,6,7,3,4,5]
    # 2. Initialise a marker​
    marker = 1
    # 3. Traverse through all list items​

    while (marker < len(tmpList)):

        # 4. Insert the selected item to its correct position​

        j = marker
        if boolean==True:
            while (tmpList[j] < tmpList[j-1] and j>0):
                L = tmpList[j]
                tmpList[j] = tmpList[j-1]
                tmpList[j-1] = L
                j = j-1
        # 6. Advance the marker to the right by 1 position
            marker = marker+1
            print(tmpList)
          
        else:
            while (tmpList[j] > tmpList[j-1] and j>0):
                L = tmpList[j]
                tmpList[j] = tmpList[j-1]
                tmpList[j-1] = L
                j = j-1
        # 6. Advance the marker to the right by 1 position
            marker = marker+1
            print(tmpList)
        
W= [9,2,3,1,5,6,7,3,4,5]
insertionSort(W, dbg=False)

def bubbleSort(tmpList, boolean=False, dbg=True):
    
    if dbg==True:
        #print('Log4.txt','w')    
        print("INPUT (initial list): "+ str(tmpList))
    
    exchange = True
    n= len(tmpList)
    i=0

    while (i< n) and  exchange:
        #if dbg==True:
            #print('\n'+"BEFORE PASS:"+ str(i+1)+str(tmpList))
        exchange = False
        
        for j in range(n-i-1):
            #if dbg==True:
                #print('\n'+"%s "+str(tmpList)+"-> ")
            if boolean== True:  
                if tmpList[j] > tmpList[j+1]:
                    tmpList[j], tmpList[j+1] = tmpList[j+1], tmpList[j]
                    exchange = True
            else:
                if tmpList[j] < tmpList[j+1]:
                    tmpList[j], tmpList[j+1] = tmpList[j+1], tmpList[j]
                    exchange = True
            #if dbg==True:
                #print('\n'+"%s "+ str(tmpList))
        if dbg==True:    
            print('\n'+"AFTER PASS: "+str(i+1)+str(tmpList))
        i=i+1
    if dbg==True:    
        print('\n'+"OUTPUT (sorted list): "+str(tmpList))
        print('\n'+str(tmpList)+'\n')

W= [9,2,3,1,5,6,7,3,4,5]
bubbleSort(W, dbg=True)
 