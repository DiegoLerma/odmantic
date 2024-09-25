from fastapi import FastAPI
from odmantic import AIOEngine, Model
from motor.motor_asyncio import AsyncIOMotorClient

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
    usuario = await engine.find_one(Usuario, Usuario.id == usuario_id)
    usuario.nombre = datos.nombre
    usuario.email = datos.email
    await engine.save(usuario)
    return usuario


@app.delete("/usuarios/{usuario_id}")
async def eliminar_usuario(usuario_id: str):
    usuario = await engine.find_one(Usuario, Usuario.id == usuario_id)
    await engine.delete(usuario)
    return {"mensaje": "Usuario eliminado"}
