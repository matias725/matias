from Persistencia.DAO import ProyectoDAO

def agregar(proyecto):
    if not proyecto.nombre.strip():
        raise ValueError("El nombre del proyecto no puede estar vacío")
    return ProyectoDAO.agregar(proyecto)

def modificar(proyecto):
    if not proyecto.nombre.strip():
        raise ValueError("El nombre del proyecto no puede estar vacío")
    return ProyectoDAO.modificar(proyecto)

def eliminar(id_proyecto):
    if id_proyecto <= 0:
        raise ValueError("ID de proyecto inválido")
    return ProyectoDAO.eliminar(id_proyecto)

def mostrarTodos():
    return ProyectoDAO.mostrarTodos()

def buscarPorCodigo(id_proyecto):
    if id_proyecto <= 0:
        raise ValueError("ID de proyecto inválido")
    return ProyectoDAO.buscarPorCodigo(id_proyecto)

def buscarPorNombre(nombre):
    if not nombre.strip():
        raise ValueError("El nombre a buscar no puede estar vacío")
    return ProyectoDAO.buscarPorNombre(nombre)