def addToClipBoard(text):
    import os
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def base64_encode(filedata):
    import base64
    data = filedata
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    addToClipBoard(encodedStr)
    print()
    print("Encoded String:")
    print(encodedStr)
    print()

def base64_decode(filedata):
    import base64
    data = filedata
    decodedBytes = base64.b64decode(data.encode("utf-8"))
    decodedStr = str(decodedBytes, "utf-8")
    addToClipBoard(decodedStr)
    print()
    print("Decoded String:")
    print(decodedStr)
    print()

def base64_encode_save(filedata):
    import base64
    import os
    data = filedata
    encodedBytes = base64.b64encode(data.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")
    addToClipBoard(encodedStr)
    print()
    print("Encoded String:")
    print(encodedStr)
    print()
    desktoppath = os.environ['USERPROFILE']
    desktoppath = desktoppath + "\Desktop"
    desktoppath = desktoppath + "\encoded.txt"
    f = open("destoppath", "x")
    f.close
    save = open(desktoppath, "r+")
    save.write(encodedStr)


def base64_decode_save(filedata):
    import base64
    import os
    data = filedata
    decodedBytes = base64.b64decode(data.encode("utf-8"))
    decodedStr = str(decodedBytes, "utf-8")
    addToClipBoard(decodedStr)
    print()
    print("Decoded String:")
    print(decodedStr)
    print()
    desktoppath = os.environ['USERPROFILE']
    desktoppath = desktoppath + "\Desktop"
    desktoppath = desktoppath + "\encoded.txt"
    f = open("destoppath", "x")
    f.close
    save = open(desktoppath, "r+")
    save.write("test")

def askforpath_encode():
    filepath = input("Drag n Drop your file here: ")
    data = open(filepath, "r")
    filedata = data.read()
    data.close()
    base64_encode(filedata)

def askforpath_decode():
    filepath = input("Drag n Drop your file here: ")
    data = open(filepath, "r")
    filedata = data.read()
    data.close()
    base64_decode(filedata)

def askforpath_encode_save():
    filepath = input("Drag n Drop your file here: ")
    data = open(filepath, "r")
    filedata = data.read()
    data.close()
    base64_encode_save(filedata)

def askforpath_decode_save():
    filepath = input("Drag n Drop your file here: ")
    data = open(filepath, "r")
    filedata = data.read()
    data.close()
    base64_decode_save(filedata)

def menue_encode():
    save = input("Do you want to save it to the Desktop? [y|n] ")
    if save == "y":
        askforpath_encode_save()
        print("Saved to Desktop!")
    elif save == "n":
        askforpath_encode()
        print("Copied to clipboard!")
    else:
        print("That is not a option!")
        menue()

def menue_decode():
    save = input("Do you want to save it to the Desktop? [y|n] ")
    if save == "y":
        askforpath_decode_save()
        print("Saved to Desktop!")
    elif save == "n":
        askforpath_decode()
        print("Copied to clipboard!")
    else:
        print("That is not a option!")
        menue()

def menue():
    print("Base64 Encoder/ Decoder - Phoenixthrush v.1.0")
    #print()

    print("Idk why tf that can´t decode I´m gonna bring version 1.1 and fix this problem")
    print()

    choice = input("Do you want to encode or decode the file? [e|d] ")
    if choice == "e":
        menue_encode()
    elif choice == "d":
        menue_decode()
    else:
        print("That is not a option!")
        menue()

menue()
