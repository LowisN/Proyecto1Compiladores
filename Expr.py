from abc import ABC, abstractmethod
from Token import Token

# Módulo: Definición de nodos de expresión del Árbol Sintáctico Abstracto (ASA/AST)
# Cada clase representa un tipo de expresión y implementa accept(visitor)
class Expr(ABC):
    """Clase base abstracta para todas las expresiones del ASA"""
    @abstractmethod
    def accept(self, visitor):
        pass

class Binaria(Expr):
    """Nodo para operaciones binarias: +, -, *, /, %.
    izquierda, operador (Token), derecha."""
    def __init__(self, izquierda: Expr, operador: Token, derecha: Expr):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha

    def accept(self, visitor):
        return visitor.visit_binaria_expr(self)

class Unaria(Expr):
    """Nodo para operaciones unarias (ej. -x). operador: Token, derecha: Expr"""
    def __init__(self, operador: Token, derecha: Expr):
        self.operador = operador
        self.derecha = derecha

    def accept(self, visitor):
        return visitor.visit_unaria_expr(self)

class Literal(Expr):
    """Nodo para valores literales: números, strings, booleanos, null"""
    def __init__(self, valor):
        self.valor = valor

    def accept(self, visitor):
        return visitor.visit_literal_expr(self)

class Agrupacion(Expr):
    """Nodo para expresiones agrupadas con paréntesis: ( expresion )"""
    def __init__(self, expresion: Expr):
        self.expresion = expresion

    def accept(self, visitor):
        return visitor.visit_agrupacion_expr(self)

class Variable(Expr):
    """Nodo para acceso a una variable por su Token identificador"""
    def __init__(self, nombre: Token):
        self.nombre = nombre

    def accept(self, visitor):
        return visitor.visit_variable_expr(self)

class Asignacion(Expr):
    """Nodo para asignación: nombre = valor.
    nombre: Token (identificador), valor: Expr"""
    def __init__(self, nombre: Token, valor: Expr):
        self.nombre = nombre
        self.valor = valor

    def accept(self, visitor):
        return visitor.visit_asignacion_expr(self)

class Llamada(Expr):
    """Nodo para llamadas a funciones:
    callee: expresión que referencia la función (p. ej. identificador),
    paren: Token del paréntesis para reportar errores,
    argumentos: lista de expresiones."""
    def __init__(self, callee: Expr, paren: Token, argumentos: list):
        self.callee = callee      # La referencia a la función (ej. el identificador "sin")
        self.paren = paren        # El token ')' o '(', útil para reportar errores de línea
        self.argumentos = argumentos # Lista de expresiones

    def accept(self, visitor):
        return visitor.visit_llamada_expr(self)