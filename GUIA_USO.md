# 🚀 Guía Rápida de Uso - Intérprete con ASA

## ⚡ Inicio Rápido

### 1. Ejecutar el REPL Interactivo

```bash
python Interprete.py
```

Esto abrirá el intérprete interactivo:

```
Intérprete de Lenguaje Estructurado
========================================
Ingrese expresiones para analizar.
Para salir: Ctrl+D (Linux/Mac) o Ctrl+Z + Enter (Windows)
========================================

>>> 
```

### 2. Ejemplos Básicos

```python
>>> 5 + 3
8.0

>>> x = 10
10.0

>>> y = x * 2
20.0

>>> sqrt(16)
4.0

>>> pow(2, 10)
1024.0
```

## 📚 Operaciones Disponibles

### Aritméticas
```python
>>> 10 + 5          # Suma
15.0
>>> 10 - 5          # Resta
5.0
>>> 10 * 5          # Multiplicación
50.0
>>> 10 / 5          # División
2.0
>>> 10 % 3          # Módulo
1.0
```

### Precedencia y Agrupación
```python
>>> 2 + 3 * 4       # Multiplicación primero
14.0
>>> (2 + 3) * 4     # Suma primero (paréntesis)
20.0
```

### Operaciones Unarias
```python
>>> -5
-5.0
>>> -(10 + 5)
-15.0
```

### Variables
```python
>>> x = 10          # Crear variable
10.0
>>> y = x + 5       # Usar variable
15.0
>>> x = x * 2       # Reasignar
20.0
```

### Punto y Coma (;)
```python
>>> x = 100         # Imprime el resultado
100.0
>>> y = 200;        # NO imprime (tiene ;)
>>> x + y           # Imprime
300.0
```

## 🔢 Funciones Matemáticas

### rand() - Número Aleatorio
```python
>>> rand()
0.7234567890123456
>>> aleatorio = rand() * 100
73.45678901234567
```

### sin(angulo) - Seno
```python
>>> sin(0)
0.0
>>> pi = 3.14159265359
>>> sin(pi / 2)
1.0
```

### cos(angulo) - Coseno
```python
>>> cos(0)
1.0
>>> cos(pi)
-1.0
```

### sqrt(valor) - Raíz Cuadrada
```python
>>> sqrt(16)
4.0
>>> sqrt(2)
1.4142135623730951
```

### pow(base, exponente) - Potencia
```python
>>> pow(2, 3)
8.0
>>> pow(10, 2)
100.0
```

## 💡 Ejemplos Prácticos

### Teorema de Pitágoras
```python
>>> a = 3
>>> b = 4
>>> c = sqrt(pow(a, 2) + pow(b, 2))
>>> c
5.0
```

### Área de un Círculo
```python
>>> pi = 3.14159265359
>>> radio = 5
>>> area = pi * pow(radio, 2)
>>> area
78.53981633975
```

### Conversión Grados → Radianes
```python
>>> grados = 45
>>> pi = 3.14159265359
>>> radianes = grados * pi / 180
>>> radianes
0.7853981633975
>>> sin(radianes)
0.7071067811865476
```

### Promedio
```python
>>> a = 10
>>> b = 20
>>> c = 30
>>> promedio = (a + b + c) / 3
>>> promedio
20.0
```

## ❌ Errores Comunes

### ❌ Número incorrecto de argumentos
```python
>>> sin(1, 2, 3)
ERROR SEMÁNTICO:
  La función 'sin' espera 1 argumento(s), pero se recibieron 3
```

### ❌ Tipo incorrecto
```python
>>> sin("Hola")
ERROR SEMÁNTICO:
  sin() requiere un argumento numérico, se recibió: str
```

### ❌ Incompatibilidad de tipos
```python
>>> 5 + "texto"
ERROR SEMÁNTICO:
  Incompatibilidad de operandos para '+': float y str
```

### ❌ Variable no definida
```python
>>> x
ERROR SEMÁNTICO:
  Variable no definida: 'x'
```

### ❌ Función no definida
```python
>>> imprimir(10)
ERROR SEMÁNTICO:
  Función no definida: 'imprimir'
```

### ❌ División por cero
```python
>>> 10 / 0
ERROR SEMÁNTICO:
  División por cero
```

## 🧪 Ejecutar Pruebas

### Pruebas Automatizadas Completas
```bash
python test_asa.py
```

### Demostración Completa
```bash
python demo_completa.py
```

### Demostración Rápida
```bash
python demo_repl.py
```

## 📖 Documentación Adicional

- **README_ASA.md**: Documentación técnica completa
- **RESUMEN_CAMBIOS.md**: Lista detallada de cambios realizados

## 💻 Requisitos

- Python 3.6 o superior
- Bibliotecas estándar: `math`, `random` (incluidas en Python)

## 🎯 Características

✅ Operaciones aritméticas (+, -, *, /, %)  
✅ Operaciones unarias (-)  
✅ Variables (creación, lectura, asignación)  
✅ Funciones matemáticas (rand, sin, cos, sqrt, pow)  
✅ Agrupación con paréntesis  
✅ Impresión condicional (con/sin ;)  
✅ Detección de errores semánticos  
✅ REPL interactivo con persistencia  

## 📝 Notas

- Las variables persisten entre expresiones en la misma sesión del REPL
- Los números se representan como flotantes (float)
- Los ángulos en funciones trigonométricas deben estar en radianes
- Para salir del REPL: `Ctrl+D` (Linux/Mac) o `Ctrl+Z` + `Enter` (Windows)

---

**¡Disfruta usando el intérprete! 🎉**
