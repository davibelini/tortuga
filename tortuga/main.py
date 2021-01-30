# tortuga: a programming language for the 6502 CPU.
# v0.1
# davibelini <https://github.com/davibelini>
# 2021-Jan-30

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from .mod.lexer import Lexer
from .mod.parse import parse
from .mod.code_gen import gen_6502
from .mod.write_hexa import write_hex

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from argparse import ArgumentParser

cli_parser = ArgumentParser(description="""
    tortuga: a programming language for the 6502 CPU.
    > tortuga basic_sum.trtg
    > cd out
    > ls
    basic_sum.exe
""")

cli_parser.add_argument("path", type=str, help="The path of the tortuga file that will be compiled")

args = cli_parser.parse_args()

path = args.path

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def main():

    try:
        src = open(path).read()
    except:
        print("file reading error")

    try:
        lexer = Lexer(src)
        tokens = lexer.tokens()
    except: print("syntax error")

    try:
        ast = parse(tokens)
    except: print("context error")

    try:
        hexa = gen_6502()
    except: print("compilation error")
        
    try:
        write_hex(hexa)
    except: print("file writing error")

main()