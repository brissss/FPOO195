from Usuario import *

#solicitar agregar datos, consultar, editar, eliminar
opcion = input("Elige una opción: ")

if opcion == "agregar":
  idU = int(input('ingrese el id del usuario:\n'))
  nombreU = input('Escribe el nombre del usuario:\n ')
  apellidosU = input('Escribe los apellidos del usuario:\n')
  sexoU = input('Ingresa el sexo del usuario:\n ')
  edadU = int(input('Escribe la edad del usuario:\n '))
  correoU = input('Escribe el correo del usuario:\n')
  contrasenaU = input('Ingresa la contraseña del usuario:\n ')

elif opcion == "consultar":
    idU = int(input('Ingrese el ID del usuario a consultar:\n'))
    
    print("ID: " + idU)
    print("Nombre: " + nombreU)
    print("Apellidos: " + apellidosU)
    print("Sexo: " + sexoU)
    print("Edad: " + edadU)
    print("Correo: " + correoU)
    
elif opcion == "editar":
    idU = int(input('Ingrese el ID del usuario a editar:\n'))
    
    nombreU = input('Escribe el nuevo nombre del usuario:\n ')
    apellidosU = input('Escribe los nuevos apellidos del usuario:\n')
    sexoU = input('Ingresa el nuevo sexo del usuario:\n ')
    edadU = int(input('Escribe la nueva edad del usuario:\n '))
    correoU = input('Escribe el nuevo correo del usuario:\n')
    contrasenaU = input('Ingresa la nueva contraseña del usuario:\n ')
    
    print("Usuario actualizado correctamente.")
    
elif opcion == "eliminar":
     idU = int(input('Ingrese el ID del usuario a eliminar:\n'))
     
     print("usuario eliminado correctamente.")
else:
  print("Opción no válida.")
  exit()


#solicitar consultar datos
Perfil = Usuario(idU,nombreU,apellidosU,sexoU,edadU,correoU,contrasenaU)

#uso de atributos
print(Perfil.getId())
print(Perfil.getNombre())
print(Perfil.getApellidos())
print(Perfil.getSexo())
print(Perfil.getEdad())
print(Perfil.getCorreo())
print(Perfil.getContrasena())

#uso de metodos
Perfil.crear()
Perfil.actualizar()
Perfil.consultar()
Perfil.eliminar()