l = [64, 34, 25, 12, 22, 11, 90]

def insertion_sort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i-1
        
        while j>=0 and l[j]>key:
            l[j+1] = key
            j -= 1
            
        l[j+1] = key