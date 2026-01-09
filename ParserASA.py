# -*- coding: utf-8 -*-
from TipoToken import TipoToken
from AST import (
    ParseError,
    Literal, Variable, Assign, Unary, Binary, Grouping, Call,
    ExprStmt
)

class Parser:
    """
    Parser (descenso recursivo) que CONSTRUYE el ASA (árbol de sintaxis abstracta).

    Gramática (equivalente a la tuya, pero construyendo nodos y con asociatividad izquierda
    para +,-,*,/,%):

    STATEMENT    -> EXPRESSION SEMICOLON_OPC EOF
    SEMICOLON_OPC-> ; | ε

    EXPRESSION   -> ASSIGNMENT
    ASSIGNMENT   -> TERM ( "=" EXPRESSION )?      (solo si LHS es Variable)

    TERM         -> FACTOR ( ( "+" | "-" ) FACTOR )*
    FACTOR       -> UNARY  ( ( "*" | "/" | "%" ) UNARY )*
    UNARY        -> "-" UNARY | CALL
    CALL         -> PRIMARY ( "(" ARGUMENTS? ")" )?
    PRIMARY      -> null | number | string | id | "(" EXPRESSION ")"

    ARGUMENTS    -> EXPRESSION ( "," EXPRESSION )*
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.actual = 0

    # ---------------------------
    # Entrada
    # ---------------------------

    def parse(self):
        stmt = self.statement()
        if not self.is_at_end():
            self.error("Se esperaba fin de cadena después de la sentencia")
        return stmt

    # ---------------------------
    # STATEMENT
    # ---------------------------

    def statement(self):
        expr = self.expression()
        has_semicolon = self.match(TipoToken.SEMICOLON)
        # si NO hay ';' se imprime en el REPL
        print_result = not has_semicolon
        return ExprStmt(expr, print_result)

    # ---------------------------
    # EXPRESSION
    # ---------------------------

    def expression(self):
        return self.assignment()

    def assignment(self):
        expr = self.term()

        if self.match(TipoToken.EQUAL):
            value = self.expression()
            # Regla semántica pedida:
            # el lado izquierdo debe ser un identificador (Variable).
            if isinstance(expr, Variable):
                return Assign(expr.name, value)
            # Esto cubre casos como: 5 + x = 12 - 3
            raise ParseError("Asignación inválida: se esperaba un identificador del lado izquierdo (ej: x = 12 - 3).")

        return expr

    # ---------------------------
    # TERM / FACTOR (asociatividad izquierda)
    # ---------------------------

    def term(self):
        expr = self.factor()
        while True:
            if self.match(TipoToken.PLUS):
                right = self.factor()
                expr = Binary(expr, "+", right)
            elif self.match(TipoToken.MINUS):
                right = self.factor()
                expr = Binary(expr, "-", right)
            else:
                break
        return expr

    def factor(self):
        expr = self.unary()
        while True:
            if self.match(TipoToken.STAR):
                right = self.unary()
                expr = Binary(expr, "*", right)
            elif self.match(TipoToken.SLASH):
                right = self.unary()
                expr = Binary(expr, "/", right)
            elif self.match(TipoToken.MOD):
                right = self.unary()
                expr = Binary(expr, "%", right)
            else:
                break
        return expr

    def unary(self):
        if self.match(TipoToken.MINUS):
            right = self.unary()
            return Unary("-", right)
        return self.call()

    # ---------------------------
    # CALL
    # ---------------------------

    def call(self):
        expr = self.primary()

        # Solo soportamos UNA llamada (como en tu gramática CALL')
        if self.match(TipoToken.LEFT_PAREN):
            # Regla semántica pedida:
            # no existe una función llamada "4" (o cualquier cosa que no sea id).
            if not isinstance(expr, Variable):
                raise ParseError("Llamada a función inválida: el nombre de la función debe ser un identificador (ej: sin(1)).")

            args = []
            if not self.check(TipoToken.RIGHT_PAREN):
                args.append(self.expression())
                while self.match(TipoToken.COMMA):
                    args.append(self.expression())

            if not self.match(TipoToken.RIGHT_PAREN):
                self.error("Se esperaba ')' después de los argumentos")

            return Call(expr.name, args)

        return expr

    # ---------------------------
    # PRIMARY
    # ---------------------------

    def primary(self):
        if self.match(TipoToken.NULL):
            return Literal(None)

        if self.match(TipoToken.NUMBER):
            # opcional contiene el valor float
            return Literal(self.previous().opcional)

        if self.match(TipoToken.STRING):
            # opcional contiene la cadena sin comillas
            return Literal(self.previous().opcional)

        if self.match(TipoToken.IDENTIFIER):
            return Variable(self.previous().lexema)

        if self.match(TipoToken.LEFT_PAREN):
            expr = self.expression()
            if not self.match(TipoToken.RIGHT_PAREN):
                self.error("Se esperaba ')' después de la expresión")
            return Grouping(expr)

        token_actual = self.peek()
        self.error(f"Expresión esperada, se encontró: '{token_actual.lexema}'")

    # ---------------------------
    # Helpers
    # ---------------------------

    def match(self, *tipos):
        for tipo in tipos:
            if self.check(tipo):
                self.advance()
                return True
        return False

    def check(self, tipo):
        if self.is_at_end():
            return False
        return self.peek().tipo == tipo

    def advance(self):
        if not self.is_at_end():
            self.actual += 1
        return self.previous()

    def is_at_end(self):
        return self.peek().tipo == TipoToken.EOF

    def peek(self):
        return self.tokens[self.actual]

    def previous(self):
        return self.tokens[self.actual - 1]

    def error(self, mensaje):
        token = self.peek()
        raise ParseError(f"[Token: {token.lexema}] Error sintáctico: {mensaje}")
