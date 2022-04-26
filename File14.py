a = input()
for i in range(0 , len(a) + 1 , 2):
    print(f'Simvol code {a[i]} is {ord(a[i])}.\n', end='')
