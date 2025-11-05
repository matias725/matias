from Presentacion.MenuPrincipal import MenuPrincipal

def main():
    try:
        menu_principal = MenuPrincipal()
        menu_principal.ejecutar()
    except Exception as e:
        print(f"Error en la aplicación: {str(e)}")

if __name__ == "__main__":
    main()