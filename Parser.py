from Token import Token
from TipoToken import TipoToken
from Expr import Binaria, Unaria, Literal, Agrupacion, Variable, Asignacion, Llamada
from Stmt import Expression, Print

# Parser: transforma la lista de tokens en una lista de sentencias (AST).
class Parser:
    def __init__(self, tokens):
        # tokens: lista de Token
        # actual: índice del token actual
        # errores: coleccion de mensajes de error
        self.tokens = tokens
        self.actual = 0
        self.errores = []

    def parse(self):
        """
        Retorna una lista de sentencias (Stmt) para ser ejecutadas.
        Punto de entrada del parser.
        """
        sentencias = []
        try:
            while not self.is_at_end():
                sentencias.append(self.statement())
            return sentencias
        except Exception as e:
            # Si hay un error, guardamos el mensaje y paramos
            self.errores.append(str(e))
            return None # O lanzar la excepción según prefieras manejarlo

    # -------------------------------------------------------------------------
    # MANEJO DE SENTENCIAS (Lógica del REPL)
    # -------------------------------------------------------------------------
    def statement(self):
        # Parsea una expresión y decide si es Expression (con ;) o Print (implícito)
        expr = self.expression()

        # REQUISITO REPL:
        # Si hay ';', es una Expression Stmt (no imprime).
        # Si NO hay ';', es un Print Stmt implícito (imprime).
        
        if self.match(TipoToken.SEMICOLON):
            return Expression(expr)
        else:
            return Print(expr)

    # -------------------------------------------------------------------------
    # EXPRESIONES
    # -------------------------------------------------------------------------
    def expression(self):
        # Entrada para expresiones: soporta asignaciones
        return self.assignment()

    def assignment(self):
        # assignment -> term ( "=" assignment )?
        # Primero analizamos como si fuera una expresión aritmética normal (R-value)
        expr = self.term()

        # Si encontramos un '=', entonces 'expr' en realidad era el destino (L-value)
        if self.match(TipoToken.EQUAL):
            igual = self.previous() # Guardamos el token '=' para reportar error si falla
            valor = self.assignment() # Recursivo (permite a = b = 5)

            if isinstance(expr, Variable):
                nombre = expr.nombre
                return Asignacion(nombre, valor)
            
            self.error("Destino de asignación inválido.")
        
        return expr

    def term(self):
        # TERM -> FACTOR ( ( - | + ) FACTOR )*
        expr = self.factor()

        while self.match(TipoToken.MINUS, TipoToken.PLUS):
            operador = self.previous()
            derecha = self.factor()
            expr = Binaria(expr, operador, derecha)

        return expr

    def factor(self):
        # FACTOR -> UNARY ( ( / | * | % ) UNARY )*
        expr = self.unary()

        while self.match(TipoToken.SLASH, TipoToken.STAR, TipoToken.MOD):
            operador = self.previous()
            derecha = self.unary()
            expr = Binaria(expr, operador, derecha)
        
        return expr

    def unary(self):
        # UNARY -> ( "-" ) UNARY | call
        if self.match(TipoToken.MINUS):
            operador = self.previous()
            derecha = self.unary()
            return Unaria(operador, derecha)
        
        return self.call()

    def call(self):
        # Permite llamadas a funciones: primary ( "(" arguments? ")" )*
        expr = self.primary()

        # Ciclo infinito para permitir cadenas de llamadas: func()() 
        # Aunque para este caso básico, usualmente corre una vez.
        while True: 
            if self.match(TipoToken.LEFT_PAREN):
                expr = self.finish_call(expr)
            else:
                break
        
        return expr

    def finish_call(self, callee):
        # Parsea la lista de argumentos hasta encontrar ')'
        argumentos = []
        if not self.check(TipoToken.RIGHT_PAREN):
            while True:
                argumentos.append(self.expression())
                if not self.match(TipoToken.COMMA):
                    break
        
        paren = self.consume(TipoToken.RIGHT_PAREN, "Se esperaba ')' después de los argumentos")
        
        # 'callee' es la expresión de la función (ej. Variable "sin")
        return Llamada(callee, paren, argumentos)

    def primary(self):
        # Valores básicos y agrupaciones
        if self.match(TipoToken.NULL):
            return Literal(None)
        
        if self.match(TipoToken.FALSE): # Asumiendo que agregaste booleanos
             return Literal(False)
        
        if self.match(TipoToken.TRUE):
             return Literal(True)

        if self.match(TipoToken.NUMBER, TipoToken.STRING):
            return Literal(self.previous().literal)

        if self.match(TipoToken.IDENTIFIER):
            return Variable(self.previous())

        if self.match(TipoToken.LEFT_PAREN):
            expr = self.expression()
            self.consume(TipoToken.RIGHT_PAREN, "Se esperaba ')' después de la expresión")
            return Agrupacion(expr)

        raise Exception(f"Se esperaba una expresión. Token actual: {self.peek().lexema}")

    # -------------------------------------------------------------------------
    # AUXILIARES (Match, Consume, etc.)
    # -------------------------------------------------------------------------
    
    def match(self, *tipos):
        # Si el token actual coincide con uno de los tipos, avanza y devuelve True
        for tipo in tipos:
            if self.check(tipo):
                self.advance()
                return True
        return False
    
    def consume(self, tipo, mensaje):
        # Consume un token esperado o lanza error con mensaje
        if self.check(tipo):
            return self.advance()
        self.error(mensaje)

    def check(self, tipo):
        # Comprueba si el token actual es de tipo 'tipo'
        if self.is_at_end(): return False
        return self.peek().tipo == tipo

    def advance(self):
        # Avanza al siguiente token y devuelve el anterior
        if not self.is_at_end():
            self.actual += 1
        return self.previous()

    def is_at_end(self):
        # True cuando el token actual es EOF
        return self.peek().tipo == TipoToken.EOF

    def peek(self):
        # Devuelve el token actual sin consumirlo
        return self.tokens[self.actual]

    def previous(self):
        # Devuelve el token anterior (ya consumido)
        return self.tokens[self.actual - 1]

    def error(self, mensaje):
        # Construye y lanza una excepción formateada con línea y lexema
        token = self.peek()
        msg_final = f"Error en línea {token.linea} ('{token.lexema}'): {mensaje}"
        raise Exception(msg_final)