from TipoToken import TipoToken

class Token:
    """Clase que representa un token del lenguaje"""
    
    def __init__(self, tipo, lexema, opcional=None):
        """
        Constructor de Token
        
        Args:
            tipo: TipoToken - El tipo de token
            lexema: str - El lexema (texto) del token
            opcional: object - Valor opcional asociado al token
        """
        self.tipo = tipo
        self.lexema = lexema
        self.opcional = opcional
    
    def get_tipo(self):
        """Retorna el tipo del token"""
        return self.tipo
    
    def get_lexema(self):
        """Retorna el lexema del token"""
        return self.lexema
    
    def get_opcional(self):
        """Retorna el valor opcional del token"""
        return self.opcional
    
    def __str__(self):
        """Representación en cadena del token"""
        opcional_str = str(self.opcional) if self.opcional is not None else ""
        return f"<{self.tipo.value} {self.lexema} {opcional_str}>"
    
    def __repr__(self):
        """Representación del token para debugging"""
        return self.__str__()
