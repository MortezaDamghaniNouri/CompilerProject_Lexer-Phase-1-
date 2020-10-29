from lexer import Lexer

object1 = Lexer().build()
inputFile = open("test1.txt")
inputText = inputFile.read()
inputFile.close()
outputFile = open("test1 result.txt", "w")
object1.input(inputText)
while True:
    tok = object1.token()
    if not tok:
        break
    print(tok)
    outputFile.write(str(tok)+"\n")
outputFile.close()
