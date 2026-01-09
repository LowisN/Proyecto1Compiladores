"""
Clases para el Árbol de Sintaxis Abstracta (ASA)

Este módulo define las clases que representan los nodos del ASA.
Cada tipo de expresión/sentencia tiene su propia clase.
"""

from abc import ABC, abstractmethod

class Nodo(ABC):
    """Clase base abstracta para todos los nodos del ASA"""
    
    @abstractmethod
    def accept(self, visitor):
        """
        Método de patrón Visitor para recorrer el ASA
        
        Args:
            visitor: Visitor - Objeto visitante que ejecutará la operación
            
        Returns:
            object: Resultado de la visita
        """
        pass


class Literal(Nodo):
    """Nodo para valores literales (números, strings, null)"""
    
    def __init__(self, valor):
        """
        Constructor
        
        Args:
            valor: object - El valor literal (número, string o None)
        """
        self.valor = valor
    
    def accept(self, visitor):
        return visitor.visit_literal(self)


class Binaria(Nodo):
    """Nodo para operaciones binarias (+, -, *, /, %)"""
    
    def __init__(self, izquierda, operador, derecha):
        """
        Constructor
        
        Args:
            izquierda: Nodo - Expresión del lado izquierdo
            operador: Token - Token del operador
            derecha: Nodo - Expresión del lado derecho
        """
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha
    
    def accept(self, visitor):
        return visitor.visit_binaria(self)


class Unaria(Nodo):
    """Nodo para operaciones unarias (-)"""
    
    def __init__(self, operador, expresion):
        """
        Constructor
        
        Args:
            operador: Token - Token del operador
            expresion: Nodo - Expresión a la que se aplica el operador
        """
        self.operador = operador
        self.expresion = expresion
    
    def accept(self, visitor):
        return visitor.visit_unaria(self)


class Agrupacion(Nodo):
    """Nodo para expresiones agrupadas con paréntesis"""
    
    def __init__(self, expresion):
        """
        Constructor
        
        Args:
            expresion: Nodo - Expresión dentro del paréntesis
        """
        self.expresion = expresion
    
    def accept(self, visitor):
        return visitor.visit_agrupacion(self)


class Variable(Nodo):
    """Nodo para acceso a variables"""
    
    def __init__(self, nombre):
        """
        Constructor
        
        Args:
            nombre: Token - Token con el nombre de la variable
        """
        self.nombre = nombre
    
    def accept(self, visitor):
        return visitor.visit_variable(self)


class Asignacion(Nodo):
    """Nodo para asignación de variables"""
    
    def __init__(self, nombre, valor):
        """
        Constructor
        
        Args:
            nombre: Token - Token con el nombre de la variable
            valor: Nodo - Expresión del valor a asignar
        """
        self.nombre = nombre
        self.valor = valor
    
    def accept(self, visitor):
        return visitor.visit_asignacion(self)


class Llamada(Nodo):
    """Nodo para llamada a funciones"""
    
    def __init__(self, callee, parentesis, argumentos):
        """
        Constructor
        
        Args:
            callee: Nodo - Expresión que se evalúa a la función
            parentesis: Token - Token del paréntesis de cierre (para errores)
            argumentos: list - Lista de expresiones (argumentos)
        """
        self.callee = callee
        self.parentesis = parentesis
        self.argumentos = argumentos
    
    def accept(self, visitor):
        return visitor.visit_llamada(self)


class Sentencia(Nodo):
    """Nodo para una sentencia (expresión con o sin punto y coma)"""
    
    def __init__(self, expresion, tiene_semicolon):
        """
        Constructor
        
        Args:
            expresion: Nodo - Expresión de la sentencia
            tiene_semicolon: bool - True si la sentencia termina con ';'
        """
        self.expresion = expresion
        self.tiene_semicolon = tiene_semicolon
    
    def accept(self, visitor):
        return visitor.visit_sentencia(self)
