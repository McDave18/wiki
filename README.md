# 📚 Wiki – Enciclopedia estilo Wikipedia / Wikipedia-like Encyclopedia (CS50W Project)

Este es un proyecto en **Python/Django** que implementa una enciclopedia en línea similar a Wikipedia, usando archivos en **Markdown** como base de datos de las entradas.  
This is a **Python/Django** project that implements an online encyclopedia similar to Wikipedia, using **Markdown** files as the database for entries.

---

## 🚀 Funcionalidades / Features

- 📄 **Ver entrada / View entry**: `/wiki/TITLE` muestra / displays Markdown content converted to HTML.
- 🔍 **Búsqueda / Search**: exacta (redirige directamente / direct redirect) o parcial (muestra coincidencias / list of results).
- 📝 **Crear entrada / Create entry**: validación para evitar duplicados (case-insensitive) / with validation to prevent case-insensitive duplicates.
- ✏️ **Editar entrada / Edit entry**: formulario con contenido prellenado / form with pre-filled Markdown content.
- 🎲 **Página aleatoria / Random page**: lleva a una entrada al azar / redirects to a random entry.
- ⚠️ **Manejo de errores / Error handling**: páginas 404 y mensajes de conflicto / 404 pages and conflict messages.

---

## 📂 Estructura del proyecto / Project structure

```
wiki/               # Proyecto Django / Django project
│
├── encyclopedia/   # App principal / Main app
│   ├── templates/encyclopedia/
│   ├── static/encyclopedia/
│   ├── views.py
│   ├── urls.py
│   └── util.py
│
├── entries/        # Archivos Markdown (.md) / Markdown (.md) entry files
│
├── manage.py
└── requirements.txt
```

---

## 🛠️ Requisitos previos / Prerequisites

- Python 3.8 o superior / Python 3.8 or higher
- pip (incluido en versiones recientes de Python / included in recent Python versions)
- Navegador web (recomendado: Chrome) / Web browser (recommended: Chrome)
- Git (opcional, para clonar el repositorio / optional, for cloning the repository)

---

## 📥 Instalación y ejecución / Installation and execution

1. **Clonar el repositorio / Clone the repository**
   ```bash
   git clone <URL_DEL_REPOSITORIO / REPOSITORY_URL>
   cd wiki
   ```

2. **Crear y activar entorno virtual / Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. **Instalar dependencias / Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Levantar el servidor / Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Abrir en el navegador / Open in your browser**
   ```
   http://127.0.0.1:8000/
   ```

---

## 📄 Uso / Usage

- **Inicio / Home page**: lista todas las entradas con enlaces clicables / lists all entries with clickable links.
- **Barra lateral / Sidebar**: buscar, crear entrada o ir a una página aleatoria / search, create a new entry, or go to a random page.
- **Ver entrada / View entry**: muestra el contenido Markdown convertido a HTML / displays Markdown content converted to HTML.
- **Editar / Edit**: enlace en la vista de la entrada / link available in the entry view.
- **Errores / Errors**: mensajes claros para entradas inexistentes o conflictos / clear messages for missing entries or conflicts.

---

## 📦 Dependencias / Dependencies

Incluidas en `requirements.txt` / Included in `requirements.txt`:
```
asgiref==3.9.1
Django==5.2.4
markdown2==2.5.4
sqlparse==0.5.3
tzdata==2025.2
```

---

## 🧪 Rutas de prueba rápida para el revisor / Quick test routes for reviewers

- `/wiki/HTML` → Entrada existente / Shows an existing entry
- `/search/?q=py` → Búsqueda parcial / Partial search (should display "Python")
- `/create/` → Crear entrada (probar duplicado y nueva) / Create a new entry (test duplicate and new entry)
- `/wiki/HTML/edit/` → Editar entrada existente / Edit an existing entry
- `/random/` → Página aleatoria / Random page

---

## 📜 Licencia / License

Proyecto académico basado en las especificaciones de [CS50 Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/).  
Academic project based on the specifications from [CS50 Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/).
