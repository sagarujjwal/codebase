#https://www.pythoncentral.io/insertion-sort-implementation-guide/
def insertionSort(alist):

   for i in range(1,len(alist)):

       #element to be compared
       current = alist[i]

       #comparing the current element with the sorted portion and swapping
       while i>0 and alist[i-1]>current:
           alist[i] = alist[i-1]
           i = i-1
          alist[i] = current

       #print(alist)

   return alist


def insertionsor(list):
    n=len(list)
    for i in range(1,n):
        value=list[i]
        print('value',value)
        pos=i
        print('pos',pos)
        while pos>0 and list[pos-1]:
            list[pos]=list[pos-1]
            pos-=1
        list[pos]=value
    
list=[9,3,7,6,5,4,3,2,1]
insertionsor(list)
print(list)


def insertionsort(list):
    n=len(list)
    for i in range(1,n):
        j=i-1
        print('j',j)
        while list[j]>list[j+1] and j>0:
            print('whil1')
            list[j],list[j+1]=list[j+1],list[j]
            j-=1
    
list=[9,3,7,6,5,4,3,2,1]
insertionsort(list)
print(list)
