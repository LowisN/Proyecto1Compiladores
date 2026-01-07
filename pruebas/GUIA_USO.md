# Guía de Uso del Intérprete

## Cómo ejecutar el intérprete

### Windows (PowerShell)
```powershell
cd "c:\Users\4PF87LA_RS7\OneDrive\Documentos\Compiladores\Practica\src"
python Interprete.py
```

### Linux/Mac
```bash
cd "/path/to/Compiladores/Practica/src"
python3 Interprete.py
```

## Uso del REPL

Una vez iniciado el intérprete, verás el prompt `>>>` donde puedes ingresar expresiones:

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

## Tokens Reconocidos

### Operadores Aritméticos
- `+` (suma)
- `-` (resta)
- `*` (multiplicación)
- `/` (división)
- `%` (módulo)

### Operadores de Comparación
- `=` (asignación)
- `==` (igualdad)

### Delimitadores
- `(` `)` (paréntesis)
- `,` (coma)
- `;` (punto y coma)

### Literales
- **Números**: `123`, `3.14`, `0.5`
- **Cadenas**: `"Hola Mundo"`, `"texto"`
- **Nulo**: `null`
- **Identificadores**: `variable`, `mi_var`, `x123`

## Ejemplos Válidos

### Expresiones Aritméticas
```
>>> 10 + 5
>>> 20 - 8
>>> 4 * 7
>>> 100 / 4
>>> 17 % 5
>>> (2 + 3) * 4
>>> 2 + 3 * 4 - 5 / 2
```

### Operadores Unarios
```
>>> -5
>>> +10
>>> -5 + 3
```

### Asignaciones
```
>>> x = 10
>>> nombre = "Juan"
>>> resultado = 2 + 3
>>> valor = null
```

### Comparaciones
```
>>> x == 5
>>> a == b
>>> 10 == 10
```

### Llamadas a Funciones
```
>>> suma(5, 10)
>>> calcular()
>>> funcion(x, y, z)
>>> f(1 + 2, 3 * 4)
```

### Expresiones Complejas
```
>>> resultado = (a + b) * c
>>> total = suma(x, y) + resta(a, b)
>>> valor = funcion(10, 20) == 30
```

## Ejemplos de Errores

### Error Léxico - Caracter Inválido
```
>>> @#$

✗ ERROR:
  [línea 1] Error: Caracter inesperado: '@'
```

### Error Léxico - Cadena Sin Cerrar
```
>>> "texto sin cerrar

✗ ERROR:
  [línea 1] Error: Cadena sin cerrar
```

### Error Sintáctico - Expresión Incompleta
```
>>> 2 +

✗ ERROR:
  [Token: $] Error sintáctico: Expresión esperada, se encontró: '$'
```

### Error Sintáctico - Paréntesis Sin Cerrar
```
>>> (2 + 3

✗ ERROR:
  [Token: $] Error sintáctico: Se esperaba ')' después de la expresión
```

### Error Sintáctico - Paréntesis Sin Abrir
```
>>> )

✗ ERROR:
  [Token: )] Error sintáctico: Expresión esperada, se encontró: ')'
```

## Ejecutar Pruebas

Para ejecutar todas las pruebas automáticas:

```powershell
cd "c:\Users\4PF87LA_RS7\OneDrive\Documentos\Compiladores\Practica\src"
python test.py
```

Esto ejecutará 28 pruebas válidas y 6 pruebas de errores.

## Ejecutar Demostración

Para ver una demostración rápida:

```powershell
cd "c:\Users\4PF87LA_RS7\OneDrive\Documentos\Compiladores\Practica\src"
python demo.py
```

## Salir del REPL

- **Windows**: Presiona `Ctrl + Z` y luego `Enter`, o `Ctrl + C`
- **Linux/Mac**: Presiona `Ctrl + D`, o `Ctrl + C`

## Estructura de la Salida

Cada expresión procesada muestra:

1. **Análisis Léxico**: Lista de tokens generados con su tipo, lexema y valor opcional
2. **Análisis Sintáctico**: Resultado de la validación según la gramática
3. **Resultado**: ✓ si es válida, ✗ si hay errores

## Notas Importantes

- El intérprete analiza **una expresión por línea**
- Las líneas vacías se ignoran
- Los errores léxicos impiden el análisis sintáctico
- Después de cada entrada, el estado se reinicia
- Los espacios en blanco se ignoran (excepto dentro de cadenas)

## Características Técnicas

### Scanner (Analizador Léxico)
- Reconoce todos los tokens especificados
- Maneja números enteros y decimales
- Procesa cadenas entre comillas dobles
- Detecta la palabra reservada `null`
- Reporta errores léxicos detallados

### Parser (Analizador Sintáctico)
- Implementa análisis predictivo de descenso recursivo
- Valida la sintaxis según la gramática del lenguaje
- Soporta precedencia de operadores
- Maneja expresiones anidadas y recursivas
- Reporta errores sintácticos con contexto

## Gramática del Lenguaje

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

Esta gramática define la precedencia de operadores y la estructura sintáctica del lenguaje.
