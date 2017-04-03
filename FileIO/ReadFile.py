def readfile():    #reads str into memory calls it f
    text_file = open("file.txt","r")
    f = text_file.read()
	return f