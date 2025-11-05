# Sistema de Gestión de Personal

Sistema CRUD completo para gestión de personal desarrollado en Python con arquitectura en 4 capas.

## Características

- **Arquitectura en 4 Capas**: Dominio, Persistencia, Aplicación, Presentación
- **POO con Herencia**: Implementación orientada a objetos con polimorfismo
- **Seguridad SQL**: Consultas parametrizadas para prevenir inyección SQL
- **Base de Datos MySQL**: Conexión segura con PyMySQL

## Entidades

- **Departamento**: Gestión de departamentos de la empresa
- **Empleado**: Gestión de empleados con relación a departamentos
- **Proyecto**: Gestión de proyectos con directores (empleados)

## Instalación

1. Instalar dependencias:
```bash
pip install pymysql python-dotenv
```

2. Configurar base de datos en `.env`:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=pro
```

3. Ejecutar script SQL en phpMyAdmin (XAMPP)

4. Ejecutar aplicación:
```bash
python main.py
```

## Estructura del Proyecto

```
├── Dominio/DTO/          # Entidades del negocio
├── Persistencia/DAO/     # Acceso a datos
├── Aplicacion/           # Lógica de negocio
├── Presentacion/         # Interfaz de usuario
├── script_empresa.sql    # Script de base de datos
└── main.py              # Punto de entrada
```