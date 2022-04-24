from abc import abstractmethod, ABC

class Structure(ABC):

    @abstractmethod
    def max_number():
        pass

    @abstractmethod
    def min_number():
        pass

    @abstractmethod
    def first_number():
        pass

    @abstractmethod
    def last_number():
        pass

    @abstractmethod
    def number_of_prime_numbers():
        pass

    @abstractmethod
    def number_of_even_numbers():
        pass

    @abstractmethod
    def number_of_odd_numbers():
        pass