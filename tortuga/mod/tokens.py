# tortuga: a compiled programming language.
# v0.1
# davibelini <https://github.com/davibelini>
# 2021-Jan-30

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class Token:
    def __init__(self, _type, _value) -> None:
        self.type =_type
        self.value = _value
    
    def __repr__(self):
        return f"{self.type}:{self.value}" if self.value != None else f"{self.type}"