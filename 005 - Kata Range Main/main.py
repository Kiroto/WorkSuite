from KRange.range import Range

def exitFunct():
    return -1

functions = {
    "exit": exitFunct
}


if __name__ == "__main__":
    while(True):
        usrIn = input().lower()
        toExecute = functions[usrIn]
        if (toExecute() == -1):
            break

