nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = len(nums1)
n = len(nums2)

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if (n==0):
        exit
    elif (m==0):
        i=m-n
        j=0
        while (i<m):
            nums1[i] = nums2[j]
            i+=1
            j+=1
        exit
    else:
        i=m-n
        j=0
        while (i<m):
            nums1[i] = nums2[j]
            i+=1
            j+=1

        j = m-n
        while(j<m):
            flag = True
            k = j
            while(flag and k>0):
                if (nums1[k] < nums1[k-1]):
                    nums1[k], nums1[k-1] = nums1[k-1], nums1[k]
                    k-=1
                else:
                    flag = False
                    j+=1      

result = merge(nums1, m, nums2, n)
