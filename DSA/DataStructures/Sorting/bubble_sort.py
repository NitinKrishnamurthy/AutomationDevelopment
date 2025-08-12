l = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort_basic(l):
    n = len(l)
    for i in range(n):
        for j in range(n-1-i):
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
    return l

def bubble_sort_optimized(l):
    n = len(l)
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]

        if not swapped:
            break
    return l

def bubble_sort_advanced(l):
    n = len(l)

    while n > 0:
        new_n = 0
        for j in range(0,n-1):
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
                new_n = j
        n = new_n



