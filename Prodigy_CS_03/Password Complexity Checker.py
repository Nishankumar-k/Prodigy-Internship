def check_password_strength(password):
        # Initialize counters for character types
        upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
        length = len(password)
    
        # Check minimum length
        if (length < 8):
            return "Password must be at least 8 characters long!"
    
        # Iterate through password characters
        else:
            for i in range(0, length):
                if (password[i].isupper()):
                    upperChars += 1
                elif (password[i].islower()):
                    lowerChars += 1
                elif (password[i].isdigit()):
                    digits += 1
                else:
                    specialChars += 1
    
        # Evaluate password strength
        if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
            if (length >= 12):
                return "Strong"
            else:
                return "The strength of password is Medium."
        else:
            if (upperChars == 0):
                return "Password must contain at least one uppercase character!"
            elif (lowerChars == 0):
                return "Password must contain at least one lowercase character!"
            elif (specialChars == 0):
                return "Password must contain at least one special character!"
            elif (digits == 0):
                return "Password must contain at least one digit!"

# Test the function
while True:
    password = input("Please enter a password: ")
    strength = check_password_strength(password)

    if strength == "Strong":
        print("The strength of password is strong.\n")
        break
    else:
        print(strength)
        print("Please enter a stronger password.\n")