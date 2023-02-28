
if __name__ == '__main__':
    while True:
        print("..::::...Bienvenido...::::...")
        print('1. Ingresar archivo')
        print('2. Salir')
        menu = input()
        if menu == '1':
            ruta = "ruta"
            print('La ruta elegida es: ', ruta)
            print()
            print('Ingrese Y o y para confirmar la ruta.')
            menu = input()
            if menu == 'Y' or menu == 'y':
                listaPacientes = "llamarlista"
                input()
            else:
                print('Error comando no reconocido')
                input()
        elif menu == '2':
            break

        
        