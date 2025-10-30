import string

def word_counter():
    sentence=input("Please give a sentence: ")
    for i in string.punctuation:
        sentence = sentence.replace(i, "")
    print("Sentence: ", sentence)
    words= sentence.split(' ')
    a={}

    for i in words:
        if i in a:
            k= a[i]
            a[i]=k+1
        else:
            
            a[i]=1
    print(a)

print(word_counter())
