from MyLexer import Lexer

lexer = Lexer().build()
file = open("MyTest.txt")
input_text = file.read()
file.close()
lexer.input(input_text)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
