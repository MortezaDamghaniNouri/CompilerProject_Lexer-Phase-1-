from lexer import Lexer

object1 = Lexer().build()
file = open("MyTest.txt")
input_text = file.read()
file.close()
object1.input(input_text)
while True:
    tok = object1.token()
    if not tok:
        break
    print(tok)
