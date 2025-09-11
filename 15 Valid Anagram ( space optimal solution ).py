def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    freq=[0]*26
    #space complexity O(1) as the size of the freq is fixed 26
    for i in range(len(s)):
        freq[ord(s[i])-97]+=1
        freq[ord(t[i])-97]-=1
    
    for i in range(26):
        if freq[i]!=0:
            return False
    return True
    

s = input()
t = input()
print(valid_anagram(s, t))
