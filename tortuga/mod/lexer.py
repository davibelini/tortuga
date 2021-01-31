# tortuga: a compiled programming language.
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
        dot = 0
        num_string = self.current_char
        self.advance()
        while (self.current_char.isnumeric() or self.current_char == '.') and self.current_char != None:
            if self.current_char == '.': dot += 1
            if dot < 1: print("more than 1 dot in a number"); break
            num_string += self.current_char
            self.advance()

        return Token(TYPE_NUMBER, int(num_string)) if '.' not in num_string else Token(TYPE_NUMBER, float(num_string))

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