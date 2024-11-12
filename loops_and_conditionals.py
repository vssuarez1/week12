

import re
password=input("Create password: ")
if len(password) >= 8 and re.search("[0-9]",password) and re.search("[@$]",password):
    print("Password is valid.")
else:
    print("Create a stronger password.")

   


    
# Correct answer

import re

while True:
    password = input("Create a password: ")
   
    if len(password) >= 8:
        if re.search("[0-9]", password):
            if re.search("[@$]", password):  # Adjust special character range as needed
                print("Password is valid.")
                break  # Exit the loop if the password is valid
            else:
                print("Password must contain at least one special character (@, $).")
        else:
            print("Password must contain at least one number.")
    else:
        print("Password must be at least 8 characters long.")
   
    print("Please create a stronger password.")

   
    

    

    

    






















