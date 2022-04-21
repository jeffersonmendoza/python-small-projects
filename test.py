
# Defining functions for drawing a character using * in the command line
# ---------- O character ---------- #
def o_character(size):
    last = size - 1 # last unit of column and width
    for row in range(size):
        for col in range(size):
            if ((row == 0 or row == last) and (col != 0 and col != last)):
                print('*', end='')
            elif (row != 0 and row != last) and (col == 0 or col == last):
                print('*', end='')
            else:
                print(end=' ')
        print()

# ---------- X character ---------- #
def x_character(size):
    i = 0
    j = size -1
    for row in range(size):
        for col in range(size):
            if (row == i) and (col == j):
                i = i + 1
                j = j - 1
                print('*',end='')
            elif (row == col):
                print('*',end='')
            else:
                print(end=' ')
        print()

# ---------- Y character ---------- #
def y_character(size):
    mid = (size / 2) - 0.5 # middle column
    i = mid # middle row
    j = 0 # row step
    k = size - 1 # column step going left
    for row in range(size):
        for col in range(size):
            if (col == mid) and (row == i):
                i = i + 1
                print('*',end='')
            elif (row == col) and (row < mid):
                print('*',end='')
            elif ((row == j) and (col == k)) and (row < mid):
                print('*',end='')
                j = j + 1
                k = k - 1
            else:
                print(end=' ')
        print()

# ---------- Z character ---------- #
def z_character(size):
    last = size - 1 # last unit of column and width
    i = 1 # row step
    j = last - 1 # column step going left
    for row in range(size):
        for col in range(size):
            if (row == 0) or (row == last):
                print('*', end='')
            elif (row == i) and (col == j):
                print('*', end='')
                i = i + 1
                j = j - 1 # column step going left
            else:
                print(end=' ')
        print()

def print_char(size):
    if char == 'O':
        o_character(size)
    elif char == 'X':
        x_character(size)
    elif char == 'Y':
        y_character(size)
    elif char == 'Z':
        z_character(size)

# ---------- Asking user input ---------- #

print('''

<=============================================>

Welcome to Character(Limited) Printing Program!

To Start:''')

char_list = ['O', 'X', 'Y', 'Z']

while True:
    char = input('''
Enter a character [O, X, Y, Z]:
(Press "Q" to quit)            ''').title() # multi-line for cosmetics only
    if (char == 'QUIT') or (char == 'Q'):
        print('\n>>>Program terminated.')
        break
    elif char in char_list:
        size = 0
        while True:
            size = input('''
Enter a non-negative odd integer not lower than 3:
(Press "Q" to quit)                               ''').title() # multi-line for cosmetics only
            if (size == 'QUIT') or (size == 'Q'):
                print('\n>>>Program terminated.')
                break
            try:
                size = int(size)
            except ValueError:
                print('\n>>>Enter a non-negative integer only!')
                pass
            else:
                if size < 3: # Unit size smaller makes character unrecognizable
                    print('\n>>>Integer must not be lower than 3!')
                    pass
                elif size % 2 == 0:
                    print('\n>>>Integer must not be even!')
                    pass
                elif size >= 3:
                    print('\n\nPrinting...')
                    print('Character:',char)
                    print('Unit Size:',size,'\n\n')
                    print_char(size)
                    print('\n\nThank you for using the program!')
                    break
        break


# o_character(size)
# x_character(size)
# y_character(size)
# z_character(size)
