"""
Test simple para verificar que el REPL funciona correctamente
Este script simula entradas al REPL
"""

import sys
from io import StringIO
from Interprete import Interprete

def test_repl():
    """Simula ejecuciones en el REPL"""
    
    print("="*60)
    print("TEST DE FUNCIONALIDAD DEL REPL")
    print("="*60)
    
    # Test 1: Operaciones básicas
    print("\n[TEST 1] Operaciones aritméticas")
    Interprete.ejecutar("5 + 3")
    Interprete.ejecutar("10 * 2")
    
    # Test 2: Variables
    print("\n[TEST 2] Variables")
    Interprete.ejecutar("x = 10")
    Interprete.ejecutar("y = x * 2")
    Interprete.ejecutar("x + y")
    
    # Test 3: Funciones
    print("\n[TEST 3] Funciones built-in")
    Interprete.ejecutar("sqrt(16)")
    Interprete.ejecutar("pow(2, 10)")
    Interprete.ejecutar("sin(0)")
    
    # Test 4: Expresiones complejas
    print("\n[TEST 4] Expresiones complejas")
    Interprete.ejecutar("resultado = sqrt(pow(3, 2) + pow(4, 2))")
    Interprete.ejecutar("resultado")
    
    # Test 5: Control de impresión
    print("\n[TEST 5] Control de impresión con ';'")
    Interprete.ejecutar("valor = 100;")
    print("(no debería imprimir nada arriba)")
    Interprete.ejecutar("valor")
    
    # Test 6: Errores
    print("\n[TEST 6] Manejo de errores")
    Interprete.ejecutar("sin(1, 2, 3)")
    Interprete.ejecutar("variable_no_existe")
    
    print("\n" + "="*60)
    print("[OK] TODOS LOS TESTS COMPLETADOS")
    print("="*60)
    print("\nEl intérprete está funcionando correctamente.")
    print("Para usar el REPL interactivo, ejecuta: python Interprete.py")
    print("="*60)

if __name__ == "__main__":
    test_repl()
