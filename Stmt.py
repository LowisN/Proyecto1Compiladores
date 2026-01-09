# Módulo: Definición de nodos de sentencia del Árbol Sintáctico (ASA/AST)
from abc import ABC, abstractmethod

class Stmt(ABC):
    """Clase base abstracta para todas las sentencias."""
    @abstractmethod
    def accept(self, visitor):
        pass

class Expression(Stmt):
    """Sentencia que termina en ';' (no imprime en REPL).
    Contiene una expresión cuyo resultado se evalúa pero no se muestra."""
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        # Llama al visitante correspondiente en el intérprete/motor
        return visitor.visit_expression_stmt(self)

class Print(Stmt):
    """Sentencia sin ';' (implicita en REPL): evalúa la expresión y la imprime."""
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        # Llama al visitante que gestiona la impresión en el intérprete/motor
        return visitor.visit_print_stmt(self)