#simple GUI  file locker/encrypter  
#This tool  can encrypt data using  RSA and it requare  password  
#The encrypted file also can be encrypted twice  usng the  passwrod  
# And it also use advance  Encryption system 



from cryptography.fernet import Fernet
import tkinter
from tkinter import filedialog
from functools import partial
from customtkinter import *
import base64
import hashlib 

fileName = None

def browseFile():
    global fileName
    file = filedialog.askopenfile(initialdir="/", title="Select File")
    if file:
        fileName = file.name
        label_file_explorer.configure(text="File Opened: " + fileName)

def derive_key(password):
    # Create a consistent key from the password
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(p_word):
    if not fileName:
        status_label.configure(text="No file selected")
        return
    
    temp_key = p_word.get()
    key = derive_key(temp_key)
    fernet = Fernet(key)

    with open(fileName, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)

    with open(fileName, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    status_label.configure(text="Encrypted")
    status_label.pack()

def decrypt_file(p_word):
    if not fileName:
        status_label.configure(text="No file selected")
        return
    
    temp_key = p_word.get()
    key = derive_key(temp_key)
    fernet = Fernet(key)

    with open(fileName, 'rb') as enc_file:
        encrypted = enc_file.read()
    
    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception as e:
        status_label.configure(text="Decryption failed: " + str(e))
        return

    with open(fileName, 'wb') as dec_file:
        dec_file.write(decrypted)

    status_label.configure(text="Decrypted")
    status_label.pack()

root = CTk() #creating window  
root.title("Locker")
root.geometry("500x310")

def mode():
    root._set_appearance_mode("light")

main_title = CTkLabel(root, text="File locker", width=100, height=2, font=("Arial", 30))
main_title.pack()

passwd = StringVar()

submit_para_en = partial(encrypt_file, passwd)
submit_para_de = partial(decrypt_file, passwd)

label_file_explorer = CTkLabel(root, text="File name: ", width=100, text_color="green", font=("JetBrains Mono", 28))
label_file_explorer.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

button_mode = CTkButton(root, text="Mode", command=mode)
# button_mode.pack()

button_explorer = CTkButton(root, text="Browse File", command=browseFile, width=600, height=40)
button_explorer.place(rely=0.4, relx=0.5, anchor=tkinter.CENTER)

password = CTkEntry(root, show='', textvariable=passwd, width=600, height=40, font=('', 24))
password.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)

button_encrypt = CTkButton(root, text="Encrypt", command=submit_para_en, width=300, height=40, fg_color="red", hover_color="red")
button_encrypt.place(rely=0.5, relx=0.7, anchor=tkinter.CENTER)

button_decrypt = CTkButton(root, text="Decrypt", command=submit_para_de, width=300, height=40, fg_color="green", hover_color="green")
button_decrypt.place(rely=0.5, relx=0.3, anchor=tkinter.CENTER)

status_label = CTkLabel(root, text="", text_color="green")

root.mainloop()
