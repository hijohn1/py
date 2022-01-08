##################################################
                                                 #   
# CISC 3220 MW12                                 #
# HW 2 (Optional)                                #
# GuanYong Guan (23732325)                       #
                                                 #
##################################################

def mergesort(a, p, r):                             
    if p<r:                        #comparing the starting point and the ending point
        q = (p+r)//2               #divding the array into two arrays
        mergesort(a, p, q)         #recursive function 
        mergesort(a, q+1, r)
        merge(a, p, q, r)          #combining two function into one array

def merge(a, p, q, r):
    n1=q-p+1                   #set up size for left array
    n2=r-q                     #set up size for right array 
    left=[0]*n1                #defining array
    right=[0]*n2

    for i in range (0, n1):    #assigning values to the left and right array
        left[i]=a[p+i]
    for j in range (0, n2):
        right[j]=a[q+1+j]
    
    i=j=0            #set up the starting point
    k=p

    while i<n1 and j<n2:      #comparing left and right side array and then assign the value to the original array
        if left[i]<right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k]=right[j]
            j += 1
        k += 1

    while i<n1:              #assigning the rest values in the left array to the original array
        a[k] = left[i]
        i += 1
        k += 1

    while j<n2:              #assigning the rest values in the right array to the original array
        a[k] = right[j]
        j += 1
        k += 1

a=[2,1,6,3,4]           #array for sorting              
print('\nBfore the merge sort: ',a)
mergesort(a,0,4)        #calliing mergesort funtion
print('\nAfter the merge sort: ',a,'\n')
