def find_square_roots(arr):
   result = []
    
   for num in arr:
        if num < 0:
            raise ValueError("Cannot compute square root of a negative number")
        if num == 0 or num == 1:
            result.append(num)
        else:
            left, right = 1, num
            while left <= right:
                mid = (left + right) // 2
                mid_squared = mid * mid
                
                if mid_squared == num:
                    result.append(mid)
                    break
                elif mid_squared < num:
                    left = mid + 1
                else:
                    right = mid - 1

            if mid_squared > num:
                if (mid * mid - num) < ((mid + 1) * (mid + 1) - num):
                    result.append(mid)
                else:
                    result.append(mid + 1)
            else:
                result.append(mid)
    
   return result

arr = [10, 20, 30, 40, 50, 80, 90, 1000]
square_roots = find_square_roots(arr)
print("Square Roots:", square_roots)