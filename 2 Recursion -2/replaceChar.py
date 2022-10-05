def replaceChar(s,a,b):
    if len(s)==0:return s
    outp = replaceChar(s[1:],a,b)
    if s[0] == a:
        return b + outp

    else:
        return s[0] + outp

print(replaceChar('abacda','a','b'))