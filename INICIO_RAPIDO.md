# 🎯 Inicio Rápido - Intérprete con ASA

## ⚡ Ejecuta el Intérprete en 3 Pasos

### Paso 1: Verifica que Python esté instalado
```bash
python --version
```
Debe mostrar Python 3.6 o superior.

### Paso 2: Navega al directorio del proyecto
```bash
cd "c:\Users\4PF87LA_RS7\OneDrive\Documentos\Compiladores\Practica\Proyecto1Compiladores"
```

### Paso 3: Ejecuta el intérprete
```bash
python Interprete.py
```

## 🎮 Prueba Estos Comandos

Una vez en el REPL, prueba:

```python
>>> 5 + 3
>>> x = 10
>>> y = x * 2
>>> sqrt(16)
>>> pow(2, 10)
>>> a = 3
>>> b = 4
>>> c = sqrt(pow(a, 2) + pow(b, 2))
>>> c
```

## 📋 Comandos Disponibles

| Comando | Descripción |
|---------|-------------|
| `python Interprete.py` | Inicia el REPL interactivo |
| `python test_asa.py` | Ejecuta todas las pruebas |
| `python test_repl.py` | Prueba el REPL |
| `python demo_completa.py` | Demo completa |
| `python demo_repl.py` | Demo rápida |

## 📖 Documentación

| Archivo | Contenido |
|---------|-----------|
| `GUIA_USO.md` | 👈 **Empieza aquí** - Guía rápida |
| `README_ASA.md` | Documentación técnica completa |
| `RESUMEN_EJECUTIVO.md` | Resumen del proyecto |
| `RESUMEN_CAMBIOS.md` | Lista de cambios realizados |

## 🚨 Solución de Problemas

### Problema: "python" no se reconoce
**Solución**: Usa `py` en lugar de `python`:
```bash
py Interprete.py
```

### Problema: No encuentra los archivos
**Solución**: Verifica que estás en el directorio correcto:
```bash
Get-Location
```

### Problema: Error de importación
**Solución**: Verifica que todos los archivos estén presentes:
```bash
Get-ChildItem *.py
```

## ✅ Verificación Rápida

Ejecuta este comando para verificar que todo funciona:
```bash
python test_repl.py
```

Si ves "✅ TODOS LOS TESTS COMPLETADOS", ¡todo está bien!

## 🎓 Características Principales

✅ Operaciones aritméticas: `+`, `-`, `*`, `/`, `%`  
✅ Variables: `x = 10`  
✅ Funciones: `sqrt()`, `pow()`, `sin()`, `cos()`, `rand()`  
✅ Agrupación: `(2 + 3) * 4`  
✅ Control de impresión: `;` para no imprimir  
✅ Errores semánticos detectados automáticamente  

## 💡 Tips

1. Las variables persisten entre comandos
2. Usa `;` al final para no imprimir el resultado
3. Los ángulos deben estar en radianes
4. Para salir: `Ctrl+Z` + `Enter` (Windows)

## 🎉 ¡Listo!

Ya puedes empezar a usar el intérprete. ¡Diviértete! 🚀

---

**¿Necesitas ayuda?** Consulta `GUIA_USO.md` para más información.
