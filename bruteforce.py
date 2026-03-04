import sys

sys.stdout.reconfigure(line_buffering=True)

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-.:,;_#'+*~<>|!§$%&/()=?´`@€{[]}\\"
password_length = 3

def generate_passwords(current_password, length):
    if length == password_length:
        print(current_password)
        return

    for char in alphabet:
        generate_passwords(current_password + char, length + 1)

def generate_all_passwords():
    for i in range(password_length + 1):
        generate_passwords("", i)

generate_all_passwords()
