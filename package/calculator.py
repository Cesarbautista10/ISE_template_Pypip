class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum(self):
        return sum(self.numbers)

    def subtract(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        return result

    def multiply(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result *= num
        return result

    def divide(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result /= num
        return result