"""
Evaluador del Árbol de Sintaxis Abstracta (ASA)

Este módulo implementa el patrón Visitor para recorrer y evaluar el ASA.
Ejecuta las operaciones representadas en el ASA y maneja errores semánticos.
"""

import math
import random
from TipoToken import TipoToken
from ASA import *


class ErrorSemantico(Exception):
    """Excepción para errores semánticos durante la evaluación"""
    pass


class FuncionBuiltIn:
    """Clase base para funciones built-in del lenguaje"""
    
    def __init__(self, nombre, aridad):
        """
        Constructor
        
        Args:
            nombre: str - Nombre de la función
            aridad: int - Número de argumentos que acepta
        """
        self.nombre = nombre
        self.aridad = aridad
    
    def llamar(self, evaluador, argumentos):
        """
        Ejecuta la función
        
        Args:
            evaluador: Evaluador - Evaluador que realiza la llamada
            argumentos: list - Lista de argumentos evaluados
            
        Returns:
            object: Resultado de la función
        """
        raise NotImplementedError()


class FuncionRand(FuncionBuiltIn):
    """Función rand() - genera número aleatorio entre 0 y 1"""
    
    def __init__(self):
        super().__init__("rand", 0)
    
    def llamar(self, evaluador, argumentos):
        return random.random()


class FuncionSin(FuncionBuiltIn):
    """Función sin(angulo) - seno en radianes"""
    
    def __init__(self):
        super().__init__("sin", 1)
    
    def llamar(self, evaluador, argumentos):
        angulo = argumentos[0]
        if not isinstance(angulo, (int, float)):
            raise ErrorSemantico(f"sin() requiere un argumento numérico, se recibió: {type(angulo).__name__}")
        return math.sin(angulo)


class FuncionCos(FuncionBuiltIn):
    """Función cos(angulo) - coseno en radianes"""
    
    def __init__(self):
        super().__init__("cos", 1)
    
    def llamar(self, evaluador, argumentos):
        angulo = argumentos[0]
        if not isinstance(angulo, (int, float)):
            raise ErrorSemantico(f"cos() requiere un argumento numérico, se recibió: {type(angulo).__name__}")
        return math.cos(angulo)


class FuncionSqrt(FuncionBuiltIn):
    """Función sqrt(valor) - raíz cuadrada"""
    
    def __init__(self):
        super().__init__("sqrt", 1)
    
    def llamar(self, evaluador, argumentos):
        valor = argumentos[0]
        if not isinstance(valor, (int, float)):
            raise ErrorSemantico(f"sqrt() requiere un argumento numérico, se recibió: {type(valor).__name__}")
        if valor < 0:
            raise ErrorSemantico(f"sqrt() no puede calcular la raíz cuadrada de un número negativo: {valor}")
        return math.sqrt(valor)


class FuncionPow(FuncionBuiltIn):
    """Función pow(base, exponente) - potencia"""
    
    def __init__(self):
        super().__init__("pow", 2)
    
    def llamar(self, evaluador, argumentos):
        base = argumentos[0]
        exponente = argumentos[1]
        if not isinstance(base, (int, float)):
            raise ErrorSemantico(f"pow() requiere argumentos numéricos, el primer argumento es: {type(base).__name__}")
        if not isinstance(exponente, (int, float)):
            raise ErrorSemantico(f"pow() requiere argumentos numéricos, el segundo argumento es: {type(exponente).__name__}")
        return math.pow(base, exponente)


