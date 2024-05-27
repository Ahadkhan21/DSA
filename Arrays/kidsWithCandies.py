candies = [2,3,5,1,3]   
extraCandies = 3

def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    res = []
    highest = max(candies)
    for i in candies:
        res.append(i + extraCandies >= highest)
        
    return res

    
result = kidsWithCandies(candies, extraCandies)
print(result)