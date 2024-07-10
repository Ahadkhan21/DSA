"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only 
have a single space separating the words. Do not include any extra spaces.

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
"""

s = "the sky is blue"
# s = "  hello world  "     #example 2
# s =  "a good   example"   #example 3

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    sArr = []
    sArrRev = []
    sRev = ''
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

    return sRev

result = reverseWords(s)
print (result)