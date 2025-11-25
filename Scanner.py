from Token import Token
from TipoToken import TipoToken

class Scanner:
    """Analizador léxico (Scanner) para el lenguaje"""
    
    def __init__(self, source):
        """
        Constructor del Scanner
        
        Args:
            source: str - La cadena de entrada a analizar
        """
        self.source = source
        self.tokens = []
        self.inicio = 0
        self.actual = 0
        self.linea = 1
        self.errores = []
    
    def scan(self):
        """
        Realiza el análisis léxico de la cadena de entrada
        
        Returns:
            list: Lista de tokens generados
        
        Raises:
            Exception: Si hay errores léxicos
        """
        while not self.is_at_end():
            self.inicio = self.actual
            self.scan_token()
        
        # Agregar token EOF al final
        self.tokens.append(Token(TipoToken.EOF, "$"))
        
        # Si hay errores, lanzar excepción
        if self.errores:
            raise Exception("\n".join(self.errores))
        
        return self.tokens
    
    def scan_token(self):
        """Escanea un token individual"""
        c = self.advance()
        
        # Ignorar espacios en blanco
        if c in [' ', '\r', '\t']:
            return
        
        # Nueva línea
        if c == '\n':
            self.linea += 1
            return
        
        # Operadores y símbolos de un solo caracter
        if c == '(':
            self.add_token(TipoToken.LEFT_PAREN)
        elif c == ')':
            self.add_token(TipoToken.RIGHT_PAREN)
        elif c == ',':
            self.add_token(TipoToken.COMMA)
        elif c == ';':
            self.add_token(TipoToken.SEMICOLON)
        elif c == '-':
            self.add_token(TipoToken.MINUS)
        elif c == '+':
            self.add_token(TipoToken.PLUS)
        elif c == '/':
            self.add_token(TipoToken.SLASH)
        elif c == '*':
            self.add_token(TipoToken.STAR)
        elif c == '%':
            self.add_token(TipoToken.MOD)
        elif c == '=':
            # Puede ser = o ==
            if self.match('='):
                self.add_token(TipoToken.EQUAL_EQUAL)
            else:
                self.add_token(TipoToken.EQUAL)
        elif c == '"':
            # Cadena de texto
            self.string()
        elif self.is_digit(c):
            # Número
            self.number()
        elif self.is_alpha(c):
            # Identificador o palabra reservada
            self.identifier()
        else:
            self.error(f"Caracter inesperado: '{c}'")
    
    def string(self):
        """Escanea una cadena de texto"""
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.linea += 1
            self.advance()
        
        if self.is_at_end():
            self.error("Cadena sin cerrar")
            return
        
        # Consumir la comilla de cierre
        self.advance()
        
        # Obtener el valor de la cadena (sin las comillas)
        valor = self.source[self.inicio + 1:self.actual - 1]
        self.add_token(TipoToken.STRING, valor)
    
    def number(self):
        """Escanea un número"""
        while self.is_digit(self.peek()):
            self.advance()
        
        # Buscar parte decimal
        if self.peek() == '.' and self.is_digit(self.peek_next()):
            # Consumir el punto
            self.advance()
            
            while self.is_digit(self.peek()):
                self.advance()
        
        valor = float(self.source[self.inicio:self.actual])
        self.add_token(TipoToken.NUMBER, valor)
    
    def identifier(self):
        """Escanea un identificador o palabra reservada"""
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        
        text = self.source[self.inicio:self.actual]
        
        # Verificar si es la palabra reservada 'null'
        if text == 'null':
            self.add_token(TipoToken.NULL)
        else:
            self.add_token(TipoToken.IDENTIFIER)
    
    def match(self, expected):
        """
        Verifica si el caracter actual coincide con el esperado
        
        Args:
            expected: str - Caracter esperado
            
        Returns:
            bool: True si coincide, False en caso contrario
        """
        if self.is_at_end():
            return False
        if self.source[self.actual] != expected:
            return False
        
        self.actual += 1
        return True
    
    def peek(self):
        """
        Retorna el caracter actual sin consumirlo
        
        Returns:
            str: Caracter actual o '\0' si está al final
        """
        if self.is_at_end():
            return '\0'
        return self.source[self.actual]
    
    def peek_next(self):
        """
        Retorna el siguiente caracter sin consumirlo
        
        Returns:
            str: Siguiente caracter o '\0' si está al final
        """
        if self.actual + 1 >= len(self.source):
            return '\0'
        return self.source[self.actual + 1]
    
    def is_alpha(self, c):
        """
        Verifica si un caracter es alfabético
        
        Args:
            c: str - Caracter a verificar
            
        Returns:
            bool: True si es alfabético o '_', False en caso contrario
        """
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'
    
    def is_digit(self, c):
        """
        Verifica si un caracter es un dígito
        
        Args:
            c: str - Caracter a verificar
            
        Returns:
            bool: True si es dígito, False en caso contrario
        """
        return c >= '0' and c <= '9'
    
    def is_alpha_numeric(self, c):
        """
        Verifica si un caracter es alfanumérico
        
        Args:
            c: str - Caracter a verificar
            
        Returns:
            bool: True si es alfanumérico, False en caso contrario
        """
        return self.is_alpha(c) or self.is_digit(c)
    
    def is_at_end(self):
        """
        Verifica si se llegó al final de la cadena
        
        Returns:
            bool: True si está al final, False en caso contrario
        """
        return self.actual >= len(self.source)
    
    def advance(self):
        """
        Avanza al siguiente caracter y retorna el actual
        
        Returns:
            str: Caracter actual
        """
        c = self.source[self.actual]
        self.actual += 1
        return c
    
    def add_token(self, tipo, opcional=None):
        """
        Agrega un token a la lista de tokens
        
        Args:
            tipo: TipoToken - Tipo del token
            opcional: object - Valor opcional del token
        """
        text = self.source[self.inicio:self.actual]
        self.tokens.append(Token(tipo, text, opcional))
    
    def error(self, mensaje):
        """
        Registra un error léxico
        
        Args:
            mensaje: str - Mensaje de error
        """
        error_msg = f"[línea {self.linea}] Error: {mensaje}"
        self.errores.append(error_msg)
