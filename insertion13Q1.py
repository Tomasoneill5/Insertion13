def insertionSort(L, boolean=True, dbg=True):
    # Insertion Sort​
    # 1. Initialise an unsorted list​
    theList = [5, 7, 3, 6, 2]
    # 2. Initialise a marker​
    marker = 1
    # 3. Traverse through all list items​

    while (marker < len(theList)):

        # 4. Insert the selected item to its correct position​

        j = marker

        if boolean==True:
            while (theList[j] < theList[j-1] and j>0):
                tmp = theList[j]
                theList[j] = theList[j-1]
                theList[j-1] = tmp
                j = j-1
        # 6. Advance the marker to the right by 1 position
            marker = marker+1
            print(theList)
          
        else:
            while (theList[j] > theList[j-1] and j>0):
                tmp = theList[j]
                theList[j] = theList[j-1]
                theList[j-1] = tmp
                j = j-1
        # 6. Advance the marker to the right by 1 position
            marker = marker+1
            print(theList)
        
W = [5, 7, 3, 6, 2]
insertionSort(W, dbg=False)
