class Alojamiento:

    def __init__(self, nombre, tipo, precio, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.capacidad = capacidad

# 1. mostrar_info()

    def mostrar_info(self):
        # COMPLETAR
        return f'{self.nombre} ({self.tipo}) -- Precio: {self.precio:,.2f} -- Capacidad: {self.capacidad} personas'


 # 2. precio_por_persona()

    def precio_por_persona(self):
        # COMPLETAR
        if self.precio <= 0 or self.capacidad <= 0:
            return None
        return round(self.precio/self.capacidad, 2)

   
# Objeto 1
casa = Alojamiento(
    "Casa Centro",
    "Casa",
    1800,
    6
)

# Objeto 2
departamento = Alojamiento(
    "Departamento Reforma",
    "Departamento",
    1200,
    4
)


# Completa las instrucciones necesarias para:
# 1. Mostrar la información de la casa.
print(casa.mostrar_info())

# 2. Mostrar el precio por persona de la casa.
print(casa.precio_por_persona())

# 3. Mostrar la información del departamento.
print(departamento.mostrar_info())

# 4. Mostrar el precio por persona del departamento.
print(departamento.precio_por_persona())