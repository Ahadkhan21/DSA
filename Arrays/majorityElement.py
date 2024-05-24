def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (len(nums) == 1):
        return nums[0]
    nums.sort()
    majority = len(nums)/2
    count = 1
    i=0
    while i < len(nums)-1:
        if (nums[i] == nums[i+1]):
            count += 1
            if count > majority:
                return nums[i]
        else:
            count = 1
        i += 1

