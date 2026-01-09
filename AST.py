# -*- coding: utf-8 -*-
"""
Definición del Árbol de Sintaxis Abstracta (ASA / AST) para el intérprete.

Nodos de expresión:
- Literal      : números, strings, null
- Variable     : lectura de variable (id)
- Assign       : asignación (id = expr)
- Unary        : operación unaria (-expr)
- Binary       : operaciones binarias (+,-,*,/,%)
- Grouping     : agrupación (expr)
- Call         : llamadas a funciones (id(args))

Nodo de sentencia:
- ExprStmt     : una expresión como sentencia; puede imprimir o no según ';'
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional

# ---------------------------
# Errores
# ---------------------------

class ParseError(Exception):
    """Error sintáctico (o de construcción del ASA)"""
    pass

class SemanticError(Exception):
    """Error semántico al evaluar el ASA"""
    pass

# ---------------------------
# Expresiones (ASA)
# ---------------------------

class Expr:
    pass

@dataclass(frozen=True)
class Literal(Expr):
    value: Any  # float | str | None

@dataclass(frozen=True)
class Variable(Expr):
    name: str

@dataclass(frozen=True)
class Assign(Expr):
    name: str
    value: Expr

@dataclass(frozen=True)
class Unary(Expr):
    op: str
    right: Expr

@dataclass(frozen=True)
class Binary(Expr):
    left: Expr
    op: str
    right: Expr

@dataclass(frozen=True)
class Grouping(Expr):
    expr: Expr

@dataclass(frozen=True)
class Call(Expr):
    callee: str
    args: List[Expr]

# ---------------------------
# Sentencias
# ---------------------------

class Stmt:
    pass

@dataclass(frozen=True)
class ExprStmt(Stmt):
    expr: Expr
    print_result: bool
