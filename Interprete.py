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
from Evaluador import Evaluador, ErrorSemantico

class Interprete:
    """Clase principal del intérprete"""
    
    existen_errores = False
    evaluador = Evaluador()  # Evaluador compartido para mantener el entorno
    
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
        Ejecuta el análisis léxico, sintáctico y semántico de una cadena
        
        Args:
            source: str - Cadena de entrada a analizar
        """
        try:
            # Fase 1: Análisis Léxico (Scanner)
            scanner = Scanner(source)
            tokens = scanner.scan()
            
            # Fase 2: Análisis Sintáctico (Parser)
            parser = Parser(tokens)
            ast = parser.parse()
            
            # Fase 3: Evaluación del ASA
            resultado, debe_imprimir = Interprete.evaluador.evaluar(ast)
            
            # Imprimir el resultado si no hay punto y coma
            if debe_imprimir:
                if resultado is None:
                    print("null")
                elif isinstance(resultado, bool):
                    print("true" if resultado else "false")
                else:
                    print(resultado)
            
        except ErrorSemantico as ex:
            # Mostrar error semántico
            print(f"\nERROR SEMÁNTICO:")
            print(f"  {str(ex)}")
            print()
            Interprete.existen_errores = True
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
