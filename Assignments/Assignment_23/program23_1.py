#####################################################################################
#
#   Description : Instance Variables: 
#                  Name → Stores the name of the book
#                  Author → Stores the name of the author
#
#                 Class Variable:
#                   NoOfBooks → Keeps track of the total number of BookStore objects created
#                 
#                 Constructor (__init__):
#                   Accepts book name and author name as parameters
#                   Increments the class variable NoOfBooks by 1 every time a new object is created
#
#                 Instance Methods
#                    Displays the book details 
#                       <BookName> by <Author> no og books <NoOfBooks>
#
#                  Object Creation
#                     Create multiple objects of the BookStore class
#                     Call the Display() method for each object
#
#   Date :   26 / 01 /2026
#
#   Author : Rekha Shankarlal Kumawat
#  
#####################################################################################

class BookStore:

    NoOfBooks = 0

    def __init__(self, N ,A):
        self.Name = N
        self.Author = A
        BookStore.NoOfBooks = BookStore.NoOfBooks+1

    def Display(self):

        print(self.Name , "By" , self.Author , "No of Books" ,self.NoOfBooks)

def main():

    obj1 = BookStore("Linux System Programming" ,  "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming" , "Dennis ritchie")
    obj2.Display()

if __name__ == "__main__":

    main()

