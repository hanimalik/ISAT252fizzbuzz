'''
An example of a Fizzbuzz program solution written using TDD
'''

def fizz(x):
    '''
    Returns 'fizz' if x is a multiple of 3, otherwise x
    '''
    return 'fizz' if x % 3 == 0 else x

def buzz(x):
    '''
    Returns 'buzz' if x is a multiple of 5, otherwise x
    '''
    return 'buzz' if x % 5 == 0 else x