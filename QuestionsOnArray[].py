from array import *

'''
def fix(A,len):
    import pdb; pdb.set_trace()
    for i in range(0,len):
        if (A[i] != -1 and A[i] != i):
            x=A[i];

            # check if desired place is not vacate
            while (A[x] != -1 and A[x] !=x):
                #store the value from desired place
                y=A[x]
                # place the x to its correct # position
                A[x]=x
                # now y will become x, now search the place for x
                x=y
            # place the x to its correct position
            A[x]=x;
            # check if while loop hasn't set the correct value at A[i]
            if (A[i] != i):
                 # if not then put -1 at the vacated place
                 A[i] =-1;

def fix(A):
    s = set()

    # Storing all the values in the Set
    for i in range(len(A)):
        s.add(A[i])

    for i in range(len(A)):
        # check for item if present in set
        if i in s:
            A[i] = i
        else:
            A[i] = -1
    return A

# Driver function.
A = array('i',[ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ])

#fix(A, len(A))
fix(A)
print(A)



def fix(A,len):
    for i in range(0,len):
        if (A[i]!=-1 and A[i]!=i):
            x=A[i]
            while (A[x]!=-1 and A[x]!=x):
                y=A[x]
                A[x]=x
                x=y
            A[x]=x
            if A[i]!=i:
                A[i]=-1


A = array('i',[ 5, -1, 7, 1, 9, 3, 2, -1, 4, -1 ])

fix(A, len(A))
print(A)
'''

#Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

def leftRotatebyOne(arr, n):
    #import pdb; pdb.set_trace();
    tmp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=tmp
    return arr

def leftRotate(arr,d,n):
    # pdb; pdb.set_trace();
    for i in range(d):
        b=leftRotatebyOne(arr,n)
    return b


arr=[1,2,3,4,5,6,7]
n=len(arr)
d=4
# A=leftRotatebyOne(arr,n)
A=leftRotate(arr,d,n)
#print(A)


def rightRotatebyoOne(arr,n):
    tmp=arr[-1]
    for i in range(1,n):
        arr[-i]=arr[-i-1]
    arr[0]=tmp
    return arr


def rightRotate(arr,d,n):
    # pdb; pdb.set_trace();
    for i in range(d):
        b=rightRotatebyoOne(arr,n)
    return b

arr=[1,2,3,4,5,6,7]
n=len(arr)
d=2
# A=rightRotatebyoOne(arr,n)
A=rightRotate(arr,d,n)
print(A)
