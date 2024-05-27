flowerbed = [1,0,0,0,1]
n = 2

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if n==0:
        return True
    if len(flowerbed)>1:
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
            if n==0:
                return (n==0)
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            if n==0:
                return (n==0)
    else:
        if flowerbed[0] == 0:
            flowerbed[0] = 1
            n -= 1
            if n==0:
                return (n==0)

    i = 1
    while i < len(flowerbed)-1:
        if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1
            if n==0:
                break        
        i += 1
    return (n==0)


result = canPlaceFlowers(flowerbed, n)
print(result)