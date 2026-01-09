from enum import Enum

class TipoToken(Enum):
    """Enumeración de tipos de tokens del lenguaje"""
    
    # Tokens de un solo caracter
    LEFT_PAREN = "LEFT_PAREN"       # (
    RIGHT_PAREN = "RIGHT_PAREN"     # )
    COMMA = "COMMA"                 # ,
    SEMICOLON = "SEMICOLON"         # ;
    MINUS = "MINUS"                 # -
    PLUS = "PLUS"                   # +
    SLASH = "SLASH"                 # /
    STAR = "STAR"                   # *
    MOD = "MOD"                     # %
    
    # Tokens de uno o dos caracteres
    EQUAL = "EQUAL"                 # =
    EQUAL_EQUAL = "EQUAL_EQUAL"     # ==
    
    # Literales
    IDENTIFIER = "IDENTIFIER"       # Variables/identificadores
    NUMBER = "NUMBER"               # Números
    STRING = "STRING"               # Cadenas de texto
    
    # Palabras reservadas
    NULL = "NULL"                   # null
    TRUE = "TRUE"                   # true  <--- AGREGAR ESTE
    FALSE = "FALSE"                 # false <--- AGREGAR ESTE
    
    # Fin de archivo/cadena
    EOF = "EOF"