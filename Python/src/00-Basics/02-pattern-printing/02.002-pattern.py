def pattern_2():
    row = 7

    for y in range(1, row + 1):
        for x in range(y):
            print('*', end='')

        print('')

pattern_2();