import os
import time
from modelos.verificar_datos import Validacion
from modelos.contactos import Contacto
from datos.conexion import Agenda


validar = Validacion()

db = Agenda()


def imprimir_opciones():
    print()
    print('BIENVENIDO A LA AGENDA DE CONTACTOS')
    print('='*50)
    print('Selecciona una Opción:')
    print('[C]rear Contacto.')
    print('[L]istado de Contactos.')
    print('[M]odificar Contacto.')
    print('[E]liminar Contacto.')
    print('[B]uscar Contacto.')
    print('[S]alir')


def chequiar_datos(mensaje, nombre_dato):

    print(mensaje)

    entrada_datos = input('>>>')

    try:
        getattr(validar, f"validar_{nombre_dato}")(entrada_datos)
        return entrada_datos
    except ValueError as e:
        print(e)
        return chequiar_datos(mensaje, nombre_dato)


def crear_contacto():

    os.system('clear')
    print('INGRESAR CONTACTO.')
    print('*'*50)

    nombre = chequiar_datos('Inserte el nombre:', 'nombre')
    movil = chequiar_datos('Inserte el movil:', 'telefono')
    email = chequiar_datos('Inserte el email:','email')

    contacto = Contacto(nombre, movil, email)

    db.grabar(contacto)

    run()


def lista_contactos():

    os.system('clear')
    print('LISTA DE CONTACTOS.')
    print('*'*50)

    db.listar_contactos()

    print()
    print('Pulse cualquier tecla para continuar.')
    input()
    print()

    run()


def existen_contactos():

    respuesta = db.existe_archivo()

    if respuesta == False:
        print()
        print('No existe datos guardados, primero guarde contactos.')

        print()
        print('Pulse cualquier tecla para continuar.')
        input()
        print()

        run()


def buscar_contacto():

    existen_contactos()

    os.system('clear')
    print('BUSCAR UN CONTACTO.')
    print('*'*50)

    nombre = chequiar_datos('Inserte nombre a buscar:','nombre')

    db.buscar_contacto(nombre)

    print()
    print('Pulse cualquier tecla para continuar.')
    input()
    print()

    run()


def actualizar_contacto():

    os.system('clear')
    print('ACTUALIZAR CONTACTO.')
    print('*'*50)   

    db.listar_contactos()

    print()

    nombre = chequiar_datos('Inserte nombre del contacto a modificar :','nombre')
    print()
    nuevo_nombre = chequiar_datos('Inserte el nuevo nombre: ','nombre')
    nuevo_movil = chequiar_datos('Inserte el nuevo numero de movil: ','telefono')
    nuevo_email = chequiar_datos('Inserta el nuevo email: ','email')

    datos = (nombre,nuevo_nombre,nuevo_movil,nuevo_email)

    db.modificar_contacto(datos)

    print()
    print('Contacto modificado correctamente.')

    print()
    print('Pulse cualquier tecla para continuar.')
    input()
    print()

    run()


def borrar_contacto():

    existen_contactos()

    os.system('clear')
    print('BORRAR CONTACTO.')
    print('*'*50)   

    db.listar_contactos()

    print()

    nombre = chequiar_datos('Inserte nombre del contacto a borrar :','nombre')
    print()

    db.elimiminar_contacto(nombre)

    print('Contacto eliminado correctamente.')

    print()
    print('Pulse cualquier tecla para continuar.')
    input()
    print()

    run()


def run():

    os.system('clear')

    imprimir_opciones()

    print()
    opcion = input('Ingrese opcion: ')
    opcion =opcion.upper()

    if opcion == 'C':
        crear_contacto()
    elif opcion == 'L':
        lista_contactos()
    elif opcion == 'M':
        actualizar_contacto()
    elif opcion == 'E':
        borrar_contacto()
    elif opcion == 'B':
        buscar_contacto()
    elif opcion == 'S':
        os.system('clear')
        print()
        print('Gracias por utilizar la app, hasta pronto.')
        print()
        os._exit(1)
    else:
        print('Opción Invalida.')
        time.sleep(1)
        run()




if __name__ == '__main__':
    run()
