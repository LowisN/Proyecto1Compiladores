# 📚 Índice de Documentación - Proyecto Intérprete con ASA

## 🚀 Inicio Rápido

1. **Lee primero**: [INICIO_RAPIDO.md](INICIO_RAPIDO.md)
2. **Ejecuta**: `python Interprete.py`
3. **Prueba**: Ver ejemplos en [GUIA_USO.md](GUIA_USO.md)

## 📖 Documentación Disponible

### Para Usuarios

| Archivo | Descripción | Cuando Leerlo |
|---------|-------------|---------------|
| **[INICIO_RAPIDO.md](INICIO_RAPIDO.md)** | Guía de inicio en 3 pasos | 👈 **Empieza aquí** |
| **[GUIA_USO.md](GUIA_USO.md)** | Guía completa de usuario con ejemplos | Después del inicio rápido |
| **[README_ASA.md](README_ASA.md)** | Documentación técnica detallada | Para entender la implementación |

### Para Desarrolladores

| Archivo | Descripción | Cuando Leerlo |
|---------|-------------|---------------|
| **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** | Resumen completo del proyecto | Visión general |
| **[RESUMEN_CAMBIOS.md](RESUMEN_CAMBIOS.md)** | Lista detallada de cambios | Para revisar modificaciones |
| **[README_ASA.md](README_ASA.md)** | Arquitectura y diseño | Para entender el código |

## 🎯 Archivos por Propósito

### Quiero ejecutar el intérprete
→ Lee [INICIO_RAPIDO.md](INICIO_RAPIDO.md) y ejecuta `python Interprete.py`

### Quiero aprender a usar el intérprete
→ Lee [GUIA_USO.md](GUIA_USO.md)

### Quiero entender cómo funciona
→ Lee [README_ASA.md](README_ASA.md)

### Quiero ver qué se implementó
→ Lee [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)

### Quiero ver los cambios realizados
→ Lee [RESUMEN_CAMBIOS.md](RESUMEN_CAMBIOS.md)

## 🧪 Scripts de Prueba

| Script | Descripción | Comando |
|--------|-------------|---------|
| `test_asa.py` | Suite completa de pruebas | `python test_asa.py` |
| `test_repl.py` | Pruebas del REPL | `python test_repl.py` |
| `demo_completa.py` | Demostración exhaustiva | `python demo_completa.py` |
| `demo_repl.py` | Demostración rápida | `python demo_repl.py` |

## 📁 Archivos del Proyecto

### Archivos Principales (Nuevos)
- `ASA.py` - Nodos del Árbol de Sintaxis Abstracta
- `Evaluador.py` - Evaluador del ASA (patrón Visitor)

### Archivos Modificados
- `Parser.py` - Ahora construye y retorna el ASA
- `Interprete.py` - Ahora evalúa el ASA

### Archivos Sin Cambios
- `Scanner.py` - Análisis léxico
- `Token.py` - Definición de tokens
- `TipoToken.py` - Tipos de tokens

## 🎓 Flujo de Lectura Recomendado

### Para Usuario Final
1. [INICIO_RAPIDO.md](INICIO_RAPIDO.md) *(3 min)*
2. Ejecutar `python Interprete.py` *(probar comandos)*
3. [GUIA_USO.md](GUIA_USO.md) *(10 min)*
4. Practicar con ejemplos

### Para Revisor/Profesor
1. [RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md) *(5 min)*
2. Ejecutar `python test_asa.py` *(ver todas las pruebas)*
3. [RESUMEN_CAMBIOS.md](RESUMEN_CAMBIOS.md) *(10 min)*
4. [README_ASA.md](README_ASA.md) *(15 min)*
5. Revisar código fuente

### Para Desarrollador
1. [README_ASA.md](README_ASA.md) - Arquitectura *(15 min)*
2. Leer `ASA.py` - Estructura de nodos *(5 min)*
3. Leer `Parser.py` - Construcción del ASA *(10 min)*
4. Leer `Evaluador.py` - Evaluación del ASA *(10 min)*
5. Experimentar con el código

## 📊 Resumen Rápido

### ¿Qué hace este proyecto?
Implementa un intérprete completo con:
- ✅ Análisis léxico (Scanner)
- ✅ Análisis sintáctico (Parser → ASA)
- ✅ Análisis semántico (Evaluador)
- ✅ Ejecución de código
- ✅ Detección de errores

### ¿Qué puedo hacer con él?
- Ejecutar operaciones aritméticas
- Crear y usar variables
- Llamar funciones matemáticas
- Escribir expresiones complejas
- Ver errores semánticos claros

### ¿Cómo lo uso?
```bash
python Interprete.py
>>> x = sqrt(pow(3, 2) + pow(4, 2))
5.0
>>> x
5.0
```

## 🎯 Características Principales

- **Operaciones**: `+`, `-`, `*`, `/`, `%`, `-` (unario)
- **Variables**: Crear, leer, asignar
- **Funciones**: `rand()`, `sin()`, `cos()`, `sqrt()`, `pow()`
- **Agrupación**: Paréntesis para precedencia
- **Control**: `;` para suprimir impresión
- **Errores**: Detección automática de errores semánticos

## 📞 Ayuda

- **Problema al ejecutar**: Ver [INICIO_RAPIDO.md](INICIO_RAPIDO.md) → Solución de Problemas
- **Duda sobre uso**: Ver [GUIA_USO.md](GUIA_USO.md)
- **Pregunta técnica**: Ver [README_ASA.md](README_ASA.md)

## ✅ Verificación Rápida

```bash
python test_repl.py
```

Si ves `[OK] TODOS LOS TESTS COMPLETADOS`, todo funciona correctamente.

---

## 🗂️ Estructura de Este Proyecto

```
📦 Proyecto1Compiladores/
│
├── 📘 Documentación
│   ├── INDICE.md (este archivo)
│   ├── INICIO_RAPIDO.md
│   ├── GUIA_USO.md
│   ├── README_ASA.md
│   ├── RESUMEN_EJECUTIVO.md
│   └── RESUMEN_CAMBIOS.md
│
├── 🐍 Código Fuente
│   ├── ASA.py
│   ├── Evaluador.py
│   ├── Parser.py
│   ├── Interprete.py
│   ├── Scanner.py
│   ├── Token.py
│   └── TipoToken.py
│
└── 🧪 Pruebas y Demos
    ├── test_asa.py
    ├── test_repl.py
    ├── demo_completa.py
    └── demo_repl.py
```

---

**¡Comienza tu viaje aquí!** → [INICIO_RAPIDO.md](INICIO_RAPIDO.md)
