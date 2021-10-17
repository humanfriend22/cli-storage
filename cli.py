print("App Starting...")


def addKeyAndValue(key, value):
    keysFile = open("keys.txt", "r")
    arr = keysFile.readlines()
    arrLength = len(arr)
    arrLength -= 1
    arr.append(key + "\n")
    new_file_contents = "".join(arr)
    keysFile.close()
    keysFile = open("keys.txt", "w")
    keysFile.write(new_file_contents)
    keysFile.close()

    valuesFile = open("values.txt", "r")
    valuesArr = valuesFile.readlines()
    valuesArrLength = len(valuesArr)
    valuesArrLength -= 1
    valuesArr.append(value + "\n")
    new_file_contents = "".join(valuesArr)
    valuesFile.close()
    valuesFile = open("values.txt", "w")
    valuesFile.write(new_file_contents)
    valuesFile.close()


def getByKey(p1):
    keysFile = open("keys.txt", "r")
    valuesFile = open("values.txt", "r")
    keysArray = keysFile.readlines()
    valuesArray = valuesFile.readlines()
    indexOfKey = keysArray.index(p1 + "\n")
    value = valuesArray[indexOfKey]
    keysFile.close()
    valuesFile.close()
    return value


def getByValue(p1):
    keysFile = open("keys.txt", "r")
    valuesFile = open("values.txt", "r")
    keysArray = keysFile.readlines()
    valuesArray = valuesFile.readlines()
    indexOfValue = valuesArray.index(p1 + "\n")
    key = keysArray[indexOfValue]
    keysFile.close()
    valuesFile.close()
    return key


def deleteByKey(p1):
    keysFile = open("keys.txt", "r")
    valuesFile = open("values.txt", "r")
    keysArray = keysFile.readlines()
    valuesArray = valuesFile.readlines()
    indexOfKey = keysArray.index(p1 + "\n")
    keysFile.close()
    valuesFile.close()
    keysFile = open("keys.txt", "w")
    valuesFile = open("values.txt", "w")
    keysArray.pop(indexOfKey)
    valuesArray.pop(indexOfKey)
    keysFile.writelines(keysArray)
    valuesFile.writelines(valuesArray)
    keysFile.close()
    valuesFile.close()


def deleteByValue(p1):
    keysFile = open("keys.txt", "r")
    valuesFile = open("values.txt", "r")
    keysArray = keysFile.readlines()
    valuesArray = valuesFile.readlines()
    indexOfValue = valuesArray.index(p1 + "\n")
    keysFile.close()
    valuesFile.close()
    keysFile = open("keys.txt", "w")
    valuesFile = open("values.txt", "w")
    keysArray.pop(indexOfValue)
    valuesArray.pop(indexOfValue)
    keysFile.writelines(keysArray)
    valuesFile.writelines(valuesArray)
    keysFile.close()
    valuesFile.close()


def start():
    print("Enter Command:")
    commandInput = input("> ")
    
    if (commandInput == "store"):
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        addKeyAndValue(key, value)
        start()
    elif (commandInput == "getByKey"):
        key = input("Enter Key: ")
        value = getByKey(key)
        print(value)
        start()
    elif (commandInput == "getByValue"):
        value = input("Enter Value: ")
        key = getByValue(value)
        print(key)
        start()
    elif (commandInput == "delete"):
        deleteBy = input("Delete by: key or value: ")
        if (deleteBy == "key"):
            key = input("Enter Key: ")
            deleteByKey(key)
        elif (deleteBy == "value"):
            value = input("Enter Value: ")
            deleteByValue(value)
        else:
            print("Invalid input. Exit command...")
        start()
    else:
        print("Unknown command")
        start()


start()
