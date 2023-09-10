input_str = '010001'
wc = list(input_str)


for i in range(1, len(wc)):
    if wc[0] == '1':
        if wc[i - 1] == '0' and wc[i] == '0':
            wc[i] = '1'
            print(f' Позиция: {i}')
    elif wc[0] == '0':
        if wc[i - 1] == '0' and wc[i] == '0' and wc[i + 1] == '0':
            wc[i] = '1'
            print(f' Позиция: {i}')

# Для наглядности
one = ''.join(wc)
print(f'Входные данные:   {input_str}')
print(f'Выходные данные:  {one}')
