# tortuga: a compiled programming language.
# v0.1
# davibelini <https://github.com/davibelini>
# 2021-Jan-30

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Grammar:
#   program     ::= {statement}
#   statement   ::= if | fn | give # for the time being
#   comparison  ::= TRUE | FALSE
#   if          ::= comparison TOKEN:IF statement
#   fn          ::= TOKEN:FN [{TOKEN:IDENTIFIER TOKEN:COMMA} TOKEN_IDENTIFIER] OPEN_C_BRACE [{statement}] CLOSE_C_BRACE

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from .token_types import *
from .tokens import Token

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def token_matches(t, t2):
    if t.type == t2.type and t.value == t2.value:
        return True
    else:
        return False

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def parse(toks):
    cur_tok = ''

    def advance():
        global index
        index = -1
        index += 1
        cur_tok = toks[index] if toks[index] != None else None

    def peek():
        global index
        return toks[index + 1]

    def behind():
        global index
        return toks[index - 1]
    
    advance()

    def program():
        while cur_tok != None:
            statement()
    
    def statement():
        while cur_tok != None:
            if token_matches(cur_tok, Token(TYPE_KEYWORD, "fn")):
                print("fn statement")

            if token_matches(cur_tok, Token(TYPE_KEYWORD, "give")):
                print("give statement")

            advance()

    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

    return program()