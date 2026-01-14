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
        pass


class Literal(Nodo):
    """Nodo para valores literales (números, strings, null)"""
    
    def __init__(self, valor):
        self.valor = valor
    
    def accept(self, visitor):
        return visitor.visit_literal(self)


class Binaria(Nodo):
    """Nodo para operaciones binarias (+, -, *, /, %)"""
    
    def __init__(self, izquierda, operador, derecha):
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha
    
    def accept(self, visitor):
        return visitor.visit_binaria(self)


class Unaria(Nodo):
    """Nodo para operaciones unarias (-)"""
    
    def __init__(self, operador, expresion):
        self.operador = operador
        self.expresion = expresion
    
    def accept(self, visitor):
        return visitor.visit_unaria(self)


class Agrupacion(Nodo):
    """Nodo para expresiones agrupadas con paréntesis"""
    
    def __init__(self, expresion):
        self.expresion = expresion
    
    def accept(self, visitor):
        return visitor.visit_agrupacion(self)


class Variable(Nodo):
    """Nodo para acceso a variables"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def accept(self, visitor):
        return visitor.visit_variable(self)


class Asignacion(Nodo):
    """Nodo para asignación de variables"""
    
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
    
    def accept(self, visitor):
        return visitor.visit_asignacion(self)


class Llamada(Nodo):
    """Nodo para llamada a funciones"""
    
    def __init__(self, callee, parentesis, argumentos):
        self.callee = callee
        self.parentesis = parentesis
        self.argumentos = argumentos
    
    def accept(self, visitor):
        return visitor.visit_llamada(self)


class Sentencia(Nodo):
    """Nodo para una sentencia (expresión con o sin punto y coma)"""
    
    def __init__(self, expresion, tiene_semicolon):
        self.expresion = expresion
        self.tiene_semicolon = tiene_semicolon
    
    def accept(self, visitor):
        return visitor.visit_sentencia(self)
