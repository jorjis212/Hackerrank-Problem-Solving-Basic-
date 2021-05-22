
# =========================String Anagram================================

def stringAnagram(List, query):
    dict = {}
    for st in List:
        L = str(sorted(st))
        if L in dict:
            dict[L] += 1
        else:
            dict[L] = 1
    ans = []
    for sl in query:
        L = str(sorted(sl))
        if L in dict:
            ans.append(dict[L])
        else:
            ans.append(0)
    return ans
