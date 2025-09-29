class Chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.login = False
        self.menu()
        
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
            pass
        elif user_input == "4":
            pass
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
        
CB = Chatbook()


