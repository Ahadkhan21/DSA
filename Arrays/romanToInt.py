s = "MCMXCIV"

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    l = []
    for i in s:
        if (i == 'I'):
            l.append(1)
        if (i == 'V'):
            l.append(5)
        if (i == 'X'):
            l.append(10)
        if (i == 'L'):
            l.append(50)
        if (i == 'C'):
            l.append(100)
        if (i == 'D'):
            l.append(500)
        if (i == 'M'):
            l.append(1000)
    numInt = 0
    i=0
    while i<len(l):
        if (i < len(l)-1):
            if l[i]<l[i+1]:
                numInt +=  l[i+1]-l[i]
                i += 2
            else:
                numInt += l[i]
                i += 1
        else:
            numInt += l[i]
            i += 1

    print(l)
    print(numInt)

romanToInt(s)