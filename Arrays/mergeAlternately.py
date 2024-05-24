word1 = "ab"
word2 = "pqrs"

def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """

    merged = ""
    if (len(word1) > len(word2)):
        i = 0
        while i<len(word2):
            merged += word1[i]
            merged += word2[i]
            i += 1
        while i<len(word1):
            merged += word1[i]
            i += 1

    elif (len(word1) < len(word2)):
        i = 0
        while i<len(word1):
            merged += word1[i]
            merged += word2[i]
            i += 1
        while i<len(word2):
            merged += word2[i]
            i += 1

    else:
        i = 0
        while i<len(word1):
            merged += word1[i]
            merged += word2[i]
            i += 1

    print(merged)

mergeAlternately(word1, word2)