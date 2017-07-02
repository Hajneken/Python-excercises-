
def writeTextToFile(x):
    STATICKY_TEXT="This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
    finalText = STATICKY_TEXT+str(x)
    file = open('myfile', 'w')
    file.write(finalText)
    file.close()
    fName = file.name
    return fName
text = "text"
fileName =writeTextToFile(text)
print(fileName)