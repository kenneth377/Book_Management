import uuid

class User:
    userlist =  []
    def __init__(self, name, age, password, email=None, telephone= None):
        self.usercart = []
        self.__password = password
        self.orderhistory= []
        self.id = str(uuid.uuid4())
        self.__name = name
        self.__age = age
        self.__email = email
        self.__tel = telephone
        User.userlist.append(self)




    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        self.__age = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,value):
        self.__email = value

    @property
    def tel(self):
        return self.__tel
        
    @tel.setter
    def tel(self,value):
        self.__tel = value



    @classmethod
    def register(cls,name,age, email=None, telephone=None):
        newuser = User(name,age, email, telephone)
        return newuser
    
    @classmethod
    def login(cls,email, password):
        for user in cls.userlist:
            if user.email == email:
                return user if password == user.password else "Incorrect Password"
            
            print(f"User {email} does not exist")
            return None
        
    