
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title '{self.title}' Author = {self.author}"

    def __len__(self):
        return len(self.pages)

    def __del__(self):
        print("Book object deleted")
if __name__ == '__main__':
    b = Book("Python Programming made easy","Naveen","100")
    print(b)
    print(len(b))
    del(b)
