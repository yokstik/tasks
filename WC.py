input_str = '0100010100001'
print(input_str)
wc = list(input_str)

for i in range(len(wc)):
    if wc[i-1] == '0' and wc[i] == '0' and wc[i+1] == '0':
        wc[i] = '1'
one = ''.join(wc)
print(one)
