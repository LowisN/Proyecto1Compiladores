#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intérprete con REPL (Read-Evaluate-Print-Loop) que:
1) Escanea (Scanner) -> tokens
2) Parsea (ParserASA) -> ASA (AST)
3) Evalúa (Evaluador) -> ejecuta operaciones y maneja variables/funciones
4) Imprime resultado SOLO si la sentencia no termina con ';'

Para salir: Ctrl+D (Linux/Mac) o Ctrl+Z seguido de Enter (Windows)
"""

import sys
from Scanner import Scanner
from ParserASA import Parser
from Evaluador import Evaluador
from AST import ParseError, SemanticError

class Interprete:
    existen_errores = False

    @staticmethod
    def main():
        print("Intérprete (ASA + Evaluación)")
        print("=" * 40)
        print("Soporta: + - * / %, unario -, variables, (), funciones rand/sin/cos/sqrt/pow")
        print("Imprime si NO hay ';' al final. Para salir: Ctrl+D o Ctrl+Z + Enter")
        print("=" * 40)
        print()

        evaluator = Evaluador()

        while True:
            try:
                linea = input(">>> ")
                if not linea.strip():
                    continue

                Interprete.ejecutar(linea, evaluator)
                Interprete.existen_errores = False

            except EOFError:
                print("\n\n¡Hasta luego!")
                break
            except KeyboardInterrupt:
                print("\n\n¡Hasta luego!")
                break

    @staticmethod
    def ejecutar(source: str, evaluator: Evaluador):
        try:
            scanner = Scanner(source)
            tokens = scanner.scan()

            parser = Parser(tokens)
            stmt = parser.parse()   # <- devuelve ASA (ExprStmt)

            result = evaluator.ejecutar(stmt)
            if result is not None:
                print(Interprete.formato(result))

        except (ParseError, SemanticError) as ex:
            print(f"\nERROR:")
            print(f"  {str(ex)}\n")
            Interprete.existen_errores = True
        except Exception as ex:
            # Cualquier otro error inesperado
            print(f"\nERROR (inesperado):")
            print(f"  {str(ex)}\n")
            Interprete.existen_errores = True

    @staticmethod
    def formato(v):
        # Para que 5.0 se imprima como 5
        if isinstance(v, float):
            if v.is_integer():
                return str(int(v))
            return str(v)
        return str(v)

if __name__ == "__main__":
    Interprete.main()
