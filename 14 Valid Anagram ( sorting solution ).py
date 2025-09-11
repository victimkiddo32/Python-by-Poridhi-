def valid_anagram(s, t):
    #anagram->aaagnmr
    #nagaram->aaagnmr
    return sorted(s)==sorted(t) 

s = input()
t = input()
print(valid_anagram(s, t))
