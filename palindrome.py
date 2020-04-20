# palindrome
def palindrome(word):
    len(word)
    new_word=''
    a=[]
    for i in range(len(word)):
        if word[i]==word[-i-1]:
            new_word+=word[i]
    print('new_word',new_word)
    if word==new_word:
        print('yes it is a palindrome')
    else:
        print('Not a palindrome')


#palindrome('nitin')


def ispalindrome(string,low,high):
    while low < high:
        if string[low]!=string[high]:
            return False
        low += 1
        high -= 1
    return True

print(ispalindrome('nitin',0,4))
