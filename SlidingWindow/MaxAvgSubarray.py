nums = [1,12,-5,-6,50,3]
k = 4


def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    windowSum = sum(nums[:k])
    maxSum = windowSum

    for i in range(k,len(nums)):
        windowSum += nums[i] - nums[i-k]
        maxSum = max(windowSum, maxSum)

    return maxSum/float(k)

print(findMaxAverage(nums, k))