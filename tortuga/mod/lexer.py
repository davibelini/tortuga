# tortuga: a programming language for the 6502 CPU.
# v0.1
# davibelini <https://github.com/davibelini>
# 2021-Jan-30

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from .tokens import Token
from .token_types import *

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = 0

    def make_num(self):
        num_string = self.current_char
        self.advance()
        while self.current_char.isnumeric() and self.current_char != None:
            self.advance()
            num_string += self.current_char

        return Token(TYPE_NUMBER, int(num_string))

    def tokens(self):
        toks = []
        while self.current_char != None:
            if self.current_char.isnumeric():
                toks.append(self.make_num())
                self.advance()

            elif self.current_char == '+':
                self.advance()
                toks.append(Token(TYPE_PLUS, None))

            elif self.current_char == '-':
                self.advance()
                toks.append(Token(TYPE_MINUS, None))

            elif self.current_char == '*':
                self.advance()
                toks.append(Token(TYPE_STAR, None))

            elif self.current_char == '/':
                self.advance()
                toks.append(Token(TYPE_SLASH, None))
        return toks