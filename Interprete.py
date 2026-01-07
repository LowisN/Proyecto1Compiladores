#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intérprete con REPL (Read-Execute-Print-Loop) para el lenguaje estructurado.

Este programa implementa un intérprete interactivo que:
1. Lee una línea de entrada del usuario
2. Ejecuta el análisis léxico (Scanner)
3. Ejecuta el análisis sintáctico (Parser)
4. Muestra los resultados

Para salir: Ctrl+D (Linux/Mac) o Ctrl+Z seguido de Enter (Windows)
"""

import sys
from Scanner import Scanner
from Parser import Parser

class Interprete:
    """Clase principal del intérprete"""
    
    existen_errores = False
    
    @staticmethod
    def main():
        """Función principal que ejecuta el REPL"""
        print("Intérprete de Lenguaje Estructurado")
        print("=" * 40)
        print("Ingrese expresiones para analizar.")
        print("Para salir: Ctrl+D (Linux/Mac) o Ctrl+Z + Enter (Windows)")
        print("=" * 40)
        print()
        
        while True:
            try:
                # Mostrar el prompt
                linea = input(">>> ")
                
                # Si la línea está vacía, continuar
                if not linea.strip():
                    continue
                
                # Ejecutar la línea
                Interprete.ejecutar(linea)
                
                # Resetear el flag de errores
                Interprete.existen_errores = False
                
            except EOFError:
                # El usuario presionó Ctrl+D (o Ctrl+Z en Windows)
                print("\n\n¡Hasta luego!")
                break
            except KeyboardInterrupt:
                # El usuario presionó Ctrl+C
                print("\n\n¡Hasta luego!")
                break
    
    @staticmethod
    def ejecutar(source):
        """
        Ejecuta el análisis léxico y sintáctico de una cadena
        
        Args:
            source: str - Cadena de entrada a analizar
        """
        try:
            # Fase 1: Análisis Léxico (Scanner)
            print("\n--- ANÁLISIS LÉXICO ---")
            scanner = Scanner(source)
            tokens = scanner.scan()
            
            # Mostrar los tokens generados
            print("Tokens generados:")
            for token in tokens:
                print(f"  {token}")
            
            # Fase 2: Análisis Sintáctico (Parser)
            print("\n--- ANÁLISIS SINTÁCTICO ---")
            parser = Parser(tokens)
            parser.parse()
            
            print("Análisis sintáctico exitoso: La expresión es válida")
            print()
            
        except Exception as ex:
            # Mostrar el error
            print(f"\nERROR:")
            print(f"  {str(ex)}")
            print()
            Interprete.existen_errores = True
    
    @staticmethod
    def error(linea, mensaje):
        """
        Reporta un error
        
        Args:
            linea: int - Número de línea donde ocurrió el error
            mensaje: str - Mensaje de error
        """
        Interprete.reportar(linea, "", mensaje)
    
    @staticmethod
    def reportar(linea, posicion, mensaje):
        """
        Reporta un error con información detallada
        
        Args:
            linea: int - Número de línea donde ocurrió el error
            posicion: str - Posición adicional del error
            mensaje: str - Mensaje de error
        """
        print(f"[línea {linea}] Error {posicion}: {mensaje}", file=sys.stderr)
        Interprete.existen_errores = True


if __name__ == "__main__":
    Interprete.main()
