from TipoToken import TipoToken

class Token:
    """Clase que representa un token del lenguaje"""
    
    def __init__(self, tipo, lexema, literal, linea):
        """
        Constructor de Token
        
        Args:
            tipo: TipoToken - El tipo de token (PLUS, MINUS, etc.)
            lexema: str - El texto original ("+", "var", "123")
            literal: object - El valor real (5.0, "hola", None). Antes 'opcional'.
            linea: int - El número de línea donde aparece el token.
        """
        self.tipo = tipo
        self.lexema = lexema
        self.literal = literal
        self.linea = linea

    def __str__(self):
        """Representación en cadena para imprimir"""
        # Esto ayuda a ver qué está pasando cuando imprimes tokens
        val = self.literal if self.literal is not None else ""
        return f"{self.tipo} {self.lexema} {val}"

    def __repr__(self):
        return self.__str__()