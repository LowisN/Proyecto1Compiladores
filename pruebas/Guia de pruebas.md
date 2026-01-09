# Intérprete de Lenguaje Estructurado

Este proyecto implementa un intérprete para un lenguaje con sintaxis similar a C/Java, capaz de realizar operaciones matemáticas, gestión de variables y llamadas a funciones nativas.

## Características

* **REPL (Read-Eval-Print Loop):** Interfaz de línea de comandos interactiva.
* **Tipos de Datos:** Números (flotantes), Cadenas de texto.
* **Operaciones:** Aritmética básica (+, -, *, /, %).
* **Variables:** Asignación dinámica y persistencia en memoria.
* **Funciones Nativas:** Soporte para `sin`, `cos`, `sqrt`, `pow`, `rand`, `clock`.
* **Manejo de Errores:** Reporte detallado de errores léxicos, sintácticos y semánticos.

## Requisitos y Ejecución

* **Requisito:** Python 3.x instalado.
* **Ejecución:**
    Abrir una terminal en la carpeta del proyecto y ejecutar:
    ```bash
    python Principal.py
    ```

## Casos de Prueba (Ejemplos de Uso)

A continuación se presentan los comandos para probar que el intérprete cumple con lo solicitado en la práctica.

### 1. Operaciones Aritméticas y Agrupación
Prueba la precedencia de operadores y el uso de paréntesis.
>>> 5 + 5
10.0
>>> 10 - 2 * 3
4.0
>>> (10 - 2) * 3
24.0
>>> 5 * (4 + 3)
35.0

### 2. Variables y Asignación
Prueba la creación de variables, lectura y el uso del ; para suprimir la salida.
>>> x = 10;
(No imprime nada, pero guarda x)
>>> x
10.0
>>> y = x * 2 + 5
25.0
>>> x = y - 5;
>>> x
20.0

### 3. Operaciones Unarias
Prueba el operador de negación.
>>> -5 + 10
5.0
>>> x = -10;
>>> -x
10.0

### 4. Funciones Nativas
Prueba la llamada a funciones implementadas en la tabla de símbolos.
>>> sin(0)
0.0
>>> cos(0)
1.0
>>> sqrt(25)
5.0
>>> pow(2, 3)
8.0
>>> rand()
0.548... (Número aleatorio)

### 5. Validaciones Semánticas (Errores)
Prueba que el intérprete detecte y reporte errores lógicos correctamente.
#### Argumentos incorrectos
>>> sin(1, 2)
ERROR: Se esperaban 1 argumentos.
#### Tipos Incompatibles
>>> 5 + "Hola"
ERROR: Operandos incompatibles para suma.
#### Llamada a no-función
>>> 4(5)
ERROR: Solo se pueden llamar funciones.
#### Variables no definidas
>>> imprimir(x)
ERROR: Variable no definida: 'imprimir'.