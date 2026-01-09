# Intérprete con Árbol de Sintaxis Abstracta (ASA)

## Descripción

Este proyecto implementa un intérprete completo con análisis léxico, sintáctico y semántico. Construye un Árbol de Sintaxis Abstracta (ASA) y lo evalúa para ejecutar las operaciones.

## Características Implementadas

### 1. Operaciones Aritméticas
- **Suma** (`+`)
- **Resta** (`-`)
- **Multiplicación** (`*`)
- **División** (`/`)
- **Módulo** (`%`)

Ejemplos:
```
>>> 5 + 3
8.0
>>> 10 * 2
20.0
>>> 17 % 5
2.0
```

### 2. Operaciones Unarias
- **Negación** (`-`)

Ejemplos:
```
>>> -5
-5.0
>>> x = -10
-10.0
>>> --5
5.0
```

### 3. Variables
- **Creación/Asignación** (`x = valor`)
- **Lectura** (`x`)

Ejemplos:
```
>>> x = 10
10.0
>>> y = x * 2
20.0
>>> x + y
30.0
```

### 4. Agrupación de Expresiones
- Uso de paréntesis para controlar la precedencia

Ejemplos:
```
>>> 2 + 3 * 4
14.0
>>> (2 + 3) * 4
20.0
```

### 5. Impresión Condicional
- **Sin `;`**: Imprime el resultado
- **Con `;`**: No imprime el resultado

Ejemplos:
```
>>> 5 + 3
8.0
>>> 5 + 3;
>>> 
```

### 6. Funciones Built-in

#### `rand()`
Genera un número aleatorio entre 0 y 1.
```
>>> rand()
0.6734177502355964
```

#### `sin(angulo)`
Calcula el seno de un ángulo en radianes.
```
>>> sin(0)
0.0
>>> sin(3.14159 / 2)
0.9999999999991198
```

#### `cos(angulo)`
Calcula el coseno de un ángulo en radianes.
```
>>> cos(0)
1.0
```

#### `sqrt(valor)`
Calcula la raíz cuadrada de un número.
```
>>> sqrt(16)
4.0
>>> sqrt(25)
5.0
```

#### `pow(base, exponente)`
Eleva un número a una potencia.
```
>>> pow(2, 3)
8.0
>>> pow(10, 2)
100.0
```

### 7. Manejo de Errores Semánticos

El intérprete detecta y reporta los siguientes errores semánticos:

#### Número incorrecto de argumentos
```
>>> sin(1, 2, 3)
ERROR SEMÁNTICO:
  La función 'sin' espera 1 argumento(s), pero se recibieron 3
```

#### Tipo de argumento incorrecto
```
>>> sin("Hola")
ERROR SEMÁNTICO:
  sin() requiere un argumento numérico, se recibió: str
```

#### Incompatibilidad de operandos
```
>>> 5 + "Hola"
ERROR SEMÁNTICO:
  Incompatibilidad de operandos para '+': float y str
```

#### Asignación a expresión no válida
```
>>> 5 + x = 3
ERROR:
  [Token: $] Error sintáctico: Objetivo de asignación inválido. Solo se pueden asignar variables.
```

#### Función no definida
```
>>> imprimir(4)
ERROR SEMÁNTICO:
  Función no definida: 'imprimir'
```

#### Llamada a valor no función
```
>>> 4(5, 2)
ERROR SEMÁNTICO:
  No se puede llamar a '4.0' como función. '4.0' es un número, no una función
```

#### Variable no definida
```
>>> w
ERROR SEMÁNTICO:
  Variable no definida: 'w'
```

#### División por cero
```
>>> 10 / 0
ERROR SEMÁNTICO:
  División por cero
```

## Arquitectura del Proyecto

### Archivos Principales

1. **ASA.py**: Define las clases para los nodos del Árbol de Sintaxis Abstracta
   - `Literal`: Valores literales (números, strings, null)
   - `Binaria`: Operaciones binarias (+, -, *, /, %)
   - `Unaria`: Operaciones unarias (-)
   - `Agrupacion`: Expresiones entre paréntesis
   - `Variable`: Acceso a variables
   - `Asignacion`: Asignación de variables
   - `Llamada`: Llamada a funciones
   - `Sentencia`: Sentencia completa con control de impresión

