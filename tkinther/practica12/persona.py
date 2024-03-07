from LoginTkinnther import *

objectPeople = LoginTkinnther()

while True:
    print("====Menu======")
    print("1. crear persona: ")
    print("2. editar persona: ")
    print("3. eliminar persona: ")
    print("4. consultar persona: ")
    print("6. salir ")
    opcion = input("elige una opcion: ")
    
    if opcion == "1":
        print(" == ingresa los datos del usuario a crear == ")
        usuario= input(" ingresa el correo del usuario: ")
        password= input(" ingresa el password del usuario: ")
        
        objectPeople.Insertar(usuario,password)
        print("usuario creado correctamente")
    
    elif opcion == "2":
        print(" ===introduce el correo del usuario a editar=== ")
        usuario= input("correo: ")
        password= input("password: ")
        
        objectPeople.editar(usuario,password)
        