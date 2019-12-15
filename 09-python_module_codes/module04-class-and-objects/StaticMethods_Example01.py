class Calculator:

    def fn(self,param1):
        print(param1)


    def add(numer_one,number_two):
        return numer_one+number_two

    @staticmethod
    def multiply(number_one,number_two):
        return number_one* number_two

if __name__ == '__main__':
    obj = Calculator()
    obj.fn("df")
    print(Calculator.add(12,13))
    print(Calculator.multiply(12, 13))