2. **Parser.py**: Analizador sintáctico que construye el ASA
   - Implementa análisis sintáctico predictivo (descenso recursivo)
   - Retorna nodos del ASA en lugar de funciones void

3. **Evaluador.py**: Evaluador del ASA usando el patrón Visitor
   - Recorre el ASA y ejecuta las operaciones
   - Implementa la tabla de símbolos para variables
   - Implementa las funciones built-in
   - Maneja errores semánticos

4. **Interprete.py**: REPL (Read-Eval-Print-Loop)
   - Coordina el análisis léxico, sintáctico y semántico
   - Maneja la impresión condicional
   - Mantiene el entorno entre ejecuciones

5. **Scanner.py**: Analizador léxico (sin cambios)

6. **Token.py**, **TipoToken.py**: Definición de tokens (sin cambios)

## Uso

### REPL Interactivo

Para iniciar el REPL interactivo:

```bash
python Interprete.py
```

Luego puedes escribir expresiones:

```
Intérprete de Lenguaje Estructurado
========================================
Ingrese expresiones para analizar.
Para salir: Ctrl+D (Linux/Mac) o Ctrl+Z + Enter (Windows)
========================================

>>> x = 10
10.0
>>> y = x * 2
20.0
>>> sqrt(x + y)
5.477225575051661
>>> resultado = pow(2, 10);
>>> resultado
1024.0
```

### Pruebas Automatizadas

Para ejecutar las pruebas:

```bash
python test_asa.py
```

Para ver una demostración:

```bash
python demo_repl.py
```

## Ejemplos Complejos

### Teorema de Pitágoras
```
>>> a = 3
3.0
>>> b = 4
4.0
>>> c = sqrt(pow(a, 2) + pow(b, 2))
5.0
>>> c
5.0
```

### Cálculo Trigonométrico
```
>>> pi = 3.14159265359
3.14159265359
>>> angulo = pi / 4
0.7853981633975
>>> seno = sin(angulo)
0.7071067811865476
>>> coseno = cos(angulo)
0.7071067811865476
>>> seno * seno + coseno * coseno
1.0
```

### Generación de Números Aleatorios
```
>>> min = 1
1.0
>>> max = 10
10.0
>>> aleatorio = min + rand() * (max - min)
7.234567890123456
```

## Gramática Implementada

```
STATEMENT      -> EXPRESSION SEMICOLON_OPC
SEMICOLON_OPC  -> ; | ε
EXPRESSION     -> ASSIGNMENT
ASSIGNMENT     -> TERM ASSIGNMENT_OPC
ASSIGNMENT_OPC -> = EXPRESSION | ε
TERM           -> FACTOR TERM'
TERM'          -> - TERM | + TERM | ε
FACTOR         -> UNARY FACTOR'
FACTOR'        -> / FACTOR | * FACTOR | % FACTOR | ε
UNARY          -> - UNARY | CALL
CALL           -> PRIMARY CALL'
CALL'          -> ( ARGUMENTS ) | ε
PRIMARY        -> null | number | string | id | ( EXPRESSION )
ARGUMENTS      -> EXPRESSION ARGUMENTS' | ε
ARGUMENTS'     -> , EXPRESSION ARGUMENTS' | ε
```

## Patrón de Diseño: Visitor

El evaluador utiliza el patrón Visitor para recorrer el ASA:

```python
class Nodo(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Evaluador:
    def evaluar(self, nodo):
        return nodo.accept(self)
    
    def visit_literal(self, literal):
        return literal.valor
    
    def visit_binaria(self, binaria):
        # Evaluar operación binaria
        ...
```

Este patrón permite:
- Separar la estructura del ASA de las operaciones sobre él
- Agregar nuevas operaciones sin modificar las clases del ASA
- Mantener el código organizado y extensible

## Conclusión

Este intérprete implementa completamente:
✅ Construcción de ASA
✅ Evaluación del ASA con patrón Visitor
✅ Operaciones aritméticas y unarias
✅ Variables (creación, lectura, asignación)
✅ Funciones built-in (rand, sin, cos, sqrt, pow)
✅ Agrupación de expresiones
✅ Impresión condicional (con/sin punto y coma)
✅ Detección de errores semánticos
✅ REPL interactivo con persistencia de variables
