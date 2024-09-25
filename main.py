from fastapi import FastAPI, HTTPException
from odmantic import AIOEngine, Model
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId  # Importar para manejar ObjectId

app = FastAPI()


class Usuario(Model):
    nombre: str
    email: str


client = AsyncIOMotorClient("mongodb://127.0.0.1:64366")
engine = AIOEngine(client=client, database="test_db")


@app.post("/usuarios/")
async def crear_usuario(usuario: Usuario):
    await engine.save(usuario)
    return usuario


@app.get("/usuarios/")
async def listar_usuarios():
    usuarios = await engine.find(Usuario)
    return usuarios


@app.put("/usuarios/{usuario_id}")
async def actualizar_usuario(usuario_id: str, datos: Usuario):
    # Convertir el id en un ObjectId
    if not ObjectId.is_valid(usuario_id):
        raise HTTPException(status_code=400, detail="ID de usuario inválido")

    usuario = await engine.find_one(Usuario, Usuario.id == ObjectId(usuario_id))
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.nombre = datos.nombre
    usuario.email = datos.email
    await engine.save(usuario)
    return usuario


@app.delete("/usuarios/{usuario_id}")
async def eliminar_usuario(usuario_id: str):
    # Convertir el id en un ObjectId
    if not ObjectId.is_valid(usuario_id):
        raise HTTPException(status_code=400, detail="ID de usuario inválido")

    usuario = await engine.find_one(Usuario, Usuario.id == ObjectId(usuario_id))
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    await engine.delete(usuario)
    return {"mensaje": "Usuario eliminado"}
