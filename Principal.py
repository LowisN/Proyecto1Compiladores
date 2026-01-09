#!/usr/bin/env python3
# Principal.py
# Módulo: Interfaz principal (REPL) que lee, parsea y ejecuta código del usuario.

import sys
from Scanner import Scanner
from Parser import Parser
from Motor import Motor

class Principal:
    """
    Clase principal que gestiona el ciclo REPL (Read-Eval-Print Loop).
    Es la interfaz entre el usuario y el intérprete.
    """
    # Bandera para indicar si ocurrió un error en la última ejecución
    existen_errores = False
    
    # Instancia del Motor Lógico. Se crea FUERA del bucle para que
    # la memoria (variables definidas) persista durante toda la sesión.
    motor = Motor() 
    
    @staticmethod
    def main():
        """Bucle principal de ejecución: lectura del usuario, evaluación y salida."""
        print("=======================================")
        print("   INTERPRÉTE DE LENGUAJE ESTRUCTURADO")
        print("=======================================")
        print("Escribe tus sentencias. Ejemplo: x = 10; sin(x)")
        print("Presiona Ctrl+C para salir.")
        print()
        
        while True:
            try:
                # 1. READ: Leer entrada del usuario
                linea = input(">>> ")
                if not linea.strip(): continue
                
                # 2. EVAL & PRINT: Ejecutar la línea
                Principal.ejecutar(linea)
                
                # Resetear bandera de errores para la siguiente línea
                Principal.existen_errores = False
                
            except (EOFError, KeyboardInterrupt):
                print("\n¡Hasta luego!")
                break
    
    @staticmethod
    def ejecutar(source):
        """Orquesta las fases: Escaneo -> Parseo -> Ejecución (REPL)."""
        try:
            # FASE 1: Scanner (Léxico)
            scanner = Scanner(source)
            tokens = scanner.scan()
            
            # FASE 2: Parser (Sintáctico)
            parser = Parser(tokens)
            statements = parser.parse()
            
            # Si el parser falló (retornó None), no intentamos ejecutar
            if statements is None: return

            # FASE 3: Motor (Semántico / Ejecución)
            Principal.motor.interpret(statements)
            
        except Exception as ex:
            # Captura cualquier error (sintáctico, léxico o en tiempo de ejecución)
            print(f"ERROR: {ex}")
            Principal.existen_errores = True

if __name__ == "__main__":
    Principal.main()