input_str = '010001'
wc = [int(i) for i in input_str]

def main():
    print(wc)
    long = len(wc)
    step = long - 1
    plus = 0
    while step > 0:
        for i in range(1, step, 2):
            peace = [wc[i - 1], wc[i], wc[i + 1]]
            if peace == [0,0,0]:
                print(f'Позиция -> {i}')
                wc[i] = 1
                plus += 1
        step -= 1
    if plus == 0:
        print('Нет места')
    print(wc)


main()
