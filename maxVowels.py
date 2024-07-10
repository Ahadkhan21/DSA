"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Example 2:
s = "aeiou"
k = 2

Example 3:
s = "leetcode"
k = 3
"""

#Example 1
s = "abciiidef"
k = 3

def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if s=='':
        return 0
            
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    temp=0
    sTemp = s[:k]
    for i in sTemp:
        if i in vowels:
            temp += 1
    count = temp
    for i in range(k+1,len(s)+1):
        sTemp = s[i-k : i]
        if s[i-k-1] in vowels:
            temp -= 1
        if s[i-1] in vowels:
            temp+=1
        count = max(temp, count)

    return count

result = maxVowels(s, k)
print (result)