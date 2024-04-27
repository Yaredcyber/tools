def man():
    print("###################Yared cryptography ################ \n"
          "****************** Information****************\n"
          "- This tool developed for simple cryptography \n"
          "- This tool not use any thier own algorith \n"
          "- It work just translating english alphabates  like a into e\n"
          "- It not have any key  i trying to develop it  \n"
          "##################### Thank You ###################")
def help():
    print("############### core command ########### \n "
          "- deco : used to decrypt texts \n "
          "- enco : used to encrpt your texts")
print("Welcome to simple yared cryptograhing tool \n ")
choice = input("crypto-> ")

def encryption():
    print("This is used to encrypt data / textx \n")
    def yared_encrypt(text):
        translation = ""
        for char in text:
            if char.lower() == "a":
                translation += "u"
            elif char.lower() == "b":
                translation += "o"
            elif char.lower() == "c":
                translation += "m"
            elif char.lower() == "d":
                translation += "e"
            elif char.lower() == "e":
                translation += "f"
            elif char.lower() == "f":
                translation += "y"
            elif char.lower() == "g":
                translation += "q"
            elif char.lower() == "h":
                translation += "b"
            elif char.lower() == "i":
                translation += "p"
            elif char.lower() == "j":
                translation += "c"
            elif char.lower() == "k":
                translation += "n"

            elif char.lower() == "l":
                translation += "v"

            elif char.lower() == "m":
                translation += "x"

            elif char.lower() == "n":
                translation += "t"

            elif char.lower() == "o":
                translation += "d"


            elif char.lower() == "p":
                translation += "w"

            elif char.lower() == "q":
                translation += "h"

            elif char.lower() == "r":
                translation += "i"

            elif char.lower() == "s":
                translation += "a"

            elif char.lower() == "t":
                translation += "z"

            elif char.lower() == "u":
                translation += "j"


            elif char.lower() == "v":
                translation += "r"

            elif char.lower() == "w":
                translation += "k"

            elif char.lower() == "x":
                translation += "g"

            elif char.lower() == "y":
                translation += "l"

            elif char.lower() == "z":
                translation += "s"



            elif char.lower() == " ":
                translation += "0"
            else:
                translation += char
        return translation

    # Example usage
    input_to_encrypt = input("Enter your text : ")
    # translated_text = spelling_translator(input_text)
    print("Encrypted text /data :", yared_encrypt(input_to_encrypt))

def decrrition():
        print("This is decript your data /texts \n")
       # import subprocess

        def yared_decrypt(text):
            translation = ""
            for char in text:
                if char.lower() == "u":
                    translation += "a"
                elif char.lower() == "o":
                    translation += "b"
                elif char.lower() == "m":
                    translation += "c"
                elif char.lower() == "e":
                    translation += "d"
                elif char.lower() == "f":
                    translation += "e"
                elif char.lower() == "y":
                    translation += "f"
                elif char.lower() == "q":
                    translation += "g"
                elif char.lower() == "b":
                    translation += "h"
                elif char.lower() == "p":
                    translation += "i"
                elif char.lower() == "c":
                    translation += "j"
                elif char.lower() == "n":
                    translation += "k"
                elif char.lower() == "v":
                    translation += "l"
                elif char.lower() == "x":
                    translation += "m"
                elif char.lower() == "t":
                    translation += "n"
                elif char.lower() == "d":
                    translation += "o"
                elif char.lower() == "w":
                    translation += "p"
                elif char.lower() == "h":
                    translation += "q"
                elif char.lower() == "i":
                    translation += "r"
                elif char.lower() == "a":
                    translation += "s"
                elif char.lower() == "z":
                    translation += "t"
                elif char.lower() == "j":
                    translation += "u"
                elif char.lower() == "r":
                    translation += "v"
                elif char.lower() == "k":
                    translation += "w"
                elif char.lower() == "g":
                    translation += "x"
                elif char.lower() == "l":
                    translation += "y"
                elif char.lower() == "s":
                    translation += "z"
                elif char.lower() == "0":
                    translation += " "
                else:
                    translation += char
            return translation

        # Example usage
        input_to_decrypt = input("Enter encrypted text : ")
        print("decrypted text /data :", yared_decrypt(input_to_decrypt))


if choice == "help":
    help()
elif choice == "enco" :
    encryption()
elif choice == "deco":
    decrrition()
elif choice == "man":
    man()
