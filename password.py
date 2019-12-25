text = """
-----------------------------------------------------
Create Password
Your password must be at least 8 characters long.
Your password must contain uppercase letters, lowercase letters and numerical values.
-----------------------------------------------------
"""
print(text)

def num_control(password):
    for i in password:
        if i.isnumeric():
            return True
    return False  

def lowercase_control(password):
    for i in password:
        if i.islower():
            return True
    return False  

def uppercase_control(password):
    for i in password:
        if i.isupper():
            return True
    return False  

def leter_control(password):
    result = uppercase_control(password) and lowercase_control(password)
    return result

def len_control(password):
    if len(password) >= 8:
        return True
    return False  

num_trial = 3

while num_trial > 0:
    try:
        password = input("Enter your password: ")

        step = "D1"
        if not num_control(password):
            print("There is no numerical value in the password you entered.")
        step = "D2"
        if not leter_control(password):
            print("There is no upper and lower case character in the password you entered.")
        step = "D3"
        if not len_control(password):
            print("The password you enter must be at least 8 characters long.")

        if len_control(password) and leter_control(password) and num_control(password) is True:
            print("Your password was successfully created.")
            break

        if num_control(password) or leter_control(password) or num_control(password) is False:
            num_trial = num_trial - 1
            if num_trial > 0:
                print("You have %s attempt(s) left!" % num_trial)
            else:
                print("No trials left!")

    
    except Exception as error:
        print("Error! Step:'%s', Error Message: '%s'" % (step, error))
        num_trial = num_trial - 1

        
    password_successful = True 


