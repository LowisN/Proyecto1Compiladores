# Intérprete de Lenguaje Estructurado

Implementación en Python de un analizador léxico (Scanner) y sintáctico (Parser) para un lenguaje estructurado simple.

## Estructura del Proyecto

```
src/
├── TipoToken.py     # Enumeración de tipos de tokens
├── Token.py         # Clase Token
├── Scanner.py       # Analizador léxico
├── Parser.py        # Analizador sintáctico
└── Interprete.py    # REPL principal
```

## Componentes

### 1. REPL (Read-Execute-Print-Loop)
Interfaz interactiva que permite al usuario ingresar expresiones para ser analizadas.

### 2. Scanner (Analizador Léxico)
Genera los siguientes tokens:
- **Operadores aritméticos**: `+`, `-`, `*`, `/`, `%`
- **Paréntesis**: `(`, `)`
- **Separadores**: `,`, `;`
- **Asignación**: `=`, `==`
- **Literales**: 
  - Números (enteros y decimales)
  - Cadenas de texto (entre comillas dobles)
  - `null`
- **Identificadores**: Variables y nombres de funciones
- **EOF**: Fin de cadena

### 3. Parser (Analizador Sintáctico)
Analizador sintáctico predictivo de descenso recursivo que verifica la validez de las expresiones según la gramática del lenguaje.

#### Gramática Implementada
```
programa    → expresion EOF
expresion   → asignacion
asignacion  → IDENTIFIER = asignacion | logica_or
logica_or   → logica_and (== logica_and)*
logica_and  → igualdad
igualdad    → comparacion ((==) comparacion)*
comparacion → termino
termino     → factor ((+ | -) factor)*
factor      → unario ((* | / | %) unario)*
unario      → (+ | -) unario | primario
primario    → NUMBER | STRING | null | IDENTIFIER | (expresion) | llamada
llamada     → IDENTIFIER (argumentos)?
argumentos  → expresion (, expresion)*
```

## Requisitos

- Python 3.6 o superior

## Ejecución

Para ejecutar el intérprete:

```powershell
cd src
python Interprete.py
```

## Ejemplos de Uso

### Expresiones Aritméticas
```
>>> 2 + 3
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <NUMBER 2 2.0>
  <PLUS + >
  <NUMBER 3 3.0>
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---
✓ Análisis sintáctico exitoso: La expresión es válida
```

### Expresiones con Paréntesis
```
>>> (5 + 3) * 2
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <LEFT_PAREN ( >
  <NUMBER 5 5.0>
  <PLUS + >
  <NUMBER 3 3.0>
  <RIGHT_PAREN ) >
  <STAR * >
  <NUMBER 2 2.0>
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---
✓ Análisis sintáctico exitoso: La expresión es válida
```

### Asignaciones
```
>>> x = 10
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <IDENTIFIER x >
  <EQUAL = >
  <NUMBER 10 10.0>
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---
✓ Análisis sintáctico exitoso: La expresión es válida
```

### Cadenas de Texto
```
>>> mensaje = "Hola Mundo"
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <IDENTIFIER mensaje >
  <EQUAL = >
  <STRING "Hola Mundo" Hola Mundo>
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---
✓ Análisis sintáctico exitoso: La expresión es válida
```

### Llamadas a Funciones
```
>>> suma(5, 10, 15)
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <IDENTIFIER suma >
  <LEFT_PAREN ( >
  <NUMBER 5 5.0>
  <COMMA , >
  <NUMBER 10 10.0>
  <COMMA , >
  <NUMBER 15 15.0>
  <RIGHT_PAREN ) >
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---
✓ Análisis sintáctico exitoso: La expresión es válida
```

### Operador Módulo
```
>>> 10 % 3
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <MOD % >
  <NUMBER 3 3.0>
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---
✓ Análisis sintáctico exitoso: La expresión es válida
```

### Comparaciones
```
>>> x == 5
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <IDENTIFIER x >
  <EQUAL_EQUAL == >
  <NUMBER 5 5.0>
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---
✓ Análisis sintáctico exitoso: La expresión es válida
```

### Valor Nulo
```
>>> valor = null
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <IDENTIFIER valor >
  <EQUAL = >
  <NULL null >
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---
✓ Análisis sintáctico exitoso: La expresión es válida
```

## Manejo de Errores

### Error Léxico
```
>>> @#$
--- ANÁLISIS LÉXICO ---

✗ ERROR:
  [línea 1] Error: Caracter inesperado: '@'
```

### Error Sintáctico
```
>>> 2 + + 3
--- ANÁLISIS LÉXICO ---
Tokens generados:
  <NUMBER 2 2.0>
  <PLUS + >
  <PLUS + >
  <NUMBER 3 3.0>
  <EOF $ >

--- ANÁLISIS SINTÁCTICO ---

✗ ERROR:
  [Token: +] Error sintáctico: Expresión esperada, se encontró: '+'
```

### Cadena Sin Cerrar
```
>>> "texto sin cerrar
--- ANÁLISIS LÉXICO ---

✗ ERROR:
  [línea 1] Error: Cadena sin cerrar
```

## Salir del Intérprete

- **Linux/Mac**: `Ctrl + D`
- **Windows**: `Ctrl + Z` seguido de `Enter`
- **Alternativa**: `Ctrl + C`

## Características Implementadas

✅ REPL interactivo con prompt `>>>`  
✅ Análisis léxico completo con manejo de errores  
✅ Reconocimiento de todos los tokens requeridos  
✅ Análisis sintáctico predictivo  
✅ Validación de expresiones según la gramática  
✅ Manejo de errores léxicos y sintácticos  
✅ Mensajes de error descriptivos  
✅ Soporte para números decimales  
✅ Soporte para cadenas de texto  
✅ Soporte para identificadores  
✅ Soporte para llamadas a funciones con argumentos  
✅ Operadores aritméticos y de comparación

## Notas

- El análisis léxico se detiene al encontrar el primer error
- El análisis sintáctico solo se ejecuta si no hay errores léxicos
- Los errores muestran la línea y una descripción del problema
- El intérprete resetea el estado de errores después de cada entrada
