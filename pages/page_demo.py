class SomeClassToTest(object):

    def __init__(self, value):
        self.value = value

    def sum_numbers(self, a, b):
        return a + b + self.value
