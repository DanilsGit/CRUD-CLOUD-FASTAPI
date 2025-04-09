# CRUD-CLOUD-FASTAPI
Práctica para APLICACIONES EN EL WEB Y REDES INALÁMBRICAS

Una REST API simple construida con **FastAPI** y **SQLAlchemy** para la gestión de eventos. Permite crear, listar, consultar, actualizar y eliminar eventos de manera sencilla.

Actualmente, esta API está desplegada en **Amazon Web Services (AWS)**.

## 🚀 Características

- Crear, obtener, actualizar y eliminar eventos.
- Validación de datos con **Pydantic**.
- Conexión a base de datos SQL con **SQLAlchemy**.
- Arquitectura modular y lista para producción.

## 🧠 Modelo de Evento

```python
class Event(Base):
    id: int
    title: str
    description: str
    location: str
    start_time: datetime
    end_time: datetime
```

## ⚙️ Instalación y uso local

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/DanilsGit/CRUD-CLOUD-FASTAPI.git
   cd event-api
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado)**:
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno**:
   - Copia el archivo `.env.example` como `.env`:
     ```bash
     cp .env.example .env
     ```
   - Completa los valores según tu entorno (por ejemplo, `DATABASE_URL`).

5. **Inicia la aplicación**:
   ```bash
   fastapi dev
   ```

## 📚 Endpoints

| Método | Ruta               | Descripción                 |
|--------|--------------------|-----------------------------|
| POST   | `/events/`         | Crear un nuevo evento       |
| GET    | `/events/`         | Obtener todos los eventos   |
| GET    | `/events/{id}`     | Obtener un evento por ID    |
| PUT    | `/events/{id}`     | Actualizar un evento por ID |
| DELETE | `/events/{id}`     | Eliminar un evento por ID   |

## 👥 Integrantes

- **Daniel Esteban Marquez Upegui**
- **Joan Manuel Jaramillo Avila**

## ✅ Notas

- La documentación interactiva está disponible en:  
  [http://localhost:8000/docs](http://localhost:8000/docs) (cuando se ejecuta localmente)
