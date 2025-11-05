from Persistencia.DAO.Conexion import Conexion
from Dominio.DTO.Departamento import Departamento
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db = os.getenv('DB_NAME')

def agregar(departamento):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO departamento (nombre) VALUES (%s)"
        con.ejecuta_query(sql, (departamento.nombre,))
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al agregar departamento: {str(e)}")
    finally:
        if con:
            con.desconectar()

def modificar(departamento):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE departamento SET nombre = %s WHERE id_departamento = %s"
        con.ejecuta_query(sql, (departamento.nombre, departamento.id_departamento))
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al modificar departamento: {str(e)}")
    finally:
        if con:
            con.desconectar()

def eliminar(id_departamento):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM departamento WHERE id_departamento = %s"
        con.ejecuta_query(sql, (id_departamento,))
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al eliminar departamento: {str(e)}")
    finally:
        if con:
            con.desconectar()

def mostrarTodos():
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT id_departamento, nombre FROM departamento"
        cursor = con.ejecuta_query(sql)
        departamentos = []
        for row in cursor.fetchall():
            dept = Departamento(row[0], row[1])
            departamentos.append(dept)
        return departamentos
    except Exception as e:
        raise Exception(f"Error al mostrar departamentos: {str(e)}")
    finally:
        if con:
            con.desconectar()

def buscarPorCodigo(id_departamento):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT id_departamento, nombre FROM departamento WHERE id_departamento = %s"
        cursor = con.ejecuta_query(sql, (id_departamento,))
        row = cursor.fetchone()
        if row:
            return Departamento(row[0], row[1])
        return None
    except Exception as e:
        raise Exception(f"Error al buscar departamento: {str(e)}")
    finally:
        if con:
            con.desconectar()

def buscarPorNombre(nombre):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT id_departamento, nombre FROM departamento WHERE nombre LIKE %s"
        cursor = con.ejecuta_query(sql, (f"%{nombre}%",))
        departamentos = []
        for row in cursor.fetchall():
            dept = Departamento(row[0], row[1])
            departamentos.append(dept)
        return departamentos
    except Exception as e:
        raise Exception(f"Error al buscar departamento por nombre: {str(e)}")
    finally:
        if con:
            con.desconectar()