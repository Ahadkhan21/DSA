str1 = "FFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKST"
str2 = "FFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKSTFFBNXKST"

def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    l1 = len(str1)
    l2 = len(str2)
    if l1 > l2:
        small = l2
    else:
        small = l1
    for i in range(1, small + 1):
        if((l1 % i == 0) and (l2 % i == 0)):
            gcd = i

    if str1 + str2 != str2 + str1:
        return ''
            
    if (len(str1) >= len(str2)):
        i=0
        j=0
        while i < len(str1):
            if (str1[i] == str2[j]):
                i += 1
                j += 1
                if (j==len(str2)):
                    j=0
            else:
                return ''

        if (len(str2) == len(str1)//2 or len(str2) == len(str1)):
            return str2

        i = 1
        pos = [str2[0]]
        while i < len(str2):
            if (str2[i] == str2[0]):
                pos.append(i)
            i+=1

        if (len(pos) == 1):
            return str2
        elif (len(pos) == 2):
            x1 = str2[:pos[1]]
            x2 = str2[pos[1]:]
            if x1 == x2:
                    return x1
        else:
            i = 1
            while i < len(pos):
                x1 = str2[:pos[i]]
                print(x1)
                k=0
                j=0
                flag = 1
                while k < len(str2):
                    if (str2[k] == x1[j]):
                        k += 1
                        j += 1
                        if (j==len(x1)):
                            j=0
                    else:
                        k = len(str2)
                        flag = 0
                if flag == 1 and len(x1) == gcd:
                    return x1
                else:
                    i += 1
    else:
        i=0
        j=0
        while i < len(str2):
            if (str2[i] == str1[j]):
                i += 1
                j += 1
                if (j==len(str1)):
                    j=0
            else:
                return ''

        if (len(str2) == len(str1)//2 or len(str2) == len(str1)):
            return str2

        i = 1
        pos = [str1[0]]
        while i < len(str1):
            if (str1[i] == str1[0]):
                pos.append(i)
            i+=1

        if (len(pos) == 1):
            return str1
        elif (len(pos) == 2):
            x1 = str1[:pos[1]]
            x2 = str1[pos[1]:]
            if x1 == x2:
                    return x1
        else:
            i = 1
            while i < len(pos):
                x1 = str1[:pos[i]]
                print(x1)
                k=0
                j=0
                flag = 1
                while k < len(str1):
                    if (str1[k] == x1[j]):
                        k += 1
                        j += 1
                        if (j==len(x1)):
                            j=0
                    else:
                        k = len(str1)
                        flag = 0
                if flag == 1  and len(x1) == gcd:
                    return x1
                else:
                    i += 1


result = gcdOfStrings(str1, str2)
print('result: ',result)