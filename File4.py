s = input()
position = 0
for i in range(len(s)):
	if s[i] == 'f':
		position = position + 1
		if position == 2:
			break
if position == 0:
	print('-2')
elif position == 1:
	print('-1')
else:
	print(i)
