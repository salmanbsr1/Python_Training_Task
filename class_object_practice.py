#Created by Salman Ansari

class Book:
    def __init__(self, title="Unknown", author="Unknown", pages="Unknown"):
        self.title = title
        self.author = author
        self.pages = pages
    def setbook(self):
        self.title= input('Enter book name: ')
        self.author = input('Enter author name: ')
        self.pages = input('Enter pages: ')
    def __len__(self):
        return self.pages
    def __del__(self):
        return 'Destructor called '+self.title+' deleted.'
        

b = Book()
print('Book author: ', b.author)
b.setbook()
print('Book author: ', b.author)
print('Book length is: ', b.__len__())
print(b.__del__())
print('Book author: ', b.author)