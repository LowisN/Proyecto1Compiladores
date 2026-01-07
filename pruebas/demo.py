#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de demostración del REPL
"""

from Scanner import Scanner
from Parser import Parser

def demo():
    """Muestra una demostración del funcionamiento del intérprete"""
    print("DEMOSTRACIÓN DEL SCANNER Y PARSER")
    print("=" * 60)
    print()
    
    expresiones = [
        "2 + 3 * 4",
        "x = 10",
        'mensaje = "Hola Mundo"',
        "suma(5, 10, 15)",
        "(2 + 3) * (4 - 1)",
    ]
    
    for expresion in expresiones:
        print(f"\nExpresión: {expresion}")
        print("-" * 60)
        
        try:
            # Scanner
            scanner = Scanner(expresion)
            tokens = scanner.scan()
            
            print("Tokens:")
            for token in tokens:
                print(f"  {token}")
            
            # Parser
            parser = Parser(tokens)
            parser.parse()
            
            print("✓ Expresión válida")
            
        except Exception as e:
            print(f"✗ Error: {str(e)}")

if __name__ == "__main__":
    demo()
