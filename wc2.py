input_str = '010001'
wc = list(input_str)

print(wc)

if '1' in wc:
	for i in range(1, len(wc) - 1):
		if wc[0] == '1':
			if wc[i - 1] == '0' and wc[i] == '0':
				wc[i] = '1'
				print(f' Позиция: {i}')
		elif wc[0] == '0':
			if wc[i - 1] == '0' and wc[i] == '0' and wc[i + 1] == '0':
				wc[i] = '1'
				print(f' Позиция: {i}')
else:
	for i in range(long):
		if not i%2:
			wc[i] = '1'

print(wc)

