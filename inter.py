def longestsubstring(s):
    l = [-1] #
    r = 0 
    c = 0
    for i in range(len(s)):
        if s[i]  == '(':
            l.append(i)
        else:
            if l[-1] == -1:
                l.append(i)
            else:
                l.pop()
                c = i - l[-1]
                r = max(r,c)
    return r