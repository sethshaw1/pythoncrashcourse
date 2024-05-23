
class User:
    """Create an instance of a user"""
    
    def __init__(self, name, age, friends, location):
        """Initialise user attributes"""
        self.name = name 
        self.age = age 
        self.friends = friends 
        self.location = location
        self.login_attempts = 0
        
    def user_summary(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Number of friends: {self.friends}")
    
    def greet_user(self):
        print(f"Hi {self.name}!")
        
    def login(self):
        self.login_attempts += 1
        
    def reset_logins(self):
        self.login_attempts = 0
        
user_1 = User("Seth", "22", "836", "Bristol")

print("Starting program")

user_1 = User("Seth", "22", "836", "Bristol")
print("User created")

user_1.login()
print("First login")

user_1.login()
print("Second login")

print(user_1.login_attempts)


             