#Password Generator==
import random
import string


while True:
    def Password_Generator():
        Uppercase_Letters  = string.ascii_uppercase
        Lowercase_Letters  = string.ascii_lowercase
        digit_chars = string.digits
        symbol_chars = string.punctuation

        try:
            Length = int(input("How long do you want your password to be: "))
            if Length < 8:
                raise ValueError
            
        except ValueError:
            print("Password must be at least 8 characters!")
            return None

        try:
            Num_Upper = int(input("How many Uppercases do you want in your password: "))
            Num_Lower = int(input("Howw many Lowercases do you want in your password: "))
            Num_digits = int(input("How many digits do you want in your password: "))
            Num_Symbols = int((input("How many Symbols do you want in your password: ")))

        except ValueError:
            print("Please enter Valid  numbers.")
            return None

        
        
        total_chars  = Num_Upper + Num_Lower + Num_digits + Num_Symbols
        


        if total_chars != Length:
            print("The total number of characters does not match the password length.")
            return None
        

        if 0 in [Num_Upper, Num_Lower, Num_digits, Num_Symbols]:
            print("Your password is missing some Character types!")
            print("Note: your password must contain at least 8 characters")
            print("Your password must have at least 1 uppercase.")
            print("Your password must have at least 1 lowercase.")
            print("Your password must have at least 1 digits.")
            print("Your password must have at least 1 symbol.")
            return None
        

        password_chars = []

        password_chars += random.choices(Uppercase_Letters, k=Num_Upper)
        password_chars += random.choices(Lowercase_Letters, k=Num_Lower)
        password_chars += random.choices(digit_chars, k=Num_digits)
        password_chars += random.choices(symbol_chars, k=Num_Symbols)

        random.shuffle(password_chars)

        password = "".join(password_chars)
        return password




    password = Password_Generator()
    if password:
        print("\ngenerated password:", password)

    again = input("\nDo you want to generate another password? (yes/no): ").lower
    
    if again == "no":
        print("Goodbye!")
        break























    