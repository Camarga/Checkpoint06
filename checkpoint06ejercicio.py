class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def info_usuario(self):
        return f"Nombre de usuario: {self.nombre_usuario}, Contraseña: {self.contraseña}"


usuario1 = Usuario("Pablo", "5b@890")
print(usuario1.info_usuario())