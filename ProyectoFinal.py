from os import system
import time


class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, anio, director, genero, sinopsis, imagen):
        self._titulo = titulo
        self._director = director
        self._anio = anio
        self._genero = genero
        self._sinopsis = sinopsis
        self._imagen = imagen     

    def __str__(self):
        return 'Titulo: {self._titulo} \nAnio: {self._anio}\nDirector: {self._director} \nGenero: {self._genero}\nSinopsis: {self._sinopsis}\nImagen: {self._imagen}'
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def anio(self):
        return self._anio

    @property
    def director(self):
        return self._director

    @property
    def genero(self):
        return self._genero

    @property
    def sinopsis(self):
        return self._sinopsis
    
    @property
    def imagen(self):
        return self._imagen

    @titulo.setter
    def titulo(self, x):
        self._titulo = x

    @anio.setter
    def anio(self, x):
        self._anio = x

    @director.setter
    def director(self, x):
        self._director = x

    @genero.setter
    def genero(self, x):
        self._genero = x

    @sinopsis.setter
    def sinopsis(self, x):
        self._sinopsis = x

    @imagen.setter
    def imagen(self, x):
        self._imagen = x


class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)

    def ultimas10(self):
        print('----------Ultimas peliculas agregadas----------\n\n')
        for i in range(9,-1,-1):
            print('###############################################\n')
            print(self.peliculas[x])
            print('')
        print('---------------------------------------------------')


class Usuario:
    def __init__(self, usuario, contrasenia):
        self._usuario = usuario
        self._contrasenia = contrasenia

    @property
    def usuario(self):
        return self._usuario

    @property
    def contrasenia(self):
        return self._contrasenia

    @usuario.setter
    def usuario(self, x):
        self._usuario = x

    @contrasenia.setter
    def contrasenia(self, x):
        self._contrasenia = x


class Registrados:
    registrados = []

    def __init__(self, registrados=[]):
        self.registrados = registrados

    def agregar(self, u):
        self.registrados.append(u)

    def estaRegistrado(self, u):
        esta = False
        for x in registrados:
            if u == x:
                esta = True
        return esta


def datosIncorrectos():
    print('Los datos ingresados son incorrectos.\n')
    print('1. Ingresar de nuevo')
    print('2. Registrarse')
    print('3. Volver al menu principal')
    opcion = input('Elija una opcion: ')
    while True:
        if(opcion == 1):
            system('cls')
            ingresar()
            break
        elif(opcion == 2):
            system('cls')
            registrar()
            break
        elif opcion == 3:
            system('cls')
            menu()
            break
        else:
            print('Opcion invalida')
            time.sleep(3)
            system('cls')
            datosIncorrectos()
            break

def ingresar()
    us = input('Usuario: ')
    cont = input('Contrasenia: ')
    usuario = Usuario(us, cont)
    r = Registrados()
    if (r.estaRegistrado(usuario)):
        paginaUsRegis()
    else:
        datosIncorrectos()

def registrar()
    us = input('Usuario: ')
    cont = input('Contrasenia: ') 
    cont2 = input('Repetir contrasenia: ')

    while True:
        confirm = input('Los datos ingresados son correctos? s/n: ')

        if confirm == 's' or confirm == 'S':
            break
        elif confirm == 'n' or confirm == 'N':
            system('cls')
            registrar()
            break
        else:
            print('Ingrese "s" o "n"')
            continue


    
    if cont == cont2:
        usuario = Usuario(us, cont)
        r = Registrados()
        if r.estaRegistrado(usuario):
            print('Este usuario ya ha sido registrado, intente de nuevo')
            system('cls')
            registrar()
        else:
            r.agregar(usuario)
            print('Su usuario ha sido registrado con exito!')
            print('1. Ingresar')
            print('2. Volver al menu principal')
            while True:
                opcion = input('Elija una opcion: ')
                if opcion == 1:
                    system('cls')
                    ingresar()
                    break
                elif opcion == 2:
                    system('cls')
                    menu()
                    break
                else:
                    print('Opcion invalida')
                    continue
    else:
        print('Las contrasenias no coinciden, intente de nuevo.')
        system('cls')
        registrar()

def menu():
    c = Catalogo()
    c.ultimas10()
    print('-----------------------Menu------------------------')
    print('1. Ingresar')
    print('2.Registrarse')
    opcion = input('/Ingrese una opcion:')
    while True:
        if(opcion == 1):
            system('cls')
            ingresar()
            break
        elif(opcion == 2):
            system('cls')
            registrar()
            break
        else:
            print('Opcion invalida')
            time.sleep(3)
            system('cls')
            menu()
            break

menu()