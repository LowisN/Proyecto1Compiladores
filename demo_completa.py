"""
Script de demostración completa del intérprete

Este script demuestra todas las funcionalidades implementadas.
"""

from Interprete import Interprete

def separador(titulo):
    """Imprime un separador con título"""
    print("\n" + "="*60)
    print(f"  {titulo}")
    print("="*60)

def ejecutar_y_mostrar(expresion):
    """Ejecuta una expresión y la muestra"""
    print(f">>> {expresion}")
    Interprete.ejecutar(expresion)

def main():
    print("\n" + "█"*60)
    print(" "*15 + "INTÉRPRETE CON ASA")
    print(" "*10 + "Demostración Completa de Funcionalidades")
    print("█"*60)
    
    # 1. Operaciones aritméticas
    separador("1. OPERACIONES ARITMÉTICAS")
    ejecutar_y_mostrar("5 + 3")
    ejecutar_y_mostrar("10 - 4")
    ejecutar_y_mostrar("6 * 7")
    ejecutar_y_mostrar("20 / 4")
    ejecutar_y_mostrar("17 % 5")
    
    # 2. Precedencia y agrupación
    separador("2. PRECEDENCIA Y AGRUPACIÓN")
    ejecutar_y_mostrar("2 + 3 * 4")
    ejecutar_y_mostrar("(2 + 3) * 4")
    ejecutar_y_mostrar("10 / 2 + 3")
    ejecutar_y_mostrar("10 / (2 + 3)")
    
    # 3. Operaciones unarias
    separador("3. OPERACIONES UNARIAS")
    ejecutar_y_mostrar("-5")
    ejecutar_y_mostrar("--10")
    ejecutar_y_mostrar("3 + -2")
    ejecutar_y_mostrar("-(5 + 3)")
    
    # 4. Variables
    separador("4. VARIABLES")
    ejecutar_y_mostrar("x = 10")
    ejecutar_y_mostrar("y = 20")
    ejecutar_y_mostrar("z = x + y")
    ejecutar_y_mostrar("z")
    ejecutar_y_mostrar("resultado = x * y / 2")
    ejecutar_y_mostrar("resultado")
    
    # 5. Funciones matemáticas
    separador("5. FUNCIONES MATEMÁTICAS")
    ejecutar_y_mostrar("sqrt(16)")
    ejecutar_y_mostrar("sqrt(2)")
    ejecutar_y_mostrar("pow(2, 3)")
    ejecutar_y_mostrar("pow(10, 2)")
    ejecutar_y_mostrar("pow(5, 0)")
    
    # 6. Funciones trigonométricas
    separador("6. FUNCIONES TRIGONOMÉTRICAS")
    ejecutar_y_mostrar("pi = 3.14159265359")
    ejecutar_y_mostrar("sin(0)")
    ejecutar_y_mostrar("cos(0)")
    ejecutar_y_mostrar("sin(pi / 2)")
    ejecutar_y_mostrar("cos(pi)")
    
    # 7. Función aleatoria
    separador("7. GENERACIÓN DE NÚMEROS ALEATORIOS")
    ejecutar_y_mostrar("rand()")
    ejecutar_y_mostrar("rand()")
    ejecutar_y_mostrar("aleatorio = rand() * 100")
    ejecutar_y_mostrar("aleatorio")
    
    # 8. Expresiones complejas
    separador("8. EXPRESIONES COMPLEJAS")
    ejecutar_y_mostrar("a = 3")
    ejecutar_y_mostrar("b = 4")
    ejecutar_y_mostrar("hipotenusa = sqrt(pow(a, 2) + pow(b, 2))")
    ejecutar_y_mostrar("hipotenusa")
    
    # 9. Punto y coma (sin impresión)
    separador("9. CONTROL DE IMPRESIÓN (;)")
    ejecutar_y_mostrar("valor1 = 100;")  # No imprime
    ejecutar_y_mostrar("valor2 = 200;")  # No imprime
    ejecutar_y_mostrar("suma = valor1 + valor2")  # Imprime
    
    # 10. Ejemplos prácticos
    separador("10. EJEMPLOS PRÁCTICOS")
    print("\n# Cálculo del área de un círculo")
    ejecutar_y_mostrar("radio = 5")
    ejecutar_y_mostrar("area = pi * pow(radio, 2)")
    ejecutar_y_mostrar("area")
    
    print("\n# Conversión de grados a radianes y cálculo de seno")
    ejecutar_y_mostrar("grados = 45")
    ejecutar_y_mostrar("radianes = grados * pi / 180")
    ejecutar_y_mostrar("seno45 = sin(radianes)")
    ejecutar_y_mostrar("seno45")
    
    print("\n# Promedio de tres números")
    ejecutar_y_mostrar("num1 = 10")
    ejecutar_y_mostrar("num2 = 20")
    ejecutar_y_mostrar("num3 = 30")
    ejecutar_y_mostrar("promedio = (num1 + num2 + num3) / 3")
    ejecutar_y_mostrar("promedio")
    
    # 11. Errores semánticos
    separador("11. DETECCIÓN DE ERRORES SEMÁNTICOS")
    print("\n# Error: Número incorrecto de argumentos")
    ejecutar_y_mostrar("sin(1, 2, 3)")
    
    print("\n# Error: Tipo de argumento incorrecto")
    ejecutar_y_mostrar('sin("Hola")')
    
    print("\n# Error: Incompatibilidad de operandos")
    ejecutar_y_mostrar('5 + "texto"')
    
    print("\n# Error: Función no definida")
    ejecutar_y_mostrar("imprimir(10)")
    
    print("\n# Error: Variable no definida")
    ejecutar_y_mostrar("variable_inexistente")
    
    print("\n# Error: División por cero")
    ejecutar_y_mostrar("10 / 0")
    
    print("\n# Error: Llamar número como función")
    ejecutar_y_mostrar("5(10, 20)")
    
    # Resumen final
    print("\n" + "█"*60)
    print(" "*15 + "FIN DE LA DEMOSTRACIÓN")
    print("█"*60)
    print("\n✅ Todas las funcionalidades han sido demostradas correctamente")
    print("✅ El intérprete está listo para usarse en modo REPL")
    print("\nPara iniciar el REPL interactivo, ejecuta:")
    print("    python Interprete.py")
    print("\n" + "█"*60 + "\n")

if __name__ == "__main__":
    main()
