from Persistencia.DAO.Conexion import Conexion
from Dominio.DTO.Proyecto import Proyecto
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db = os.getenv('DB_NAME')

def agregar(proyecto):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO proyecto (nombre, fecha_inicio, id_director) VALUES (%s, %s, %s)"
        valores = (proyecto.nombre, proyecto.fecha_inicio, proyecto.id_director)
        con.ejecuta_query(sql, valores)
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al agregar proyecto: {str(e)}")
    finally:
        if con:
            con.desconectar()

def modificar(proyecto):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE proyecto SET nombre = %s, fecha_inicio = %s, id_director = %s WHERE id_proyecto = %s"
        valores = (proyecto.nombre, proyecto.fecha_inicio, proyecto.id_director, proyecto.id_proyecto)
        con.ejecuta_query(sql, valores)
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al modificar proyecto: {str(e)}")
    finally:
        if con:
            con.desconectar()

def eliminar(id_proyecto):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM proyecto WHERE id_proyecto = %s"
        con.ejecuta_query(sql, (id_proyecto,))
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al eliminar proyecto: {str(e)}")
    finally:
        if con:
            con.desconectar()

def mostrarTodos():
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT id_proyecto, nombre, fecha_inicio, id_director FROM proyecto"
        cursor = con.ejecuta_query(sql)
        proyectos = []
        for row in cursor.fetchall():
            proy = Proyecto(row[0], row[1], row[2], row[3])
            proyectos.append(proy)
        return proyectos
    except Exception as e:
        raise Exception(f"Error al mostrar proyectos: {str(e)}")
    finally:
        if con:
            con.desconectar()

def buscarPorCodigo(id_proyecto):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT id_proyecto, nombre, fecha_inicio, id_director FROM proyecto WHERE id_proyecto = %s"
        cursor = con.ejecuta_query(sql, (id_proyecto,))
        row = cursor.fetchone()
        if row:
            return Proyecto(row[0], row[1], row[2], row[3])
        return None
    except Exception as e:
        raise Exception(f"Error al buscar proyecto: {str(e)}")
    finally:
        if con:
            con.desconectar()

def buscarPorNombre(nombre):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT id_proyecto, nombre, fecha_inicio, id_director FROM proyecto WHERE nombre LIKE %s"
        cursor = con.ejecuta_query(sql, (f"%{nombre}%",))
        proyectos = []
        for row in cursor.fetchall():
            proy = Proyecto(row[0], row[1], row[2], row[3])
            proyectos.append(proy)
        return proyectos
    except Exception as e:
        raise Exception(f"Error al buscar proyecto por nombre: {str(e)}")
    finally:
        if con:
            con.desconectar()