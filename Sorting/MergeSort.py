array = [ 7, 5, 3, 1, 6, 4, 2]

def divide(array):
    if len(array) <= 1:
        return array
    arr1 = divide(array[:len(array)//2])
    arr2 = divide(array[len(array)//2:])
    return merge(arr1, arr2)

def merge(arr1, arr2):
    result = []
    l = r = 0
    while (l<len(arr1) and r<len(arr2)):
        if arr1[l]>arr2[r]:
            result.append(arr2[r])
            r += 1
        else:
            result.append(arr1[l])
            l += 1
    result.extend(arr1[l:])
    result.extend(arr2[r:])
    return result
    
s = divide(array)
print(s)