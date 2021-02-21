# tortuga: a compiled programming language.
# v0.1
# davibelini <https://github.com/davibelini>
# 2021-Jan-30

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from mod.lexer import Lexer
from mod.parse import parse
from mod.code_gen import gen_hex
from mod.write_bin import write_bin

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from pprint import pprint

from argparse import ArgumentParser

cli_parser = ArgumentParser(description="""
    tortuga: a programming language for the 6502 CPU.
    > tortuga basic_sum.trtg
    > cd out
    > ls
    basic_sum.exe
""")

debug = True

if debug: cli_parser.add_argument("--path", type=str, help="The path of the tortuga file that will be compiled")
else: cli_parser.add_argument("path", type=str, help="The path of the tortuga file that will be compiled")

args = cli_parser.parse_args()

path = args.path

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def error(e):
    print(f"""
    Tortuga
        ERROR: {e}
    """)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def main():

    try:
        src = open(path, "r").read()
    except:
        error("file reading error")

    try:
        lexer = Lexer(src)
        tokens = lexer.tokens()
    except: error("syntax error")

    try:
        ast = parse(tokens)
    except: error("context error")

    try:
        hexa = gen_hex()
    except: error("compilation error")
        
    try:
        write_bin(hexa)
    except: error("file writing error")

# main()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def debug_lexer():
    try:
        s = open("../examples/power.trtg", "r").read()
        lexer = Lexer(s, open("../examples/power.trtg"))
        tokens = lexer.tokens()
        print(tokens)
    except Exception as e: print(e)

    # Expected:
    #    [KEYWORD:fn,
    #    IDENTIFIER:power,
    #    IDENTIFIER:x,
    #    COMMA,
    #    IDENTIFIER:n,
    #    OPEN_C_BRACE,
    #    IDENTIFIER:n,
    #    LESS_THAN,
    #    NUMBER:0,
    #    IF,
    #    KEYWORD:give,
    #    OPEN_PARENTHESIS,
    #    IDENTIFIER:power,
    #    NUMBER:1,
    #    SLASH,
    #    IDENTIFIER:x,
    #    COMMA,
    #    MINUS,
    #   IDENTIFIER:n,
    #    CLOSE_PARENTHESIS,
    #    IDENTIFIER:n,
    #    CHECK_EQUALS,
    #    NUMBER:0,
    #    IF,
    #    KEYWORD:give,
    #   NUMBER:1,
    #    IDENTIFIER:n,
    #    CHECK_EQUALS,
    #    NUMBER:1,
    #    IF,
    #    KEYWORD:give,
    #    IDENTIFIER:x,
    #    IDENTIFIER:n,
    #    DOT,
    #    IDENTIFIER:is_even,
    #    IF,
    #    KEYWORD:give,
    #    OPEN_PARENTHESIS,
    #    IDENTIFIER:power,
    #    IDENTIFIER:x,
    #    STAR,
    #    IDENTIFIER:x,
    #    COMMA,
    #    IDENTIFIER:n,
    #    SLASH,
    #    NUMBER:2,
    #    CLOSE_PARENTHESIS,
    #    IDENTIFIER:n,
    #    DOT,
    #    IDENTIFIER:is_odd,
    #    IF,
    #    KEYWORD:give,
    #    IDENTIFIER:x,
    #    STAR,
    #    OPEN_PARENTHESIS,
    #    IDENTIFIER:power,
    #    IDENTIFIER:x,
    #    STAR,
    #    IDENTIFIER:x,
    #    COMMA,
    #    OPEN_PARENTHESIS,
    #    IDENTIFIER:n,
    #    MINUS,
    #    NUMBER:1,
    #    CLOSE_PARENTHESIS,
    #    SLASH,
    #    NUMBER:2,
    #    CLOSE_PARENTHESIS,
    #    CLOSE_C_BRACE]

debug_lexer()