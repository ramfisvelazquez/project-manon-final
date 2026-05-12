# Lumière

Lumière es una tienda de moda desarrollada con Reflex y Python, inspirada en un diseño moderno, elegante y minimalista.  
La aplicación incluye categorías para Women, Men y Kids, además de navegación dinámica entre páginas.

---

# Características

- Diseño moderno y responsive
- Navegación entre páginas
- Categorías de moda
- Integración de imágenes dinámicas
- Íconos sociales interactivos
- Desarrollado completamente con Reflex + Python

---

# Tecnologías utilizadas

- Python
- Reflex
- Poetry
- JSON
- HTML/CSS mediante Reflex

---

# Instalación

## 1. Clonar el proyecto

```bash
git clone https://github.com/tuusuario/lumiere.git
cd lumiere
```

---

## 2. Instalar Poetry

Instalar Poetry desde su página oficial:

https://python-poetry.org/docs/

Verificar instalación:

```bash
poetry --version
```

---

## 3. Instalar Reflex con Poetry

```bash
poetry add reflex
```

---

## 4. Instalar dependencias del proyecto

```bash
poetry install
```

---

## 5. Ejecutar el proyecto

```bash
poetry run reflex run
```

La aplicación se ejecutará en:

```plaintext
http://localhost:3000
```

---

# Estructura del proyecto

```plaintext
lumiere/
│
├── assets/
│
├── lumiere/
│   ├── __init__.py
│   ├── index.py
│   ├── Women.py
│   ├── Men.py
│   ├── Kids.py
│
├── rxconfig.py
├── pyproject.toml
└── README.md
```

---

# Rutas disponibles

- `/`
- `/women`
- `/men`
- `/kids`

---

# Solución de errores comunes

## Error 404 Not Found

Eliminar la carpeta `.web` y reiniciar Reflex:

```bash
rmdir /s /q .web
poetry run reflex run
```

---

## Error:
```plaintext
No module update found for route routes/._index
```

### Solución

1. Detener Reflex
2. Eliminar `.web`
3. Ejecutar nuevamente:

```bash
poetry run reflex run
```

---

# Autor
Ramfis Velazquez
Proyecto desarrollado con Reflex + Python.
