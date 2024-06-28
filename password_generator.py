import os

print("[+] Welcome to Numerical password Generator tools [+]")
print("[+] This tool is made by @yaredcyber [+]")
try:
    file_name = input("Enter your password filename: ")
    digit = int(input("Please enter how many digits the password should have: "))
except ValueError:
    print("Please enter a valid integer for the number of digits.")

def generate_passwords(length):
    with open(file_name, 'w') as file:
        if length == 4:
            for i in range(10000):
                password = f"{i:04}"
                file.write(password + '\n')
        elif length == 5:
            for i in range(100000):
                password = f"{i:05}"
                file.write(password + '\n')
        elif length == 6:
            for i in range(1000000):
                password = f"{i:06}"
                file.write(password + '\n')
        elif length == 7:
            for i in range(10000000):
                password = f"{i:07}"
                file.write(password + '\n')
        elif length == 8:
            confirm = input("Generating 8-digit passwords may take a long time and use CPU resources. Continue? (Y/N): ")
            if confirm.upper() == 'Y':
                for i in range(100):
                    password = f"{i:02}"
                    file.write(password + '\n')
            else:
                print("Operation aborted. Thank you for using this tool.")

if os.path.exists(file_name):
    print("File already exists.")
else:
    generate_passwords(digit)
    print(f"Passwords generated and saved to {file_name}. Thank you.")
