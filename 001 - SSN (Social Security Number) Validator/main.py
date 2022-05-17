from ssnValidator import validateSsn
import platform    # For obtaining the operating system information
import os          # Import the os module to clear screen


def clr_scr():
    #Python program to clear screen
    #Get command to execute
    if(platform.system().lower() == "windows"):
        cmd = 'cls'
    else:
        cmd = 'clear'
    # Run command
    os.system(cmd)

def getUserString(prompt: str):
    print(prompt)
    userInput = input()
    return userInput

def main():
    while(True):
        usrIn = getUserString("Input the text to check for SSN Validity\n(or \"exit\" to exit)\n(An SSN has the following format: XXX-YY-ZZZZ where XXX cannot be 000, 666, or 900-999; YY cannot be 00, and ZZZZ cannot be 0000)")
        if (usrIn.lower() == "exit"):
            break
        clr_scr()
        if (validateSsn(usrIn)):
            print("The text \"" + usrIn + "\" is a valid SSN")
        else:
            print("The text \"" + usrIn + "\" is not a valid SSN")


if __name__ == "__main__":
    main()