def F(month, k):
    if month==0:
        return 0
    if month==1:
        return 1

    return F(month-1, k) + k*F(month-2, k)

print(F(28, 5))