# Módulo: Gestión de entorno de ejecución (almacena variables y funciones)
class Environment:
    # Clase que mantiene un diccionario de valores (variables/funciones)
    def __init__(self):
        # values: mapa nombre -> valor
        self.values = {}

    def define(self, nombre: str, valor):
        """Define una nueva variable o actualiza una existente"""
        # Inserta o actualiza el valor en el entorno global/local actual
        self.values[nombre] = valor

    def get(self, nombre):
        """Obtiene el valor de una variable. Lanza error si no existe."""
        # nombre es un Token: usamos nombre.lexema para la clave
        if nombre.lexema in self.values:
            return self.values[nombre.lexema]
        
        # Si no existe, se informa el error al intérprete
        raise Exception(f"Variable no definida: '{nombre.lexema}'.")

    def assign(self, nombre, valor):
        """Asigna valor a una variable existente."""
        # Actualiza solo si la variable ya fue definida previamente
        if nombre.lexema in self.values:
            self.values[nombre.lexema] = valor
            return
        
        # Si no existe la variable, se lanza error (no crea implícitamente)
        raise Exception(f"Variable no definida: '{nombre.lexema}'.")