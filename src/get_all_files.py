from sys import exit
import os

file_paths = []


def get_all_files_fnc(directory):
    file_paths.clear()
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if (
                    file == "key_file.txt"
                    or file == "main.exe"
                    or file == "main"
                ):
                    continue
                file_paths.append(os.path.join(root, file))
        return file_paths
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
    except Exception as e:
        print(f"An error occurred while accessing the directory: {e}")
        exit(1)
