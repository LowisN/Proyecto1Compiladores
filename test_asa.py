"""
Script de prueba para el intérprete con ASA

Prueba todas las funcionalidades implementadas:
- Operaciones aritméticas
- Operaciones unarias
- Variables
- Asignación
- Funciones built-in
- Manejo de errores semánticos
"""

import sys
from Scanner import Scanner
from Parser import Parser
from Evaluador import Evaluador, ErrorSemantico

def probar_expresion(expresion, descripcion):
    """Prueba una expresión y muestra el resultado"""
    print(f"\n{'='*60}")
    print(f"Prueba: {descripcion}")
    print(f"Expresión: {expresion}")
    print(f"{'-'*60}")
    
    try:
        # Análisis léxico
        scanner = Scanner(expresion)
        tokens = scanner.scan()
        
        # Análisis sintáctico
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Evaluación
        evaluador = Evaluador()
        resultado, debe_imprimir = evaluador.evaluar(ast)
        
        if debe_imprimir:
            print(f"✓ Resultado: {resultado}")
        else:
            print(f"✓ Ejecutado (sin impresión)")
            
    except ErrorSemantico as e:
        print(f"✗ ERROR SEMÁNTICO: {e}")
    except Exception as e:
        print(f"✗ ERROR: {e}")

def main():
    """Ejecuta todas las pruebas"""
    print("="*60)
    print("PRUEBAS DEL INTÉRPRETE CON ASA")
    print("="*60)
    
    # Pruebas de operaciones aritméticas
    probar_expresion("5 + 3", "Suma básica")
    probar_expresion("10 - 4", "Resta básica")
    probar_expresion("6 * 7", "Multiplicación básica")
    probar_expresion("20 / 4", "División básica")
    probar_expresion("17 % 5", "Módulo básico")
    probar_expresion("2 + 3 * 4", "Precedencia de operadores")
    probar_expresion("(2 + 3) * 4", "Agrupación con paréntesis")
    
    # Pruebas de operación unaria
    probar_expresion("-5", "Negación unaria")
    probar_expresion("--10", "Doble negación")
    probar_expresion("3 + -2", "Suma con negativo")
    
    # Pruebas de variables
    evaluador_compartido = Evaluador()
    
    print(f"\n{'='*60}")
    print("Pruebas con variables (usando evaluador compartido)")
    print(f"{'='*60}")
    
    expresiones_variables = [
        ("x = 10", "Asignación simple"),
        ("x", "Lectura de variable"),
        ("y = x * 2", "Asignación usando variable"),
        ("y", "Lectura de y"),
        ("z = x + y", "Operación con variables"),
        ("z", "Lectura de z"),
    ]
    
    for expr, desc in expresiones_variables:
        print(f"\n{'-'*60}")
        print(f"Prueba: {desc}")
        print(f"Expresión: {expr}")
        print(f"{'-'*60}")
        try:
            scanner = Scanner(expr)
            tokens = scanner.scan()
            parser = Parser(tokens)
            ast = parser.parse()
            resultado, debe_imprimir = evaluador_compartido.evaluar(ast)
            if debe_imprimir:
                print(f"✓ Resultado: {resultado}")
            else:
                print(f"✓ Ejecutado (sin impresión)")
        except Exception as e:
            print(f"✗ ERROR: {e}")
    
    # Pruebas con punto y coma
    probar_expresion("5 + 3;", "Expresión con ';' (no imprime)")
    probar_expresion("5 + 3", "Expresión sin ';' (imprime)")
    
    # Pruebas de funciones built-in
    probar_expresion("rand()", "Función rand()")
    probar_expresion("sin(0)", "Función sin(0)")
    probar_expresion("cos(0)", "Función cos(0)")
    probar_expresion("sqrt(16)", "Función sqrt(16)")
    probar_expresion("pow(2, 3)", "Función pow(2, 3)")
    probar_expresion("sqrt(25) + pow(3, 2)", "Combinación de funciones")
    
    # Pruebas de errores semánticos
    print(f"\n{'='*60}")
    print("PRUEBAS DE ERRORES SEMÁNTICOS")
    print(f"{'='*60}")
    
    probar_expresion("sin(1, 2, 3)", "Función con argumentos incorrectos")
    probar_expresion('sin("Hola")', "Función con tipo incorrecto")
    probar_expresion('5 + "Hola"', "Incompatibilidad de operandos")
    probar_expresion("5 + a = 3", "Asignación a expresión no válida")
    probar_expresion("imprimir(4)", "Función no definida")
    probar_expresion("4(5, 2)", "Llamar número como función")
    probar_expresion("w", "Variable no definida")
    probar_expresion("10 / 0", "División por cero")
    
    print(f"\n{'='*60}")
    print("PRUEBAS COMPLETADAS")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
