a = input()
res = ''
for i in range(0, len(a)):
    if i % 3 != 0:
        res = res + a[i]
print(res)


