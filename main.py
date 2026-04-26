from cryptography import fernet
from crypto import encrypt_file, decrypt_file
from get_all_files import file_paths, get_all_files_fnc
from starting import folder_or_file, encrypting_or_decrypting, check_key

key = None  # Initialize key globally
folder_name = None
file_name = None
decrypting = False
encrypting = False
input_choice = "None"
int_choice = None
key = None

def main():
    global key
    folder, file = folder_or_file(folder_name, file_name)
    encrypting, decrypting, key = encrypting_or_decrypting(encrypting, decrypting, key)
    check_key(key)
    if encrypting:
        print("You chose to encrypt the files.")
        print("Schlüssel: ", key.decode())
        with open("key_file.txt", "w") as key_file:
            key_file.write(key.decode())
        print("Please keep the key safe, otherwise this can never be decrypted again.")
    elif decrypting:
        print("You chose to decrypt the files.")
        key_file = open("key_file.txt", "r")
        key_input = key_file.read()
        key = key_input.encode()
    if folder:
        if not folder_name:  # Ensure folder_name is not None
            print("Error: Folder name is not set. Exiting.")
            exit()
        get_all_files_fnc(folder_name)
        for file in file_paths:
            if encrypting:
                encrypt_file(file, key)
            elif decrypting:
                decrypt_file(file, key)
    elif file:
        if encrypting:
            encrypt_file(file_name, key)
        elif decrypting:
            decrypt_file(file_name, key)
    print("Process completed.")


if __name__ == "__main__":
    while True:
        main()
        do_exit = input("Do you want to exit? (y/n): ")
        if do_exit.lower() == "y":
            break
    input("Press Enter to exit...")
