from Persistencia.DAO.Conexion import Conexion
from Dominio.DTO.Empleado import Empleado
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
db = os.getenv('DB_NAME')

def agregar(empleado):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """INSERT INTO empleado 
                (run, nombre, apellidos, direccion, fono, correo, fecha_contrato, id_departamento) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (empleado.run, empleado.nombre, empleado.apellidos, empleado.direccion,
                  empleado.fono, empleado.correo, empleado.fecha_contrato, empleado.id_departamento)
        con.ejecuta_query(sql, valores)
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al agregar empleado: {str(e)}")
    finally:
        if con:
            con.desconectar()

def modificar(empleado):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """UPDATE empleado SET run = %s, nombre = %s, apellidos = %s, 
                direccion = %s, fono = %s, correo = %s, fecha_contrato = %s, 
                id_departamento = %s WHERE id_empleado = %s"""
        valores = (empleado.run, empleado.nombre, empleado.apellidos, empleado.direccion,
                  empleado.fono, empleado.correo, empleado.fecha_contrato, 
                  empleado.id_departamento, empleado.id_empleado)
        con.ejecuta_query(sql, valores)
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al modificar empleado: {str(e)}")
    finally:
        if con:
            con.desconectar()

def eliminar(id_empleado):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM empleado WHERE id_empleado = %s"
        con.ejecuta_query(sql, (id_empleado,))
        con.commit()
        return True
    except Exception as e:
        if con:
            con.rollback()
        raise Exception(f"Error al eliminar empleado: {str(e)}")
    finally:
        if con:
            con.desconectar()

def mostrarTodos():
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """SELECT id_empleado, run, nombre, apellidos, direccion, 
                fono, correo, fecha_contrato, id_departamento FROM empleado"""
        cursor = con.ejecuta_query(sql)
        empleados = []
        for row in cursor.fetchall():
            emp = Empleado(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            empleados.append(emp)
        return empleados
    except Exception as e:
        raise Exception(f"Error al mostrar empleados: {str(e)}")
    finally:
        if con:
            con.desconectar()

def buscarPorCodigo(id_empleado):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """SELECT id_empleado, run, nombre, apellidos, direccion, 
                fono, correo, fecha_contrato, id_departamento FROM empleado WHERE id_empleado = %s"""
        cursor = con.ejecuta_query(sql, (id_empleado,))
        row = cursor.fetchone()
        if row:
            return Empleado(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        return None
    except Exception as e:
        raise Exception(f"Error al buscar empleado: {str(e)}")
    finally:
        if con:
            con.desconectar()

def buscarPorNombre(nombre):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """SELECT id_empleado, run, nombre, apellidos, direccion, 
                fono, correo, fecha_contrato, id_departamento FROM empleado 
                WHERE nombre LIKE %s OR apellidos LIKE %s"""
        cursor = con.ejecuta_query(sql, (f"%{nombre}%", f"%{nombre}%"))
        empleados = []
        for row in cursor.fetchall():
            emp = Empleado(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            empleados.append(emp)
        return empleados
    except Exception as e:
        raise Exception(f"Error al buscar empleado por nombre: {str(e)}")
    finally:
        if con:
            con.desconectar()