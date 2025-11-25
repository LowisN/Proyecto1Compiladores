from Token import Token
from TipoToken import TipoToken

class Parser:
    """
    Analizador sintáctico predictivo (Parser) para el lenguaje.
    
    Gramática implementada (descenso recursivo predictivo):
    
    programa -> expresion EOF
    expresion -> asignacion
    asignacion -> IDENTIFIER = asignacion | logica_or
    logica_or -> logica_and (== logica_and)*
    logica_and -> igualdad
    igualdad -> comparacion ((==) comparacion)*
    comparacion -> termino
    termino -> factor ((+ | -) factor)*
    factor -> unario ((* | / | %) unario)*
    unario -> (+ | -) unario | primario
    primario -> NUMBER | STRING | null | IDENTIFIER | (expresion) | llamada
    llamada -> IDENTIFIER (argumentos)?
    argumentos -> expresion (, expresion)*
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
            self.programa()
            
            if self.errores:
                raise Exception("\n".join(self.errores))
            
            return True
        except Exception as e:
            if not self.errores:
                self.errores.append(str(e))
            raise Exception("\n".join(self.errores))
    
    def programa(self):
        """programa -> expresion EOF"""
        self.expresion()
        
        # Verificar que estamos en EOF (no es un error, es lo esperado)
        if not self.is_at_end():
            self.error("Se esperaba fin de cadena después de la expresión")
    
    def expresion(self):
        """expresion -> asignacion"""
        self.asignacion()
    
    def asignacion(self):
        """asignacion -> IDENTIFIER = asignacion | logica_or"""
        # Verificar si es una asignación
        if self.check(TipoToken.IDENTIFIER):
            # Guardar la posición actual
            posicion_guardada = self.actual
            self.advance()
            
            if self.match(TipoToken.EQUAL):
                # Es una asignación
                self.asignacion()
                return
            else:
                # No es una asignación, retroceder
                self.actual = posicion_guardada
        
        self.logica_or()
    
    def logica_or(self):
        """logica_or -> logica_and (== logica_and)*"""
        self.logica_and()
        
        while self.match(TipoToken.EQUAL_EQUAL):
            self.logica_and()
    
    def logica_and(self):
        """logica_and -> igualdad"""
        self.igualdad()
    
    def igualdad(self):
        """igualdad -> comparacion ((==) comparacion)*"""
        self.comparacion()
        
        while self.match(TipoToken.EQUAL_EQUAL):
            self.comparacion()
    
    def comparacion(self):
        """comparacion -> termino"""
        self.termino()
    
    def termino(self):
        """termino -> factor ((+ | -) factor)*"""
        self.factor()
        
        while self.match(TipoToken.PLUS, TipoToken.MINUS):
            self.factor()
    
    def factor(self):
        """factor -> unario ((* | / | %) unario)*"""
        self.unario()
        
        while self.match(TipoToken.STAR, TipoToken.SLASH, TipoToken.MOD):
            self.unario()
    
    def unario(self):
        """unario -> (+ | -) unario | primario"""
        if self.match(TipoToken.PLUS, TipoToken.MINUS):
            self.unario()
            return
        
        self.primario()
    
    def primario(self):
        """primario -> NUMBER | STRING | null | IDENTIFIER | (expresion) | llamada"""
        # Literales
        if self.match(TipoToken.NUMBER):
            return
        
        if self.match(TipoToken.STRING):
            return
        
        if self.match(TipoToken.NULL):
            return
        
        # Identificador o llamada a función
        if self.match(TipoToken.IDENTIFIER):
            # Verificar si es una llamada a función
            if self.match(TipoToken.LEFT_PAREN):
                # Es una llamada a función
                if not self.check(TipoToken.RIGHT_PAREN):
                    self.argumentos()
                
                if not self.match(TipoToken.RIGHT_PAREN):
                    self.error("Se esperaba ')' después de los argumentos")
            return
        
        # Expresión entre paréntesis
        if self.match(TipoToken.LEFT_PAREN):
            self.expresion()
            
            if not self.match(TipoToken.RIGHT_PAREN):
                self.error("Se esperaba ')' después de la expresión")
            return
        
        # Si llegamos aquí, hay un error
        token_actual = self.peek()
        self.error(f"Expresión esperada, se encontró: '{token_actual.lexema}'")
    
    def argumentos(self):
        """argumentos -> expresion (, expresion)*"""
        self.expresion()
        
        while self.match(TipoToken.COMMA):
            self.expresion()
    
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
