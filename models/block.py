from util.math_helpers import is_prime
from util.math_helpers import odd_number
from util.math_helpers import even_number
from models.structure import Structure

class Block(Structure):

    def max_number(self):
        return max(self.__b_list)

    def min_number(self):
        return min(self.__b_list)

    def first_number(self):
        return self.__b_list[0]

    def last_number(self):
        return self.__b_list[-1]

    def prime_numbers(self):
        prime_numbers = list(filter(lambda i: is_prime(i), self.__b_list))
        return prime_numbers

    def even_numbers(self):
        even_numbers = list(filter(lambda i: even_number(i), self.__b_list))
        return even_numbers

    def odd_numbers(self):
        odd_numbers = list(filter(lambda i: odd_number(i), self.__b_list))
        return odd_numbers

    def number_of_even_numbers(self):
        return len(self.even_numbers())

    def number_of_odd_numbers(self):
        return len(self.odd_numbers())

    def number_of_prime_numbers(self):
        return len(self.prime_numbers())
    
    def get_resume(self):
        return [ self.max_number, self.min_number, self.first_number, self.last_number,
            self.number_of_prime_numbers, self.number_of_even_numbers, self.number_of_odd_numbers ]
        
    def get_b_list(self):
        return self.__b_list
    
    def get_a(self):
        return self.__a
        
    def set_b_list(self, b_list):
        self.__b_list = b_list
    
    def set_a(self, a):
        self.__a = a
        
    def __init__(self, *args):
        if len(args) > 0:
            self.__b_list = args[0]

    
    def __str__(self):
        return ('a: {}\n'
        'max_number: {}\n'
        'min_number: {}\n'
        'first_number: {}\n'
        'last_number: {}\n'
        'number_of_even_numbers: {}\n'
        'number_of_odd_numbers: {}\n'
        'number_of_prime_numbers: {}\n\n'
        '----------------------').format(
            self.__a, self.max_number(), self.min_number(),self.first_number(),self.last_number(),
            self.number_of_even_numbers(),
            self.number_of_odd_numbers(),self.number_of_prime_numbers())
    
    