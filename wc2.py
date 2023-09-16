wc = list('00010')
long = len(wc)

print(wc)

if '1' in wc:
	if not long%2:
		if wc[0] == '1':
			print(f'Кол-во четное, 1')
		elif wc[0] == '0':
			print(f'Кол-во четное, 0')
	else:
		if wc[0] == '1':
			print(f'Кол-во не четное, 1')
		elif wc[0] == '0':
			print(f'Кол-во не четное, 0')
else:
	for i in range(long):
		if not i%2:
			wc[i] = '1'

print(wc)
