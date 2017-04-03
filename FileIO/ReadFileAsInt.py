def readint():#Reads file of numbers to int to file
    text_file = open("file.txt", "r")
    numberInt = int(text_file.read())