# s = "the sky is blue"
s = "a good   example"
# s = "  hello world  "

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    sArr = []
    sArrRev = []
    sRev =""
    for i in s:
        sArr.append(i)
    
    i = len(sArr)-1
    endpoint = i
    flag = 0
    while i >= 0:
        if (sArr[i] == ' ' or i == 0):
            j = i+1
            if i == 0:
                j = 0
            while j <= endpoint:
                sArrRev.append(sArr[j])
                j += 1
            if (i != 0):
                sArrRev.append(sArr[i])
            if i>0:
                endpoint = i-1
            if i == 0:
                j = 0
        i -= 1

    i = 0
    l= len(sArrRev)
    while i < len(sArrRev):
        

        if (sArrRev[0] == ' '):
            sArrRev.pop(0)
            l = len(sArrRev)
        elif(sArrRev[l-1] == ' '):
            sArrRev.pop(l-1)
            l = len(sArrRev)
        else:
            i += 1

    i = 1
    l= len(sArrRev)-1
    while i < l:
        
        if (sArrRev[i] == ' ' and sArrRev[i+1] == ' '):
            sArrRev.pop(i+1)
            l = len(sArrRev)
        
        else:
            i += 1

        

    for i in sArrRev:
        sRev += i

    print(sArr)
    print(sArrRev)
    print(sRev)
        
reverseWords(s)