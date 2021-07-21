import itertools


class Contacto:

    def __init__(self, nombre, movil, email):
        self._nombre = nombre
        self._movil = movil
        self._email = email


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    @property
    def movil(self):
        return self._movil

    @movil.setter
    def movil(self, movil):
        self._movil = movil


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email


    def __str__(self):

        return f"Nombre: {self._nombre}.\nMovil: {self._movil}.\nEmail: {self._email}."