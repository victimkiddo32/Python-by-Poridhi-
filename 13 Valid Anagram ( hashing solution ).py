def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    cnt_map_S = {}
    cnt_map_T = {}
    for i in range(len(s)):
        cnt_map_S[s[i]] = cnt_map_S.get(s[i], 0) + 1
        cnt_map_T[t[i]] = cnt_map_T.get(t[i], 0) + 1
    # Compare dictionaries after counting
    return cnt_map_S==cnt_map_T

s = input()
t = input()
print(valid_anagram(s, t))
