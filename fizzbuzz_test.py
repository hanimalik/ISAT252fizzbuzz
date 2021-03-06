'''
Unit tests for the TDD Fizzbuzz program solution.
'''

#Import code to be tested
from fizzbuzz import fizz, buzz

def describe_a_fizzbuzz_program_that():

    def has_a_smoke_test():
        '''
    The purpose of a smoke test is to give us 
    confidence that our testing infastructure
    is set up correctly. We do that by creating
     a test that should ALWAYS pass.
        '''
    assert True 

    def takes_a_numeric_input_and_returns_fizz_if_it_is_a_multiple_of_3():
        '''
        We need a function that can take a single input and that
        returns a value which could either be "fizz" or whatever
         the input was to begin with.
        '''
        assert fizz(3) == 'fizz'
        assert fizz(4) == 4
        assert fizz(9) == 'fizz'
        assert fizz(17) == 17
        assert fizz(15) == 'fizz'
        assert fizz(5) == 5


    def takes_a_numeric_input_and_returns_buzz_if_it_is_a_multiple_of_5():
        '''
        We need a function that can take a single input and that
        returns a value which could either be "buzz" or whatever
        the input was to begin with.
        '''
        assert buzz(5) == 'buzz'
        assert buzz(4) == 4
        assert buzz(17) == 17
        assert buzz(15) == 'buzz'
        assert buzz(3) == 3