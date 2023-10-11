def bin_search(arr, x, l, r):
    if l>r:
        return -1
    m =  (l + r) // 2

    if arr[m] == x:
        return m
    
    elif arr[m] > x:
        return bin_search(arr, x, l, m-1)

    else:
        return bin_search(arr, x, m+1, r)

arr = [1, 2 , 3 ,5 , 7 , 9 , 11 , 21 , 23 , 27 , 29]
x = 9
res = bin_search(arr, x , 0 , len(arr)-1)

if res != -1:
    print("Element found at index",res)
else:
    print("Element not found ")