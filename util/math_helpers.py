def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def even_number(num):
    return True if num % 2 == 0 else False

def odd_number(num):
    return True if num % 2 != 0 else False
