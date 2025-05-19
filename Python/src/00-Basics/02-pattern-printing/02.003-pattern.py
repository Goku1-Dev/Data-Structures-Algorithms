def pattern_3():
    row = 5

    for y in range(1, row + 1):
        for x in range(1, y + 1):
            print(x, end='')
        print()

pattern_3()
