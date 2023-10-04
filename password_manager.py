import string
TOTAL_ALPHABET = len(string.ascii_lowercase)

SHIFT = 5


def encrypt(password, SHIFT):
#to encrypt using ceaser cipher method
     return ''.join(chr((ord(char) - ord("A") + SHIFT) % TOTAL_ALPHABET + ord("A")) if char.isupper() else 
                   chr((ord(char) - ord("a") + SHIFT) % TOTAL_ALPHABET + ord("a")) if char.islower() else 
                   str(int(char) + SHIFT) if char.isdigit else char for char in password)


def decrypt(password, SHIFT):   
    #to decrypt 
    return ''.join(chr((ord(char) - ord("A") - SHIFT) % TOTAL_ALPHABET + ord("A")) if char.isupper() else 
                   chr((ord(char) - ord("a") - SHIFT) % TOTAL_ALPHABET + ord("a")) if char.islower() else 
                   str(int(char) - SHIFT) if char.isdigit else char for char in password)


def view():
    
    #to view the content of the file in decipher
    while True:
        main_password = input(
            "Enter main password to view your password manager(press q to go back to main menu):")
        if main_password == "q" or main_password == "Q":
            break
        if main_password == "mainpassword":
            with open('passwords.txt', 'r') as f:
                for line in f.readlines():
                    data = line.rstrip()
                    user, password = data.split("|")

                    decrypted_password = decrypt(password, SHIFT)

                    print("Name:", user, "|" "Password:", decrypted_password)
            break
        else:
            print("password incorrect please re-enter")


def add():
    #to add new username and password on the file
    name = input('Your Name: ')
    password = input('Your Password: ')
    while True:
        if (SHIFT <= 26):
            ciphered_password = encrypt(password, SHIFT)
            with open('passwords.txt', 'a') as f:
                f.write(name + "|" + ciphered_password + "\n")
            print(  
                "Succesfully saved!- name: {0} and password:{1}".format(name, ciphered_password))
            break
        else:
            print("Enter valid value for SHIFT(1-26)")
            continue


while True:
    #for the prompt
    choice = input(
        "Press (A) for adding new password and (V) for viewing (q) for quiting: ")
    if choice == "q" or choice == "Q":
        break
    if choice == "a" or choice == "A":
        add()
    elif choice == "v" or choice == "V":
        view()
    else:
        print("invalid choice please re-select")
        continue
