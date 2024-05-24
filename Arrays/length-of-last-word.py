s = input("Enter a string: ")
def lengthOfLastWord(s: str) -> int:
    count=0
    i = len(s)-1
    while i >= 0 :
        if s[i] != " ":
            count += 1
        elif s[i] == " " and count>0 :
            break
        i -= 1

    return count

result = lengthOfLastWord(s)
print(result)