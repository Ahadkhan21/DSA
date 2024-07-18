array = [ 7, 5, 1, 3, 6, 4, 2]

def sort(arr):
    for i in range(1,len(arr)):
        target = arr[i]
        j = i-1
        while j >= 0 and arr[j]>target:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = target             
    return arr

print(sort(array))