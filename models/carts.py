from books import Book
from user import User

class Cart:
    cart = []


    @classmethod
    def add(cls,user,book):
        if not user in cls.cart:
            cls.cart.append(user)
        
        user.usercart.append(book)
        book.quantity = book.quantity - 1
    
    @classmethod
    def viewcart(cls,user):
        viewcartl =[]
        for book in user.usercart:
            bookdict = {"Title":f"{book.title}", "Author":f"{book.author}", "Genre":f"{book.genre}", "Price":f"{book.price}"}
            viewcartl.append(bookdict)
        
        return viewcartl
    

    @classmethod
    def checkout(cls,user):
        order = Cart.viewcart(user)
        user.orderhistory.append(order)

        user.usercart =[]


    @classmethod
    def viewhistory(cls,user):
        print(user.orderhistory)
