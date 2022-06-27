from KRange.range import Range

def exitFunct():
    return -1

def enterFunct():
    return 0

functions = {
    "exit": exitFunct,
    "enter": enterFunct
}


if __name__ == "__main__":
    while(True):
        usrIn = input().lower()
        toExecute = functions[usrIn]
        
        if (usrIn in functions.keys):
            toExecute = functions[usrIn]
            if (toExecute() == -1):
                break
            # program

        

