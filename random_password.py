##Password brute forcer
##Requirements:
##Length more than 8 characters less than 16
##At least one upper case letter 
##At least one lower case letter
##At least one special password
import random 

class Bruteforcer:
    def __init__(self, length=8, upper=1, lower=6, special=1, combinations=10, threads=1, digit=2):
        self.length = length
        self.upper = upper
        self.lower = lower
        self.special = special
        self.combinations = combinations 
        self.digit = digit 

    def generate_password(self):
        password = ""
        operations = [self.get_digits(), self.get_special_chars(), self.get_lower_chars(), self.get_upper_chars()]
        random.shuffle(operations)

        for index in range(len(operations)):
            password += operations[index]
        
        return password
        
    def get_digits(self):
        digits = ""
        for _ in range(self.digit):
            digit = random.randint(48, 57)
            digits += chr(digit)
        return digits 

    def get_special_chars(self):
        special_chars = ""
        for _ in range(self.special):
            special = random.randint(0, 9)  
            special_mapping = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
            special_chars += special_mapping[special]
        return special_chars  
        
    def get_lower_chars(self):
        lower_chars = ""
        for _ in range(self.lower): 
            lower = random.randint(97, 122)
            lower_chars += chr(lower)
        return lower_chars

    def get_upper_chars(self):
        upper_chars = ""
        for _ in range(self.upper): 
            upper = random.randint(65, 90)
            upper_chars += chr(upper)
        return upper_chars
    
    def __str__(self):
        attributes = ""
        for key, val in self.__dict__.items():
            attributes += f"Attribute:{key} Value: {val}"
        return attributes



password = Bruteforcer()
print(password)
print(password.generate_password())