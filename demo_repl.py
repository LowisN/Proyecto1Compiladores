"""
Script de prueba rápida para verificar el REPL sin interacción

Este script simula el uso del intérprete ejecutando varias expresiones.
"""

from Interprete import Interprete

def probar_repl():
    """Prueba el intérprete con varias expresiones"""
    
    expresiones = [
        # Operaciones básicas
        "5 + 3",
        "10 * 2",
        "(4 + 6) / 2",
        
        # Variables
        "x = 10",
        "y = x * 2",
        "x + y",
        
        # Funciones
        "sqrt(16)",
        "pow(2, 8)",
        "sin(3.14159 / 2)",
        
        # Con punto y coma (no imprime)
        "z = 100;",
        "z",
        
        # Expresión compleja
        "resultado = sqrt(pow(3, 2) + pow(4, 2))",
        "resultado",
    ]
    
    print("="*60)
    print("DEMOSTRACIÓN DEL INTÉRPRETE")
    print("="*60)
    
    for expr in expresiones:
        print(f"\n>>> {expr}")
        Interprete.ejecutar(expr)

if __name__ == "__main__":
    probar_repl()
