class Variable:
    number=10

    def __init__(self):
        self.number=1
        Variable.number+=1

    @staticmethod
    def getStaticNumber():
        return Variable.number

    def getNumber(self):
        return self.number

if __name__ == '__main__':
    obj1 = Variable()
    obj2 = Variable()

    print(obj1.getNumber())
    print(obj1.getStaticNumber())

