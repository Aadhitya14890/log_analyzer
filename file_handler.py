# file_handler.py

def read_log_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        print("Sorry! The log file was not found.")
        return None