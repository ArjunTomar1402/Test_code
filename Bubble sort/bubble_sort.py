def bub_sort(l):
    n = len(l)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]


list1 = [99, 25, 28, 12, 45, 69, 80]

print("Unsorted List: ", list1)
    
bub_sort(list1)
    
print("Sorted List: ", list1)
