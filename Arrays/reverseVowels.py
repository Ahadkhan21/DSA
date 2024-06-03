s = "hello"

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    vowels = []
    string = []
    r=''
    for i in s:
        string.append(i)
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
            vowels.append(i)

    j = len(vowels)-1
    i = 0
    while i < len(string):
        if string[i] == 'a' or string[i] == 'A' or string[i] == 'e' or string[i] == 'E' or string[i] == 'i' or string[i] == 'I' or string[i] == 'o' or string[i] == 'O' or string[i] == 'u' or string[i] == 'U':
            string[i] = vowels[j]
            j -= 1
        i += 1

    for i in string:
        r += i


    return r

result = reverseVowels(s)
print(result)