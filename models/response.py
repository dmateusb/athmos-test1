class Response():

    def __init__(self, *args):
        if len(args) > 0:
            
            self.__a = args[0]
            self.__b = args[1]

    def __call__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        return "[a: {}, b: {}]".format(self.__a, self.__b)

    def __str__(self):
        return "[a: {}, b: {}]".format(self.__a, self.__b)

    
    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

