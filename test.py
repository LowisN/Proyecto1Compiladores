#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de pruebas para el Scanner y Parser
"""

from Scanner import Scanner
from Parser import Parser

def test_expresion(expresion, descripcion):
    """Prueba una expresión y muestra el resultado"""
    print(f"\n{'='*60}")
    print(f"Prueba: {descripcion}")
    print(f"Expresión: {expresion}")
    print(f"{'='*60}")
    
    try:
        # Scanner
        print("\n--- ANÁLISIS LÉXICO ---")
        scanner = Scanner(expresion)
        tokens = scanner.scan()
        
        print("Tokens generados:")
        for token in tokens:
            print(f"  {token}")
        
        # Parser
        print("\n--- ANÁLISIS SINTÁCTICO ---")
        parser = Parser(tokens)
        parser.parse()
        
        print("✓ Análisis sintáctico exitoso: La expresión es válida")
        return True
        
    except Exception as e:
        print(f"\n✗ ERROR:")
        print(f"  {str(e)}")
        return False

def main():
    """Ejecuta las pruebas"""
    print("\n" + "="*60)
    print("PRUEBAS DEL SCANNER Y PARSER")
    print("="*60)
    
    pruebas = [
        # Expresiones aritméticas básicas
        ("2 + 3", "Suma simple"),
        ("5 - 2", "Resta simple"),
        ("4 * 3", "Multiplicación simple"),
        ("10 / 2", "División simple"),
        ("10 % 3", "Módulo simple"),
        
        # Expresiones con paréntesis
        ("(2 + 3) * 4", "Paréntesis y precedencia"),
        ("((1 + 2) * (3 + 4))", "Paréntesis anidados"),
        
        # Expresiones complejas
        ("2 + 3 * 4 - 5 / 2", "Expresión aritmética compleja"),
        ("-5 + 3", "Unario negativo"),
        ("+10 - 5", "Unario positivo"),
        
        # Asignaciones
        ("x = 10", "Asignación simple"),
        ("y = 2 + 3", "Asignación con expresión"),
        ("z = x + y", "Asignación con variables"),
        
        # Cadenas
        ('"Hola Mundo"', "Cadena de texto"),
        ('mensaje = "Hola"', "Asignación de cadena"),
        
        # Comparaciones
        ("x == 5", "Comparación igualdad"),
        ("a == b", "Comparación entre variables"),
        
        # Null
        ("valor = null", "Asignación de null"),
        ("null", "Literal null"),
        
        # Llamadas a funciones
        ("suma(5, 10)", "Llamada a función con argumentos"),
        ("funcion()", "Llamada a función sin argumentos"),
        ("calcular(x, y, z)", "Función con múltiples argumentos"),
        ("f(1 + 2, 3 * 4)", "Función con expresiones como argumentos"),
        
        # Números decimales
        ("3.14", "Número decimal"),
        ("2.5 + 3.7", "Operación con decimales"),
        
        # Identificadores
        ("variable", "Identificador simple"),
        ("mi_variable", "Identificador con guión bajo"),
        ("variable123", "Identificador con números"),
    ]
    
    exitosos = 0
    fallidos = 0
    
    for expresion, descripcion in pruebas:
        if test_expresion(expresion, descripcion):
            exitosos += 1
        else:
            fallidos += 1
    
    # Pruebas de errores (deben fallar)
    print("\n\n" + "="*60)
    print("PRUEBAS DE ERRORES (DEBEN FALLAR)")
    print("="*60)
    
    pruebas_error = [
        ("@#$", "Caracteres inválidos"),
        ("2 + + 3", "Operador doble inválido"),
        ('"texto sin cerrar', "Cadena sin cerrar"),
        ("(2 + 3", "Paréntesis sin cerrar"),
        (")", "Paréntesis de cierre sin apertura"),
        ("2 + ", "Expresión incompleta"),
    ]
    
    errores_detectados = 0
    
    for expresion, descripcion in pruebas_error:
        resultado = test_expresion(expresion, descripcion)
        if not resultado:
            errores_detectados += 1
    
    # Resumen
    print("\n\n" + "="*60)
    print("RESUMEN DE PRUEBAS")
    print("="*60)
    print(f"Pruebas válidas exitosas: {exitosos}/{len(pruebas)}")
    print(f"Pruebas válidas fallidas: {fallidos}/{len(pruebas)}")
    print(f"Errores detectados correctamente: {errores_detectados}/{len(pruebas_error)}")
    print("="*60)

if __name__ == "__main__":
    main()
