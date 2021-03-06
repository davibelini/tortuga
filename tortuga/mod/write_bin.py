# tortuga: a compiled programming language.
# v0.1
# davibelini <https://github.com/davibelini>
# 2021-Jan-30

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from binascii import unhexlify

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def write_bin(hexdecimal):
    binary_string = unhexlify(hexdecimal)
    try:    
        with open("out.exe", "w+") as new:
            new.write(binary_string)
    except Exception as e:
        print(e)