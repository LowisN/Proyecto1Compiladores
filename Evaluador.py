# -*- coding: utf-8 -*-
"""
Evaluador / Intérprete del ASA.

Soporta:
- Aritmética: + - * / %
- Unario: -expr
- Variables: creación/lectura/asignación (id = expr)
- Agrupación: (expr)
- Impresión en REPL: depende de print_result en ExprStmt
- Funciones: rand(), sin(x), cos(x), sqrt(x), pow(x,y)

Errores semánticos:
- Aridad incorrecta
- Tipos de argumentos incorrectos
- Incompatibilidad de operandos
- Variable no definida
- Función no definida
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, List, Callable
import math
import random

from AST import (
    SemanticError,
    Expr, Stmt,
    Literal, Variable, Assign, Unary, Binary, Grouping, Call,
    ExprStmt
)

Value = Any  # float | str | None

@dataclass
class BuiltinSpec:
    arity: int
    fn: Callable[[List[Value]], Value]

class Evaluador:
    def __init__(self):
        self.vars: Dict[str, Value] = {}
        self.funcs: Dict[str, BuiltinSpec] = self._builtins()

    def _builtins(self) -> Dict[str, BuiltinSpec]:
        def need_number(v: Value, where: str) -> float:
            if not isinstance(v, (int, float)):
                raise SemanticError(f"{where} requiere un argumento numérico.")
            return float(v)

        return {
            "rand": BuiltinSpec(0, lambda args: random.random()),
            "sin": BuiltinSpec(1, lambda args: math.sin(need_number(args[0], "sin()"))),
            "cos": BuiltinSpec(1, lambda args: math.cos(need_number(args[0], "cos()"))),
            "sqrt": BuiltinSpec(1, lambda args: self._sqrt(need_number(args[0], "sqrt()"))),
            "pow": BuiltinSpec(2, lambda args: math.pow(
                need_number(args[0], "pow(base, exp)"),
                need_number(args[1], "pow(base, exp)")
            )),
        }

    def _sqrt(self, x: float) -> float:
        if x < 0:
            raise SemanticError(f"sqrt() no acepta valores negativos: {x}")
        return math.sqrt(x)

    # ----------------------------
    # Ejecución de sentencias
    # ----------------------------

    def ejecutar(self, stmt: Stmt) -> Value | None:
        if isinstance(stmt, ExprStmt):
            val = self.eval(stmt.expr)
            return val if stmt.print_result else None
        raise SemanticError("Sentencia no soportada.")

    # ----------------------------
    # Evaluación de expresiones
    # ----------------------------

    def eval(self, expr: Expr) -> Value:
        if isinstance(expr, Literal):
            return expr.value

        if isinstance(expr, Grouping):
            return self.eval(expr.expr)

        if isinstance(expr, Variable):
            if expr.name not in self.vars:
                raise SemanticError(f"Variable no definida: {expr.name}")
            return self.vars[expr.name]

        if isinstance(expr, Assign):
            value = self.eval(expr.value)
            self.vars[expr.name] = value
            return value

        if isinstance(expr, Unary):
            right = self.eval(expr.right)
            if expr.op == "-":
                self._ensure_number(right, "Operador unario '-'")
                return -float(right)
            raise SemanticError(f"Operador unario no soportado: {expr.op}")

        if isinstance(expr, Binary):
            left = self.eval(expr.left)
            right = self.eval(expr.right)
            op = expr.op

            if op in {"+", "-", "*", "/", "%"}:
                self._ensure_number(left, f"Operación '{op}'")
                self._ensure_number(right, f"Operación '{op}'")
                a = float(left)
                b = float(right)

                if op == "+": return a + b
                if op == "-": return a - b
                if op == "*": return a * b
                if op == "/":
                    if b == 0.0:
                        raise SemanticError("División entre cero.")
                    return a / b
                if op == "%":
                    if b == 0.0:
                        raise SemanticError("Módulo entre cero.")
                    return a % b

            raise SemanticError(f"Operador binario no soportado: {op}")

        if isinstance(expr, Call):
            if expr.callee not in self.funcs:
                raise SemanticError(f"Función no definida: {expr.callee}")

            spec = self.funcs[expr.callee]
            if len(expr.args) != spec.arity:
                raise SemanticError(
                    f"Número incorrecto de argumentos para {expr.callee}(): "
                    f"esperaba {spec.arity}, recibió {len(expr.args)}"
                )

            args = [self.eval(a) for a in expr.args]
            return spec.fn(args)

        raise SemanticError("Expresión no soportada.")

    def _ensure_number(self, v: Value, where: str):
        if not isinstance(v, (int, float)):
            raise SemanticError(f"Incompatibilidad de operandos: {where} requiere números (se recibió {type(v).__name__}).")
