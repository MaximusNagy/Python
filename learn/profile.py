class Profile:
    def __init__(self, name, email, learn_language):
        self.name = name
        self.email = email
        self.learn_lang = learn_language

Name = input("Enter your name: ")
Email = input("Enter your email: ")
Learn_language = input("Enter your language: ")

customer = Profile(Name, Email, Learn_language)
print(customer.name)



