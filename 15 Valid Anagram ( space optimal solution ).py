def valid_anagram(s, t):
    arr=[0]*26
    #space complexity O(1) as the size of the arr is fixed 26
    for i in range(len(s)):
        arr[ord(s[i])-97]+=1
        arr[ord(t[i])-97]-=1
    
    for i in range(26):
        if arr[i]!=0:
            return False
    return True
    

s = input()
t = input()
print(valid_anagram(s, t))
