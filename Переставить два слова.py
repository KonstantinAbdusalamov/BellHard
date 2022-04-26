s = input()
space = s.find(' ') 
s1 = s[:space]
s2 = s[space:]
print(s2 + ' ' + s1)