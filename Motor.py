# --- Importaciones: módulos estándar y dependencias internas ---
import math
import time
import random
from TipoToken import TipoToken
from Environment import Environment

# --- Definición de funciones nativas (Las herramientas del lenguaje) ---
# Clase base para funciones que pueden ser llamadas desde el lenguaje interpretado.
class Callable:
    def arity(self): raise NotImplementedError
    def call(self, motor, arguments): raise NotImplementedError

# Cada clase "Native..." implementa una función disponible en el entorno global.
# Ej: sin(x), cos(x), sqrt(x), pow(x,y), rand(), clock()
class NativeSin(Callable):
    def arity(self): return 1
    def call(self, motor, arguments): return math.sin(arguments[0])

class NativeCos(Callable):
    def arity(self): return 1
    def call(self, motor, arguments): return math.cos(arguments[0])

class NativeSqrt(Callable):
    def arity(self): return 1
    def call(self, motor, arguments): return math.sqrt(arguments[0])

class NativePow(Callable):
    def arity(self): return 2
    def call(self, motor, arguments): return math.pow(arguments[0], arguments[1])

class NativeRand(Callable):
    def arity(self): return 0
    def call(self, motor, arguments): return random.random()

class NativeClock(Callable):
    def arity(self): return 0
    def call(self, motor, arguments): return time.time()

# --- La Clase Motor (El intérprete principal) ---
# Motor administra el Environment (variables/funciones) y provee
# métodos para interpretar sentencias y evaluar expresiones.
class Motor:
    def __init__(self):
        # El environment almacena variables y funciones disponibles.
        self.environment = Environment()
        
        # Cargar funciones nativas al iniciar el motor (disponibles globalmente)
        self.environment.define("clock", NativeClock())
        self.environment.define("sin", NativeSin())
        self.environment.define("cos", NativeCos())
        self.environment.define("sqrt", NativeSqrt())
        self.environment.define("pow", NativePow())
        self.environment.define("rand", NativeRand())

    # Punto de entrada para ejecutar una lista de sentencias (AST)
    def interpret(self, statements):
        """Punto de entrada para ejecutar una lista de sentencias"""
        if statements is None: return
        for statement in statements:
            self.execute(statement)

    def execute(self, stmt):
        stmt.accept(self)

    def evaluate(self, expr):
        return expr.accept(self)

    # --- Visitantes de Sentencias (manejadores para nodos de sentencia) ---
    # visit_expression_stmt: evalúa una expresión sin imprimirla
    def visit_expression_stmt(self, stmt):
        self.evaluate(stmt.expression)

    # visit_print_stmt: evalúa la expresión y la imprime en stdout
    def visit_print_stmt(self, stmt):
        valor = self.evaluate(stmt.expression)
        print(self.stringify(valor))

    # --- Visitantes de Expresiones (manejadores para nodos de expresión) ---
    # Literal: devuelve el valor directamente
    def visit_literal_expr(self, expr):
        return expr.valor

    # Agrupación: evalúa la expresión interna (paréntesis)
    def visit_agrupacion_expr(self, expr):
        return self.evaluate(expr.expresion)

    # Variable: obtiene el valor desde el environment
    def visit_variable_expr(self, expr):
        return self.environment.get(expr.nombre)

    # Asignación: evalúa y define/actualiza la variable en el environment
    def visit_asignacion_expr(self, expr):
        valor = self.evaluate(expr.valor)
        # Usamos .define() para que CREÉ la variable si no existe
        self.environment.define(expr.nombre.lexema, valor) 
        return valor

    # Unaria: maneja operadores como negación unaria
    def visit_unaria_expr(self, expr):
        derecha = self.evaluate(expr.derecha)
        if expr.operador.tipo == TipoToken.MINUS:
            return -float(derecha)
        return None

    # Binaria: suma, resta, multiplicación, división, módulo y comprobaciones de tipos
    def visit_binaria_expr(self, expr):
        izq = self.evaluate(expr.izquierda)
        der = self.evaluate(expr.derecha)
        op = expr.operador.tipo

        if op == TipoToken.PLUS:
            if isinstance(izq, (int, float)) and isinstance(der, (int, float)):
                return float(izq) + float(der)
            if isinstance(izq, str) and isinstance(der, str):
                return str(izq) + str(der)
            raise Exception("Operandos incompatibles para suma.")
        
        if op == TipoToken.MINUS: return float(izq) - float(der)
        if op == TipoToken.STAR: return float(izq) * float(der)
        if op == TipoToken.SLASH: 
            if der == 0: raise Exception("División por cero")
            return float(izq) / float(der)
        if op == TipoToken.MOD: return float(izq) % float(der)

        return None

    # Llamada: evalúa la función/objeto invocable y sus argumentos, luego la ejecuta
    def visit_llamada_expr(self, expr):
        callee = self.evaluate(expr.callee)
        argumentos = [self.evaluate(arg) for arg in expr.argumentos]

        if not isinstance(callee, Callable):
            raise Exception("Solo se pueden llamar funciones.")
        
        if len(argumentos) != callee.arity():
            raise Exception(f"Se esperaban {callee.arity()} argumentos.")
        
        return callee.call(self, argumentos)

    # stringify: formato de salida para valores (null, floats sin .0, etc.)
    def stringify(self, obj):
        if obj is None: return "null"
        if isinstance(obj, float):
            text = str(obj)
            return text[:-2] if text.endswith(".0") else text
        return str(obj)