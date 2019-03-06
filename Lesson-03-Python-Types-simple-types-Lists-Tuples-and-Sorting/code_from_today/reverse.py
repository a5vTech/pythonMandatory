"""
# Reverse words
Have the function first_reverse(str) take the str parameter being 
passed and return the string in reversed order. 
For example: if the input string is "Hello World and Coders" 
then your program should return the string "sredoC dna dlroW olleH". 
"""

def first_reverse(str):  
    #temp = ''

    ## for i in range(len(str)):
       ## temp += str[i]

    # one liner



    return str[::-1]


# ===========================================================
# Leave this untouched
# ===========================================================
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f'{prefix} got: {got} expected: {expected}')


# Keep this main here - do not change anything
def main():

    print()
    print('First Reverse')
    test(first_reverse('coderbyte'), 'etybredoc')
    test(first_reverse('I Love Code'), 'edoC evoL I')
    test(first_reverse('Claus Bove'), 'evoB sualC')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()