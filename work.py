#Sistema de incripcion a curso Online
#nombre✅, #edad entre 18 y 65✅, #correo con @ y .com o .cl✅, #telefono 9digitos✅, cursos a tomar✅
#menu✅
#registro✅
#descueto
#salir.

usuarios = []

import time
import os

while True:
    print("-"*70)
    print("B i e n v e i d o   a l   s i s t e m a   d e   i n s c r i p c i ó n  c u r s o s  O n l i n e".center(70," "))
    print("-"*70)
    
    opuser = input(" 1.Inscribir persona. \n 2.Ver inscritos. \n 3.Calcular pago con descuento. \n 4.Salir \n")
    
    if opuser == "1":
        while True:
            print("Inscribete.")
            nombre = input("Ingresa tu nombre completo!:\n")
            if nombre.replace(" ", "").isalpha():
                print("Nombre guardado con Exito!")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("Solo puedes ingresar letras!, Intenta nuevamente.")
                continue
        while True:
            try:
                edad = int(input("Ingresa tu edad:\n"))
                assert(edad in range(18, 66))
                print("Edad guradada con exito!")
                time.sleep(0.5)
                break
            except AssertionError:
                print("La edad debe estar entre 18 y 65 años")
            except:
                print("Uy! no puedes ingresar letras!")
        while True:
            correo = input("Ingresa tu correo electronico:\n")
            if "@" in correo and (correo.endswith(".com") or correo.endswith(".cl")):
                print("Correo Válido!")
                time.sleep(0.5)
                break
            else:
                print("Correo inválido, debe contener @ y terminar en .com o .cl")
        while True:
            telefono = input("Ingresa tu número de teléfono (9 digitos): \n")
            if telefono.isdigit() and len(telefono) == 9:
                print("Teléfono válido!")
                time.sleep(0.5)
                break
            else:
                print("Teléfono inválido, el número debe contener 9 dígitos numéricos.!")
        while True:
            print("¿Qué taller le gustaría tomar?")
            taller = input("Opciones: python, Diseño UX, Excel, Ciberseguridad\n" ).strip().lower()
            talleresdisponibles = ["python", "diseño UX", "excel","ciberseguridad"]
            if taller in talleresdisponibles:
                print("Taller tomado con éxito!")
                time.sleep(0.5)
                os.system('cls')
                break
            else:
                print("Solo puedes ingresar uno de los talleres válidos, Intenta nuevamente \n")
                
        usuario = {
                "nombre"  : nombre,
                "edad"    : edad,
                "taller"  : taller,
                "correo"  : correo,
                "telefono": telefono,
            }
        usuarios.append(usuario)
        print("Usuario inscritos correctamente!\n")



    elif opuser == "2":
        if not usuarios:
            print("No hay usuarios inscritos aún.\n")
        else:
            print("\nUsuarios inscritos:\n")
            for i, u in enumerate(usuarios, 1):
                
                print(f"Usuario: {i}:")
                print(f" Nombre: {u["nombre"]}")
                print(f" Edad:  {u["edad"]}")
                print(f" Taller: {u["taller"]}")
                print(f" Correo: {u["correo"]}")
                print(f" Teléfono: {u["telefono"]}")
        
        
    
    elif opuser == "3":
        print("Ver Descueto")
        if not usuarios:
            print("No hay usuarios para calcular el pago\n")
        else:
            print("\n Cálculo de mensualidad con descuento:")
        if edad in range(19,26):
            por = 20
        elif edad in range(27,41):
            por = 10
        else:
            por = 0
        print(f"El monto del descuento obtenido es  {por}%")

    elif opuser == "4":
        print("Gracias por usar el sistema de inscripcion, vuelva pronto!.")
        break
    else:
        print("Opcion no valida, intente nuevamente.!")