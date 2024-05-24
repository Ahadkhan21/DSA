haystack = "mississippi"
needle  = "issipi"

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    result = -1
    flag = 0
    haystackArray = []
    needleArray =[]
    index =[]

    for i in haystack:
        haystackArray.append(i)

    for i in needle:
        needleArray.append(i)

    print(haystackArray)
    print(needleArray)

    i = 0
    while i < len(haystackArray):
        if haystackArray[i] == needleArray[0]:
            index.append(i)
        i += 1

        
    if (len(needleArray) > len(haystackArray)) or len(index) == 0:
        return result

        
    i = 0
    j = index[i]
    k = 0
    while i < len(index):
        print(index[i],j,k)
        print(haystackArray[j], needleArray[k])

        if (haystackArray[j] != needleArray[k]):
            i += 1
            k = 0
            flag = 0
            result = -1
            if i == len(index):
                break
            j = index[i]
        elif (haystackArray[j] == needleArray[k]):
            # print (j, k)
            if flag == 0:
                r = j
                flag = 1
            j += 1
            k += 1
            if k == len(needleArray):
                result = r
                break
            if j == len(haystackArray):
                break
                
    print(result)

strStr(haystack, needle)