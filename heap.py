def repairHeap(H,i):
    heap=H
    largestChild = 0
    
    if i >= len(H)//2:
    	return
    	
    # choose largest child element of i
    l = 2*i+1 
    r = 2*i+2
    
    largestChild = l if (heap[l] >= heap[r]) else r
    
    if (heap[i] < heap[largestChild]):
        heap[i], heap[largestChild] = heap[largestChild], heap[i]
        repairHeap (heap, largestChild)

def buildHeap(A):
    
    # alloc heap for array A len n
    n=len(A)
    array = A
    heapSize = 0

    for i in range(n):
        if heapSize>=n: break
        heapSize = heapSize + 2**i

    array = array + [float('-inf')]*(heapSize - n)
    
    # the indexes of leave elements in heap: n//2...n
    # repair heap
    i = len(array)//2
    while i>=0:
        repairHeap(array,i)
        i-=1
        
    array = list(filter(lambda x: x!= float('-inf'), array))
    
    return array

f = open("rosalind_hea.txt", "r")
n = f.readline()
A_str = f.readline()
f.close()

heap=buildHeap(list(map(int, A_str.split())))

f = open("rosalind_hea_res.txt", "w")
f.write( ' '.join(map(str, heap)))
f.close()