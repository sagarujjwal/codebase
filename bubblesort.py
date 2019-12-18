def bubblesort(list):
    n=len(list)
    for i in range(n-1,0,-1):
        print(i)
        for j in range(i):
            print(j)
            if list[j]>list[j+1]:
                tmp=list[j]
                list[j]=list[j+1]
                list[j+1]=tmp
            
        

list=[10,30,2,56,1,4,345,23,56,768,34,323,2,65,5876,879,8989,890,5654,5]
bubblesort(list)
print(list)


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
