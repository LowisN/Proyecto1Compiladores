# Módulo: Analizador léxico (Scanner)
# Convierte la entrada de texto en una lista de tokens que el parser consumirá.
from Token import Token
from TipoToken import TipoToken

class Scanner:
    """Analizador léxico (Scanner) para el lenguaje"""
    
    def __init__(self, source):
        # source: cadena fuente a tokenizar
        # tokens: lista resultante de Token
        # inicio: índice donde comienza el lexema actual
        # actual: índice del cursor actual en la fuente
        # linea: número de línea actual para reportes de error
        # errores: lista de mensajes de error encontrados durante el escaneo
        self.source = source
        self.tokens = []
        self.inicio = 0
        self.actual = 0
        self.linea = 1
        self.errores = []
    
    def scan(self):
        """Realiza el análisis léxico de la fuente completa y devuelve la lista de tokens."""
        # Recorre la fuente hasta el final, tokenizando lexema por lexema.
        while not self.is_at_end():
            self.inicio = self.actual
            self.scan_token()
        
        # CORRECCIÓN IMPORTANTE: 
        # Token EOF debe tener 4 argumentos: Tipo, Lexema, Literal, Línea
        self.tokens.append(Token(TipoToken.EOF, "", None, self.linea))
        
        if self.errores:
            # Imprime los errores acumulados para depuración.
            error_msg = "\n".join(self.errores)
            print(f"Errores de escaneo: {error_msg}")
            # Si prefieres que detenga todo, descomenta la siguiente línea:
            # raise Exception(error_msg)
        
        return self.tokens
    
    def scan_token(self):
        """Lee el siguiente carácter y genera el token correspondiente."""
        c = self.advance()
        
        # Ignorar espacios en blanco y tabs
        if c in [' ', '\r', '\t']:
            return
        
        # Nueva línea: incrementar contador de líneas
        if c == '\n':
            self.linea += 1
            return
        
        # Operadores y símbolos simples
        if c == '(': self.add_token(TipoToken.LEFT_PAREN)
        elif c == ')': self.add_token(TipoToken.RIGHT_PAREN)
        elif c == ',': self.add_token(TipoToken.COMMA)
        elif c == ';': self.add_token(TipoToken.SEMICOLON)
        elif c == '-': self.add_token(TipoToken.MINUS)
        elif c == '+': self.add_token(TipoToken.PLUS)
        elif c == '/': self.add_token(TipoToken.SLASH)
        elif c == '*': self.add_token(TipoToken.STAR)
        elif c == '%': self.add_token(TipoToken.MOD)
        elif c == '=':
            # Puede ser asignación (=) o comparación (==)
            token = TipoToken.EQUAL_EQUAL if self.match('=') else TipoToken.EQUAL
            self.add_token(token)
        elif c == '"':
            # Inicia literal de cadena
            self.string()
        elif self.is_digit(c):
            # Inicia literal numérico
            self.number()
        elif self.is_alpha(c):
            # Identificador o palabra reservada
            self.identifier()
        else:
            # Carácter no reconocido
            self.error(f"Caracter inesperado: '{c}'")
    
    def string(self):
        """Procesa literales de cadena encerradas en comillas dobles."""
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.linea += 1
            self.advance()
        
        if self.is_at_end():
            self.error("Cadena sin cerrar")
            return
        
        self.advance() # Consumir la comilla de cierre
        
        # Extraer el contenido sin las comillas
        valor = self.source[self.inicio + 1:self.actual - 1]
        self.add_token(TipoToken.STRING, valor)
    
    def number(self):
        """Procesa literales numéricos (enteros y decimales)."""
        while self.is_digit(self.peek()):
            self.advance()
        
        # Parte decimal opcional
        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()
        
        valor = float(self.source[self.inicio:self.actual])
        self.add_token(TipoToken.NUMBER, valor)
    
    def identifier(self):
        """Procesa identificadores y palabras reservadas."""
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        
        text = self.source[self.inicio:self.actual]
        
        # Mapeo simple para palabras reservadas
        if text == 'null':
            self.add_token(TipoToken.NULL)
        elif text == 'false': # Soporte booleano literal
            self.add_token(TipoToken.FALSE)
        elif text == 'true':
            self.add_token(TipoToken.TRUE)
        else:
            # Si no es palabra reservada, es un identificador
            self.add_token(TipoToken.IDENTIFIER)
    
    # --- MÉTODOS AUXILIARES ---
    
    def add_token(self, tipo, literal=None):
        """Crea y añade un token a la lista con su lexema, literal y línea."""
        # CORRECCIÓN IMPORTANTE: 
        # Se envía self.linea para que el Token sepa dónde está
        text = self.source[self.inicio:self.actual]
        self.tokens.append(Token(tipo, text, literal, self.linea))

    def advance(self):
        """Consume el siguiente carácter y devuelve el anterior."""
        self.actual += 1
        return self.source[self.actual - 1]

    def match(self, expected):
        """Consume el carácter siguiente si coincide con 'expected'."""
        if self.is_at_end(): return False
        if self.source[self.actual] != expected: return False
        self.actual += 1
        return True

    def peek(self):
        """Devuelve el carácter actual sin consumirlo."""
        if self.is_at_end(): return '\0'
        return self.source[self.actual]

    def peek_next(self):
        """Devuelve el siguiente carácter sin consumirlo."""
        if self.actual + 1 >= len(self.source): return '\0'
        return self.source[self.actual + 1]

    def is_alpha(self, c):
        """Comprueba si c es una letra o guion bajo (para identificadores)."""
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'

    def is_digit(self, c):
        """Comprueba si c es un dígito decimal."""
        return c >= '0' and c <= '9'

    def is_alpha_numeric(self, c):
        """Comprueba si c es letra o dígito (parte de un identificador)."""
        return self.is_alpha(c) or self.is_digit(c)

    def is_at_end(self):
        """Indica si se llegó al final de la fuente."""
        return self.actual >= len(self.source)

    def error(self, mensaje):
        """Registra un error encontrado durante el escaneo (no lanza excepción)."""
        self.errores.append(f"[línea {self.linea}] Error: {mensaje}")