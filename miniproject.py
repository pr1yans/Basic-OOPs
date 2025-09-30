class Chatbook:
    __user_id=0
    def __init__(self):
        self.userid = Chatbook.__user_id
        Chatbook.__user_id += 1
        self.username = ""
        self.password = ""
        self.login = False
        #self.menu()
    @staticmethod   
    def get_id():
        return Chatbook.__user_id
    @staticmethod
    def set_id(value):
        Chatbook.__user_id = value
        
    def menu(self):
        user_input = input(""""Welcome,
                            1. press 1 to signup
                            2. press 2 to login
                            3. press 3 to write a post
                            4. press 4 to text message
                            5. press anything to exit""")
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.snd_msg()
        else:
            exit()
    
    def signup(self):
        email = input("enter your email, ")
        password = input("enter your password, ")
        self.username = email
        self.password = password
        print("tou have signed up")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == "" and self.password == "":
            print("please first signup")
            self.menu()
        else:
            uname = input("enter your email, ")
            pd = input("enter your password, ")
            if self.username==uname and self.password==pd:
                print("signin successfull")
                self.login =True
            else:
                print("write correct credentials")
        print("\n")
        self.menu()    
    
    def my_post(self):
        if self.login == True:
            x = input("ENTER YOUR POST")
            print(f"your post has been scheduled {x}") 
        else:
            print("log in first if don't have an account then sign in first")   
        print('\n')
        self.menu()
    
    def snd_msg(self):
        if self.login ==True:
            a = input("enter your msg -> ")
            b = input('enter friend name ->')
            print(f"your msg has been sent to {b}")
        else:
            print("log in first if don't have an account then sign in first")   
        print('\n')
        self.menu()
            

