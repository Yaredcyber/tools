import pyzipper
import zipfile
import os
import platform

print(
    "\033[38;2;17;166;49m"
    '''
----------------------Welcome to zipper tool------------------
MMM"""AMV `7MMF'`7MM"""Mq.`7MM"""Mq.`7MM"""YMM  `7MM"""Mq.
M'   AMV    MM    MM   `MM. MM   `MM. MM    `7    MM   `MM.
'   AMV     MM    MM   ,M9  MM   ,M9  MM   d      MM   ,M9
   AMV      MM    MMmmdM9   MMmmdM9   MMmmMM      MMmmdM9
  AMV   ,   MM    MM        MM        MM   Y  ,   MM  YM.
 AMV   ,M   MM    MM        MM        MM     ,M   MM   `Mb.
AMVmmmmMM .JMML..JMML.    .JMML.    .JMMmmmmMMM .JMML. .JMM.

\n --------------------- Devloped by @yaredcyber -------------------
    '''
    "\033[0m"
)



def zip():
  print("Zipping file with out encryption may case data insecur ⚠⚠")
  folder_name = input('Enter name of folder (with out extension): \n')
  file_name = input('Enter name of your file name with extension(by separating whitespace): \n')
  if os.path.exists(folder_name+'.zip'):
    print("Folder already exists")
  else:
    with pyzipper.AESZipFile(folder_name+'.zip','w',compression=pyzipper.ZIP_DEFLATED) as zip:
      data = file_name.split()
      for file in data:
       zip.write(file,os.path.basename(file))
    print("Your data is seccsefully place on",folder_name+'.zip')




def zip_pass():
  print("ziping file with password")
  folder_name = input('Enter name of folder(without zip extension: \n')
  file_name = input('Enter name of your file file name with extension( by separating whitespace): \n')
  password = input('Enter your password: \n')
  if os.path.exists(folder_name+'.zip'):
    print("Folder already exists")
  else:
    with pyzipper.AESZipFile(folder_name+'.zip','w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES) as zip:
      zip.setpassword(password.encode('utf-8'))
      data = file_name.split()
      for file in data:
       zip.write(file,os.path.basename(file))
    print("Your ziped file is filed in ",folder_name+'.zip')

def zip_uncomp():
  print("Zipping file with out compression  \n")
  folder_name = input('Enter name of folder(with out extension): \n')
  file_name = input('Enter name of your file file: \n')
  if os.path.exists(folder_name+'.zip'):
    with pyzipper.AESZipFile(folder_name+'.zip','w') as zip:
     data = file_name.split()
    for file in data:
       zip.write(file,os.path.basename(file))
    print("Your data is ziped on ",folder_name+'.zip')

def unzip_pass():
    print("Unzipping file with password")
    folder_name = input('Enter the zipped folder name(without extenaion): \n')
    save = input('Enter the name of the directory to save unzipped data: \n')
    password = input('Enter your password: \n')

    if os.path.exists(save):
        print("Save folder already exists. Please choose a different name or delete the existing folder.")
    else:
        try:
            with pyzipper.AESZipFile(folder_name+'.zip', 'r', encryption=pyzipper.WZ_AES) as zip_file:
                zip_file.setpassword(password.encode('utf-8'))
                zip_file.extractall(save)
            print(f"Your data has been unzipped to {save}")
        except (RuntimeError, FileNotFoundError, pyzipper.zipfile.BadZipFile) as e:
            print(f"An error occurred: {e}. Please check your zip file and password.")




def unzip():
  print("Unziping file with out password")
  folder_name = input('Enter ziped folder name (without extension): \n')
  save = input('Enter name of your unziped data save: \n')
  if os.path.exists(save+'.zip'):
    print("Folder already exists")
  else:
    with pyzipper.AESZipFile(folder_name+'.zip','r') as zip:
      zip.extractall(save)
  print("Your unziped file saved on ",save)



def crack():
    print("Cracking password of zip file")
    zip_file = input("Enter ziped folder: \n")

    wordlist = input('Enter the name of your wordlist (without extension): \n')

    try:
        with open(wordlist + '.txt', 'r') as file:
            passwords = file.readlines()

        print("The zipped folder is being cracked...")

        for password in passwords:
            password = password.strip()
            try:
                with pyzipper.AESZipFile(zip_file+'.zip', 'r') as zip_ref:
                    zip_ref.pwd = password.encode()
                    zip_ref.extractall()
                    print(f"Password found: {password}")
                    return
            except (RuntimeError, pyzipper.zipfile.BadZipFile, pyzipper.zipfile.LargeZipFile):
                continue

        print("Password not found in the provided wordlist.")

    except FileNotFoundError:
        print("Wordlist file not found. Please check the file name and try again.")

def crack_zip():
   print("Cracking password of zip file , This not support for pyzipper ")
   zip_file = input("Enter ziped folder(without extension): \n")
   wordlist = input('Enter the name of your wordlist (without extension): \n')
   try:
      with open(wordlist+'.txt','r') as file:
         passwords = file.readlines()
         print("The zipped folder is being cracked...")
         for password in passwords:
            password=password.strip()
            try:
               with zipfile.ZipFile(zip_file+'.zip','r') as zip_ref:
                  zip_ref.extractall(pwd=password.encode())
                  print(f"Password found: {password}")
                  return
            except(RuntimeError):
               continue
   except FileNotFoundError:
      print("Wordlist file not found. Please check the file name and try again.")

def clear_screen():

    current_os = platform.system()


    if current_os == "Windows":
        os.system('cls')

    else:
        os.system('clear')


while True:
  try:

    choice = input("zipper/>")
    if choice == 'zip':
      zip()
    elif choice == 'zip_pass':
      zip_pass()
    elif choice == 'zip_uncomp':
      zip_uncomp()
    elif choice == 'unzip_pass':
      unzip_pass()
    elif choice == 'unzip':
      unzip()
    elif choice == 'crack':
      crack()
    elif choice == 'crack_zip':
       crack_zip()
    elif choice == 'clear':
       clear_screen()
    elif choice == '--help':
      print('zip = Zip file \n ')
      print('zip_pass = Zipping file with password AES \n')
      print('zip_nopass = Zipping \n')
      print('zip_uncomp = Zipping file with out password and compression \n')
      print('unzip_pass = Unzipping file it has password \n ')
      print('unzip = Unzip Ziped file with no password \n ' )
      print('crack = Brute forcing password for python zipped files  \n ')
      print('crack_zip = Brute forcing password for normal ziped file \n ')
      print('--help = To show commands and their uses \n')
      print('clear = To clear the screen \n')
    elif choice == 'exit':
      print("Thnakyou for your choice  please follow  in X  and github  account ")
      break
    else:
      print("Please Enter  --help  to see more option ")
  except:
    print("Please Enter valid option")
