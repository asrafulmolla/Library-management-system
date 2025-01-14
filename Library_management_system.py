class Library:
    _book_list=[]
    
    @classmethod
    def entry_book(self, book):
        self._book_list.append(book)
    @classmethod
    def find_book(self, id):
        for book in self._book_list:
            if book.get_id()==id:
                return book
        return False 
class Book(Library):
    
    def __init__(self, book_id, title, author, availability = True):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=availability
        self.entry_book(self)
        
    def get_id(self):
        return self.__book_id
    
    def get_availability(self):
        return self.__availability
        
    def set_availability(self, current):
        self.__availability = current
    
    def borrow_book(self, id):
        book = self.find_book(id)
        if book==True: 
            print(f'Book ID: {id} Not Exist in Library')
        elif book.get_availability()==True:
            book.set_availability(False)
            print(f'Book ID: {id} borrow successfully.')
        else:
            print(f'Book ID: {id} is not available for borrow.')
        
    def return_book(self,id):
        book = self.find_book(id)
        if book.get_availability() == False:
            book.set_availability(True)
            
    def view_book_info(self):
        if self.get_availability() == True:
            now='Availabe'
        else:
            now='Not Available'
        
        print(f'ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {now}')
    @classmethod
    def view_all_book(self):
        if len(self._book_list)==0:
            print (f'No book Available.')
        else:
            for all_book in self._book_list:
                all_book.view_book_info()

Book(book_id=101, title='Python Programming', author='John Doe')
Book(book_id=102, title='Data Science', author='Jane Smith')
Book(book_id=103, title='OOP', author='Asraful')
Book(book_id=104, title='DS', author='Molla')
Book(book_id=105, title='Machine learning' , author='Rafiq')
Book(book_id=106, title='Data Analysis' , author='Kuddus')

while 1:
    print ('\n------ Wellcome to the Library ------')
    print ('1. View All Books')
    print ('2. Borrow Book')
    print ('3. Return Book')
    print ('4. Exit.\n')
    choice= input('Enter Your Choice: ')
    choice=int(choice)
    print ('\n')
    if choice==1:
        print ('Library Books: ')
        Book.view_all_book()
    elif choice ==2:
        id = int(input('Enter Book ID: '))
        book = Library.find_book(id)
        if book==False:
            print (f'Book ID: {id} Not Exist in Library')
        else:
            book.borrow_book(id)
            
    elif choice ==3:
        id = int(input('Enter Book ID: '))
        book = Library.find_book(id)
        if book==False:
            print (f'Book ID: {id} Not Exist in Library')
        else:
            if book.get_availability() == False:
                book.return_book(id)
                print ('Your Book Return Successfully')
            else:
                print (f'Book ID: {id}, Book not Borrow')
    elif choice ==4:
        break
    else :
        print ('Invalid Choice. Try Again')
        