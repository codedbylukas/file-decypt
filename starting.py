from cryptography import fernet


def folder_or_file(folder_name, file_name):
    print("""Do you want to 
    1. work with a folder 
    2. work with a single file?""")
    input_choice = input("Enter 1 or 2: ")
    int_choice = int(input_choice)
    if int_choice == 1:
        folder = True
        file = False
        folder_name = input("Enter the folder path: ")
    elif int_choice == 2:
        folder = False
        file = True
        file_name = input("Enter the file path: ")
    else:
        print("Invalid choice. Exiting.")
        exit()
    return folder, file


def encrypting_or_decrypting(encrypting, decrypting, key):
    print("""Do you want to 
    1.encrypt 
    2.decrypt 
    the files'?""")
    input_choice = input("Enter 1 or 2: ")
    int_choice = int(input_choice)
    if int_choice == 1:
        encrypting = True
        decrypting = False
        key = fernet.Fernet.generate_key()  # Generate key for encryption
    elif int_choice == 2:
        encrypting = False
        decrypting = True
        try:
            with open("key_file.txt", "r") as key_file:
                key = key_file.read().encode()  # Read key for decryption
        except FileNotFoundError:
            print("Key file not found. Cannot decrypt.")
            exit()
    else:
        print("Invalid choice. Exiting.")
        exit()


def check_key(key: str):
    if key is None:  # Check if key is properly initialized
        print("Error: Key is not initialized. Exiting.")
        exit()

