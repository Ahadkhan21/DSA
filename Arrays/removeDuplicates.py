nums = [0,0,1,1,1,1,2,3,3]

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    i = 0
    l = len(nums)
    count = 0
    currentElement = nums[0]
    while i < l:
        print("i:",i , " nums[i]:",nums[i], " currentElement:",currentElement, nums[i] == currentElement)
        if (nums[i] == currentElement):
            count += 1
            print("count:", count)
            if count > 2:
                nums.remove(nums[i])
                count -= 1
                l = len(nums)
            else:
                i+=1
        elif(nums[i] != currentElement):
            currentElement = nums[i]
            count = 1
            i += 1
    print(nums)

removeDuplicates(nums)