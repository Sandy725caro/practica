let="abcdefghijklmnopqrstuvwxyz"
def cesar(ct,pas):
    decs=""
    for i in ct:
        pos=let.find(i)- pas
        md=int(pos)% len(let)
        decs=decs+str(let[md])
    return decs.lower()


#usuario : sandy
#contraseña :  khfuvy
#clave : 7
nombrecuenta="sandy"
sanclave=str(input("ingresa el nombre de usuario:  "))
if sanclave==nombrecuenta:
    print("usuario reconocido")
    ctr=str(input("ingresa la contraseña: "))
    clnu=int(input("ingresa el nuemero clave: "))
    clavesesar=cesar(ctr,clnu)
    if clavesesar=="daynor":
        print("clave reconocida")
        print("iniciooooo y hasta aqui llegue")
    else:
        print("contraseña no reconocida")
else:
    print("no reconosco el nombre de la cuenta")