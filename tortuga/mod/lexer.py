# tortuga: a compiled programming language.
# v0.1
# davibelini <https://github.com/davibelini>
# 2021-Jan-30

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from os import error
from .tokens import Token
from .token_types import *

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Lexer:
    def __init__(self, text):
        self.raw_text = text
        self.text = iter(text)
        self.advance()

    def error(self, e, c_char):
        print(f"""
        Tortuga:
            ERROR: {e}
                At {int(self.raw_text.index(c_char))}
        """)
    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def make_num(self):
        dot = 0
        num_string = self.current_char
        self.advance()
        while self.current_char != None and (self.current_char in "0123456789" or self.current_char == '.'):
            if self.current_char == '.':
                dot += 1
                if dot > 1: self.error("more than 1 dot in a number", '.')
                break
            num_string += self.current_char
            self.advance()

        return Token(TYPE_NUMBER, int(num_string)) if '.' not in num_string else Token(TYPE_NUMBER, float(num_string))

    def make_dash(self):
        if self.current_char != None and self.current_char == '-':
            self.advance()
            if self.current_char != '-':
                self.error("'--' is not an operator", '--') 
                return Token(TYPE_ERROR, None)
            return Token(TYPE_EQUALS, None)
        elif self.current_char != None and self.current_char != '-': return Token(TYPE_MINUS, None)

    def tokens(self):
        toks = []
        while self.current_char != None:
            if self.current_char  == ' ':
                self.advance()
            elif self.current_char  == '\t':
                self.advance()
            elif self.current_char.isnumeric():
                toks.append(self.make_num())

            elif self.current_char == '+':
                self.advance()
                toks.append(Token(TYPE_PLUS, None))

            elif self.current_char == '-':
                self.advance()
                toks.append(self.make_dash())

            elif self.current_char == '*':
                self.advance()
                toks.append(Token(TYPE_STAR, None))

            elif self.current_char == '/':
                self.advance()
                toks.append(Token(TYPE_SLASH, None))

            else:
                self.error(f"illegal character '{self.current_char}'", self.current_char)
                break
        return toks