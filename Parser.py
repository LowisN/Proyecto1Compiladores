from Token import Token
from TipoToken import TipoToken

class Parser:
    """
    Analizador sintáctico predictivo (Parser) para el lenguaje.
    
    Gramática implementada (descenso recursivo predictivo):
    
    STATEMENT -> EXPRESSION SEMICOLON_OPC
    SEMICOLON_OPC -> ; | Ɛ
    EXPRESSION -> ASSIGNMENT
    ASSIGNMENT -> TERM ASSIGNMENT_OPC
    ASSIGNMENT_OPC -> = EXPRESSION | Ɛ
    TERM -> FACTOR TERM'
    TERM' -> - TERM | + TERM | Ɛ
    FACTOR -> UNARY FACTOR'
    FACTOR' -> / FACTOR | * FACTOR | % FACTOR | Ɛ
    UNARY -> - UNARY | CALL
    CALL -> PRIMARY CALL'
    CALL' -> ( ARGUMENTS ) | Ɛ
    PRIMARY -> null | number | string | id | ( EXPRESSION )
    ARGUMENTS -> EXPRESSION ARGUMENTS' | Ɛ
    ARGUMENTS' -> , EXPRESSION ARGUMENTS' | Ɛ
    """
    
    def __init__(self, tokens):
        """
        Constructor del Parser
        
        Args:
            tokens: list - Lista de tokens a analizar
        """
        self.tokens = tokens
        self.actual = 0
        self.errores = []
    
    def parse(self):
        """
        Inicia el análisis sintáctico
        
        Returns:
            bool: True si el análisis fue exitoso, False en caso contrario
            
        Raises:
            Exception: Si hay errores sintácticos
        """
        try:
            self.statement()
            
            if self.errores:
                raise Exception("\n".join(self.errores))
            
            return True
        except Exception as e:
            if not self.errores:
                self.errores.append(str(e))
            raise Exception("\n".join(self.errores))
    
    def statement(self):
        """STATEMENT -> EXPRESSION SEMICOLON_OPC"""
        self.expression()
        self.semicolon_opc()
        
        # Verificar que estamos en EOF
        if not self.is_at_end():
            self.error("Se esperaba fin de cadena después de la sentencia")
    
    def semicolon_opc(self):
        """SEMICOLON_OPC -> ; | Ɛ"""
        self.match(TipoToken.SEMICOLON)  # Opcional, no falla si no está
    
    def expression(self):
        """EXPRESSION -> ASSIGNMENT"""
        self.assignment()
    
    def assignment(self):
        """ASSIGNMENT -> TERM ASSIGNMENT_OPC"""
        self.term()
        self.assignment_opc()
    
    def assignment_opc(self):
        """ASSIGNMENT_OPC -> = EXPRESSION | Ɛ"""
        if self.match(TipoToken.EQUAL):
            self.expression()
    
    def term(self):
        """TERM -> FACTOR TERM'"""
        self.factor()
        self.term_prime()
    
    def term_prime(self):
        """TERM' -> - TERM | + TERM | Ɛ"""
        if self.match(TipoToken.MINUS):
            self.term()
        elif self.match(TipoToken.PLUS):
            self.term()
        # Ɛ - no hacer nada
    
    def factor(self):
        """FACTOR -> UNARY FACTOR'"""
        self.unary()
        self.factor_prime()
    
    def factor_prime(self):
        """FACTOR' -> / FACTOR | * FACTOR | % FACTOR | Ɛ"""
        if self.match(TipoToken.SLASH):
            self.factor()
        elif self.match(TipoToken.STAR):
            self.factor()
        elif self.match(TipoToken.MOD):
            self.factor()
        # Ɛ - no hacer nada
    
    def unary(self):
        """UNARY -> - UNARY | CALL"""
        if self.match(TipoToken.MINUS):
            self.unary()
        else:
            self.call()
    
    def call(self):
        """CALL -> PRIMARY CALL'"""
        self.primary()
        self.call_prime()
    
    def call_prime(self):
        """CALL' -> ( ARGUMENTS ) | Ɛ"""
        if self.match(TipoToken.LEFT_PAREN):
            self.arguments()
            if not self.match(TipoToken.RIGHT_PAREN):
                self.error("Se esperaba ')' después de los argumentos")
        # Ɛ - no hacer nada
    
    def primary(self):
        """PRIMARY -> null | number | string | id | ( EXPRESSION )"""
        if self.match(TipoToken.NULL):
            return
        
        if self.match(TipoToken.NUMBER):
            return
        
        if self.match(TipoToken.STRING):
            return
        
        if self.match(TipoToken.IDENTIFIER):
            return
        
        if self.match(TipoToken.LEFT_PAREN):
            self.expression()
            if not self.match(TipoToken.RIGHT_PAREN):
                self.error("Se esperaba ')' después de la expresión")
            return
        
        # Si llegamos aquí, hay un error
        token_actual = self.peek()
        self.error(f"Expresión esperada, se encontró: '{token_actual.lexema}'")
    
    def arguments(self):
        """ARGUMENTS -> EXPRESSION ARGUMENTS' | Ɛ"""
        # Verificar si hay argumentos (Ɛ)
        if self.check(TipoToken.RIGHT_PAREN):
            return  # Ɛ - no hay argumentos
        
        self.expression()
        self.arguments_prime()
    
    def arguments_prime(self):
        """ARGUMENTS' -> , EXPRESSION ARGUMENTS' | Ɛ"""
        if self.match(TipoToken.COMMA):
            self.expression()
            self.arguments_prime()  # Recursión
        # Ɛ - no hacer nada
    
    def match(self, *tipos):
        """
        Verifica si el token actual coincide con alguno de los tipos dados
        
        Args:
            *tipos: TipoToken - Tipos de token a verificar
            
        Returns:
            bool: True si coincide, False en caso contrario
        """
        for tipo in tipos:
            if self.check(tipo):
                self.advance()
                return True
        
        return False
    
    def check(self, tipo):
        """
        Verifica si el token actual es del tipo especificado sin consumirlo
        
        Args:
            tipo: TipoToken - Tipo de token a verificar
            
        Returns:
            bool: True si coincide, False en caso contrario
        """
        if self.is_at_end():
            return False
        return self.peek().tipo == tipo
    
    def advance(self):
        """
        Avanza al siguiente token y retorna el actual
        
        Returns:
            Token: Token actual
        """
        if not self.is_at_end():
            self.actual += 1
        return self.previous()
    
    def is_at_end(self):
        """
        Verifica si se llegó al final de los tokens
        
        Returns:
            bool: True si está al final, False en caso contrario
        """
        return self.peek().tipo == TipoToken.EOF
    
    def peek(self):
        """
        Retorna el token actual sin consumirlo
        
        Returns:
            Token: Token actual
        """
        return self.tokens[self.actual]
    
    def previous(self):
        """
        Retorna el token anterior
        
        Returns:
            Token: Token anterior
        """
        return self.tokens[self.actual - 1]
    
    def error(self, mensaje):
        """
        Registra un error sintáctico
        
        Args:
            mensaje: str - Mensaje de error
        """
        token = self.peek()
        error_msg = f"[Token: {token.lexema}] Error sintáctico: {mensaje}"
        self.errores.append(error_msg)
        raise Exception(error_msg)
