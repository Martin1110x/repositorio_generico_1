class Persona:
    def __init__(self: object, nombre:  str, apellido: str, dni: int, edad: int, sexo: str):
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.dni: int = dni
        self.edad: int = edad
        self.sexo: str = sexo

    def __str__(self):
        nueva_linea: str = "\n"
        return f"Nombre: {self.nombre}{nueva_linea}Apellido: {self.apellido}{nueva_linea}DNI: {self.dni}{nueva_linea}Edad: {self.edad}{nueva_linea}Sexo: {self.sexo}{nueva_linea}"