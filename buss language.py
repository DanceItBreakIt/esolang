from sly import Lexer

class BasicLexer(Lexer):
    tokens = { NAME, NUMBER, STRING }
    ignore = '\t '
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';'}

    # define tokens as regular expressions
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    # number token
    @_(r'\d+')
    def NUMBER(self, t):
        # convert it to a python integer
        t.value = int(t.value)
        return t
    
    # comment token
    @_(r'🗣️.*')
    def COMMENT(self, t):
        pass