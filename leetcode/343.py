def reverseString(s):
    for i in range((len(s)+1)//2):
        s[i], s[len(s)-1-i]=s[len(s)-1-i], s[i]
    return s

print(reverseString(["i", "z", "w"]))


        