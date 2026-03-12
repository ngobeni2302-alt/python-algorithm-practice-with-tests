def retry_password(password):
    while True:
        if input("Please Enter Password: ") == password:
            print("Login Successful")
            break
        else:
            print("Access Denied")

def guess_number(secret_number):
    while True:
        # secret_number = "7"
        if input("Please enter number:") == secret_number:
            print("Correct!")
            break
        else:
            print("Wrong guess")

def retry_code(code):
    while True:
        if input("Please enter code: ") == code:
            print("Door Unlocked")
            break
        else:
            print("Invalid Code")

def atm_attempt(pin):
    while True:
        if input("Please enter pin: ") == pin:
            print("Welcome!")
            break
        else:
            print("Wrong PIN")


def unlock_phone(pin):
    while True:
        if input("Please enter pin: ") == pin:
            print("Phone Unlocked")
            break
        else:
            print("Try Again")

