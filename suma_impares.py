from functools import reduce

def main():
    operaciones()
   
def pregunta():
    pregunta = input('Introduce una serie de números separados por un espacio: ')
    respuesta = pregunta.split()

    lista_global = []
    for n in respuesta:
        lista_global.append(int(n))
    return lista_global

def filtrar(número):
    if número % 2 != 0:
        return True
    return False
    
def suma(a,b):
    return a+b

def operaciones():
    lista = pregunta()
    filtro = filter(filtrar,lista)
    impares = list(filtro)
    sumatorio = reduce(suma,impares)
    print(f"La suma de los números de Impares = {impares} es {sumatorio}")
   
    

if __name__ == "__main__":
    main()
