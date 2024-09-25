# CRUD Básico con FastAPI, Odmantic y MongoDB

Este proyecto implementa un CRUD (Crear, Leer, Actualizar, Eliminar) básico utilizando **FastAPI** como framework web, **Odmantic** como ODM (Object-Document Mapper) para interactuar con MongoDB y **Motor** como el driver asíncrono para MongoDB.

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para crear APIs con Python.
- **Odmantic**: ODM (Object-Document Mapper) para trabajar con MongoDB a través de un estilo similar a los ORMs como SQLAlchemy, pero optimizado para bases de datos NoSQL.
- **Motor**: Driver asíncrono para MongoDB, que permite la interacción no bloqueante con la base de datos.
- **Uvicorn**: Un servidor ASGI que ejecuta la aplicación FastAPI de forma eficiente y con soporte asíncrono.

## Requisitos Previos

- Python 3.8 o superior
- Docker (para ejecutar MongoDB localmente)

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/DiegoLerma/odmantic.git
   cd odmantic
   ```

2. **Instalar las dependencias:**
   Se recomienda utilizar un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usar venv\Scripts\activate
   pip install fastapi odmantic motor uvicorn
   ```

3. **Iniciar MongoDB usando Docker:**
   Si no tienes MongoDB instalado localmente, puedes ejecutarlo rápidamente usando Docker:

   ```bash
   docker run --name mongodb -p 27017:27017 mongo:4.2.18-rc0-bionic
   ```

   Esto expondrá MongoDB en `localhost` en el puerto 27017.

## Ejecución

1. **Ejecutar la aplicación:**
   Una vez que MongoDB esté en funcionamiento, puedes correr la aplicación utilizando **uvicorn**:

   ```bash
   uvicorn main:app --reload
   ```

2. **Acceder a la API:**
   La API estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000), y puedes ver la documentación interactiva generada automáticamente en:
   - Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

### Crear un Usuario (POST /usuarios/)

- **Descripción**: Crea un nuevo usuario en la base de datos.
- **Ejemplo de Solicitud**:

   ```json
   {
     "nombre": "Juan Perez",
     "email": "juan.perez@example.com"
   }
   ```

### Listar Usuarios (GET /usuarios/)

- **Descripción**: Obtiene la lista de todos los usuarios registrados.

### Actualizar Usuario (PUT /usuarios/{usuario_id})

- **Descripción**: Actualiza la información de un usuario basado en su ID.
- **Ejemplo de Solicitud**:

   ```json
   {
     "nombre": "Juan Actualizado",
     "email": "nuevo.email@example.com"
   }
   ```

### Eliminar Usuario (DELETE /usuarios/{usuario_id})

- **Descripción**: Elimina un usuario de la base de datos basado en su ID.

## Descripción de Odmantic

**Odmantic** es un Object-Document Mapper (ODM) para MongoDB, diseñado para aprovechar la funcionalidad asíncrona de Python. Proporciona una sintaxis similar a los Object-Relational Mappers (ORM) que se utilizan comúnmente con bases de datos SQL, pero está optimizado para trabajar con documentos JSON en bases de datos NoSQL como MongoDB.

### Ventajas de Odmantic

1. **Fácil de usar**: Proporciona una API clara y sencilla para definir modelos de datos utilizando clases de Python que heredan de `Model`.

2. **Integración con FastAPI**: Odmantic trabaja perfectamente con FastAPI, facilitando la validación y serialización de datos a través de Pydantic, lo cual garantiza la integridad de los datos en las peticiones HTTP.

3. **Asíncrono**: Odmantic está basado en Motor, un driver asíncrono para MongoDB. Esto permite que las operaciones de lectura y escritura en la base de datos no bloqueen el resto de la aplicación, lo que mejora la eficiencia y el rendimiento.

4. **Definición de Modelos Sencilla**: Los modelos se definen de manera similar a Pydantic, lo que facilita la definición de los esquemas de datos y su validación.

### Ejemplo de Modelo con Odmantic

```python
from odmantic import Model

class Usuario(Model):
    nombre: str
    email: str
```

En el ejemplo anterior, `Usuario` es un modelo que se almacena como un documento en MongoDB. Cada instancia de `Usuario` representa un documento en la colección correspondiente.

### Operaciones Soportadas

- **Creación de documentos**: Mediante `engine.save()`.
- **Consulta de documentos**: Con `engine.find()` o `engine.find_one()`.
- **Actualización de documentos**: Simplemente modificando los atributos y llamando a `engine.save()`.
- **Eliminación de documentos**: Utilizando `engine.delete()`.

## Próximos pasos

1. **Implementar manejo de errores**: Es importante añadir manejo de excepciones en caso de fallos al conectar con MongoDB o errores en la validación de los datos.

2. **Agregar autenticación**: Se puede integrar autenticación para restringir el acceso a los endpoints.
