#Voy a crear un diccionario vacio como base de datos para almacenar
#los usuario en claves y las contraseñas en valores
datos_usuarios = {}

#Esta funcion me permite registrar usuarios 
def registrar_usuario():
    while True:
        print("""Bienvenido al registro de usuarios. Complete los siguientes datos 
para crear su usuario.""")
        nombre_usuario = input("Ingrese un nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")
        
#Con este ciclo verifico si el nombre de usuario ya existe
        if nombre_usuario in datos_usuarios:
            print("""El nombre de usuario ya existe. 
Por favor, elija otro nombre de usuario.""")
        else:
            datos_usuarios[nombre_usuario] = contraseña
            print("Usuario registrado con éxito.")
#Dentro del ciclo while pongo un bloque if-elif para preguntarle si quiere registrar otro usuario        
        mensaje = input("Seleccione una de las siguientes opciones:\nA) Registrar otro usuario\nB) Finalizar\n: ")
    
        if mensaje.upper() == "B":
            break
        elif mensaje.upper() != "A":
            print("Opción no válida")

#Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    
# Verificar si el nombre de usuario existe
    if nombre_usuario in datos_usuarios:
        contraseña = input("Ingrese su contraseña: ")
        
#Verificar si la contraseña es correcta
        if datos_usuarios[nombre_usuario] == contraseña:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta. Intente de nuevo.")
    else:
        print("El nombre de usuario no está registrado. Regístrese primero.")

# Función para mostrar los datos almacenados 
def mostrar_datos():
    for usuario, contraseña in datos_usuarios.items():
        print(f"Los usuarios que se han registrados son: {usuario}, Contraseña: {contraseña}")

# Llamar a las funciones según sea necesario
registrar_usuario()
iniciar_sesion()
mostrar_datos()
