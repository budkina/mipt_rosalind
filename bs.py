def binary_search(el, A, start_index):
    if len(A) == 0:
        return -1
    if len(A) == 1 and el != A[0]:
        return -1
    i_median = len(A)//2
    if el == A[i_median]:
        return start_index+i_median+1
    if el < A[i_median]:
        return binary_search(el, A[:i_median], start_index)
    if el > A[i_median]:
        return binary_search(el, A[i_median+1:], start_index+i_median+1)

f = open("rosalind_bins.txt", "r")
n = f.readline()
m = f.readline()
A_str = f.readline()
B_str = f.readline()
f.close()

A=list(map(float, A_str.split()))
B=list(map(float, B_str.split()))

indexes = []

for el in B:
	indexes.append(binary_search(el,A,0))

f = open("rosalind_bins_res.txt", "w")
f.write( ' '.join(map(str, indexes)))
f.close()