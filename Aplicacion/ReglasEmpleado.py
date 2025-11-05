from Persistencia.DAO import EmpleadoDAO

def agregar(empleado):
    if not empleado.run.strip():
        raise ValueError("El RUN del empleado no puede estar vacío")
    if not empleado.nombre.strip():
        raise ValueError("El nombre del empleado no puede estar vacío")
    if not empleado.apellidos.strip():
        raise ValueError("Los apellidos del empleado no pueden estar vacíos")
    return EmpleadoDAO.agregar(empleado)

def modificar(empleado):
    if not empleado.run.strip():
        raise ValueError("El RUN del empleado no puede estar vacío")
    if not empleado.nombre.strip():
        raise ValueError("El nombre del empleado no puede estar vacío")
    if not empleado.apellidos.strip():
        raise ValueError("Los apellidos del empleado no pueden estar vacíos")
    return EmpleadoDAO.modificar(empleado)

def eliminar(id_empleado):
    if id_empleado <= 0:
        raise ValueError("ID de empleado inválido")
    return EmpleadoDAO.eliminar(id_empleado)

def mostrarTodos():
    return EmpleadoDAO.mostrarTodos()

def buscarPorCodigo(id_empleado):
    if id_empleado <= 0:
        raise ValueError("ID de empleado inválido")
    return EmpleadoDAO.buscarPorCodigo(id_empleado)

def buscarPorNombre(nombre):
    if not nombre.strip():
        raise ValueError("El nombre a buscar no puede estar vacío")
    return EmpleadoDAO.buscarPorNombre(nombre)