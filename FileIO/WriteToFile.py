def WriteToFile(toBewritten,FileName="out",FileType=".txt",WriteType="w+"):
    FileName = FileName+FileType
    text_file = open(FileName, WriteType)
    text_file.write(toBewritten)
    text_file.close()
