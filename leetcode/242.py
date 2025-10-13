def isAnagram(s,t):
        if len(s)!=len(t):
            return False
        else:
            s_= s
            t_= t
            for i in (s):
                if i in t:
                    t=t.replace(i, "", 1)
            if len(t)==0:
                return True
        return False

print(isAnagram("aaa", "aaa"))
isAnagram("djkwjdn", "ekrer")