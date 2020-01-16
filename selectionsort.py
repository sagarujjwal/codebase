def selectionsort(list):
    n=len(list)
    for i in range(n-1):
        smallNdx=i
        for j in range(i+1,n):
            if list[j]<list[smallNdx]:
                smallNdx=j

            if smallNdx !=i:
                print('2')
                tmp=list[i]
                list[i]=list[smallNdx]
                list[smallNdx]=tmp

list=[123,4,56,56,78,8]
selectionsort(list)
print(list)





def selectionSort(alist):

   for i in range(len(alist)):

      # Find the minimum element in remaining
       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j

       # Swap the found minimum element with minPosition
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist

print(selectionSort([5,2,1,9,0,4,6]))