class Evaluador:
    """
    Evaluador del ASA usando el patrón Visitor.
    Recorre el árbol y ejecuta las operaciones.
    """
    
    def __init__(self):
        """Constructor - inicializa la tabla de símbolos"""
        self.entorno = {}  # Tabla de símbolos para variables
        self.funciones = {  # Tabla de símbolos para funciones
            "rand": FuncionRand(),
            "sin": FuncionSin(),
            "cos": FuncionCos(),
            "sqrt": FuncionSqrt(),
            "pow": FuncionPow()
        }
    
    def evaluar(self, nodo):
        """
        Evalúa un nodo del ASA
        
        Args:
            nodo: Nodo - Nodo del ASA a evaluar
            
        Returns:
            object: Resultado de la evaluación
        """
        return nodo.accept(self)
    
    def visit_sentencia(self, sentencia):
        """
        Visita un nodo Sentencia
        
        Args:
            sentencia: Sentencia - Nodo de sentencia
            
        Returns:
            tuple: (valor, debe_imprimir) donde debe_imprimir es False si hay ';'
        """
        valor = self.evaluar(sentencia.expresion)
        debe_imprimir = not sentencia.tiene_semicolon
        return (valor, debe_imprimir)
    
    def visit_literal(self, literal):
        """
        Visita un nodo Literal
        
        Args:
            literal: Literal - Nodo literal
            
        Returns:
            object: El valor del literal
        """
        return literal.valor
    
    def visit_binaria(self, binaria):
        """
        Visita un nodo Binaria (operación binaria)
        
        Args:
            binaria: Binaria - Nodo de operación binaria
            
        Returns:
            object: Resultado de la operación
            
        Raises:
            ErrorSemantico: Si hay incompatibilidad de tipos
        """
        izquierda = self.evaluar(binaria.izquierda)
        derecha = self.evaluar(binaria.derecha)
        operador = binaria.operador.tipo
        
        # Operaciones aritméticas
        if operador == TipoToken.PLUS:
            if isinstance(izquierda, (int, float)) and isinstance(derecha, (int, float)):
                return izquierda + derecha
            elif isinstance(izquierda, str) and isinstance(derecha, str):
                return izquierda + derecha
            else:
                raise ErrorSemantico(
                    f"Incompatibilidad de operandos para '+': "
                    f"{type(izquierda).__name__} y {type(derecha).__name__}"
                )
        
        elif operador == TipoToken.MINUS:
            if isinstance(izquierda, (int, float)) and isinstance(derecha, (int, float)):
                return izquierda - derecha
            else:
                raise ErrorSemantico(
                    f"Incompatibilidad de operandos para '-': "
                    f"{type(izquierda).__name__} y {type(derecha).__name__}"
                )
        
        elif operador == TipoToken.STAR:
            if isinstance(izquierda, (int, float)) and isinstance(derecha, (int, float)):
                return izquierda * derecha
            else:
                raise ErrorSemantico(
                    f"Incompatibilidad de operandos para '*': "
                    f"{type(izquierda).__name__} y {type(derecha).__name__}"
                )
        
        elif operador == TipoToken.SLASH:
            if isinstance(izquierda, (int, float)) and isinstance(derecha, (int, float)):
                if derecha == 0:
                    raise ErrorSemantico("División por cero")
                return izquierda / derecha
            else:
                raise ErrorSemantico(
                    f"Incompatibilidad de operandos para '/': "
                    f"{type(izquierda).__name__} y {type(derecha).__name__}"
                )
        
        elif operador == TipoToken.MOD:
            if isinstance(izquierda, (int, float)) and isinstance(derecha, (int, float)):
                if derecha == 0:
                    raise ErrorSemantico("Módulo por cero")
                return izquierda % derecha
            else:
                raise ErrorSemantico(
                    f"Incompatibilidad de operandos para '%': "
                    f"{type(izquierda).__name__} y {type(derecha).__name__}"
                )
        
        return None
    
    def visit_unaria(self, unaria):
        """
        Visita un nodo Unaria (operación unaria)
        
        Args:
            unaria: Unaria - Nodo de operación unaria
            
        Returns:
            object: Resultado de la operación
            
        Raises:
            ErrorSemantico: Si el operando no es numérico
        """
        expresion = self.evaluar(unaria.expresion)
        operador = unaria.operador.tipo
        
        if operador == TipoToken.MINUS:
            if isinstance(expresion, (int, float)):
                return -expresion
            else:
                raise ErrorSemantico(
                    f"El operador unario '-' requiere un operando numérico, "
                    f"se recibió: {type(expresion).__name__}"
                )
        
        return None
    
    def visit_agrupacion(self, agrupacion):
        """
        Visita un nodo Agrupacion (expresión entre paréntesis)
        
        Args:
            agrupacion: Agrupacion - Nodo de agrupación
            
        Returns:
            object: Resultado de evaluar la expresión interna
        """
        return self.evaluar(agrupacion.expresion)
    
    def visit_variable(self, variable):
        """
        Visita un nodo Variable (lectura de variable)
        
        Args:
            variable: Variable - Nodo de variable
            
        Returns:
            object: Valor de la variable
            
        Raises:
            ErrorSemantico: Si la variable no está definida
        """
        nombre = variable.nombre.lexema
        if nombre in self.entorno:
            return self.entorno[nombre]
        else:
            raise ErrorSemantico(f"Variable no definida: '{nombre}'")
    
    def visit_asignacion(self, asignacion):
        """
        Visita un nodo Asignacion (asignación de variable)
        
        Args:
            asignacion: Asignacion - Nodo de asignación
            
        Returns:
            object: Valor asignado
        """
        valor = self.evaluar(asignacion.valor)
        nombre = asignacion.nombre.lexema
        self.entorno[nombre] = valor
        return valor
    
    def visit_llamada(self, llamada):
        """
        Visita un nodo Llamada (llamada a función)
        
        Args:
            llamada: Llamada - Nodo de llamada
            
        Returns:
            object: Resultado de la función
            
        Raises:
            ErrorSemantico: Si hay errores en la llamada
        """
        # Verificar que callee sea una variable
        if not isinstance(llamada.callee, Variable):
            # Si no es una variable, evaluar y verificar si es un número u otro literal
            callee_valor = self.evaluar(llamada.callee)
            if isinstance(callee_valor, (int, float)):
                raise ErrorSemantico(
                    f"No se puede llamar a '{callee_valor}' como función. "
                    f"'{callee_valor}' es un número, no una función"
                )
            else:
                raise ErrorSemantico(
                    f"Solo se pueden llamar funciones, no valores de tipo {type(callee_valor).__name__}"
                )
        
        # Obtener el nombre de la función
        nombre_funcion = llamada.callee.nombre.lexema
        
        # Verificar que la función exista
        if nombre_funcion not in self.funciones:
            raise ErrorSemantico(f"Función no definida: '{nombre_funcion}'")
        
        funcion = self.funciones[nombre_funcion]
        
        # Evaluar los argumentos
        argumentos = []
        for arg in llamada.argumentos:
            argumentos.append(self.evaluar(arg))
        
        # Verificar la aridad
        if len(argumentos) != funcion.aridad:
            raise ErrorSemantico(
                f"La función '{nombre_funcion}' espera {funcion.aridad} argumento(s), "
                f"pero se recibieron {len(argumentos)}"
            )
        
        # Llamar a la función
        try:
            return funcion.llamar(self, argumentos)
        except ErrorSemantico:
            raise
        except Exception as e:
            raise ErrorSemantico(f"Error al ejecutar '{nombre_funcion}': {str(e)}")
