from pilahanoi import *

def getTablero(n):
    pila_torre1 = Pila()
    pila_torre2 = Pila()
    pila_torre3 = Pila()

    #metemos los discos con los que vamos a jugar en el palo incial pero de mayor a menor
    for disco in range(n, 0, -1):
        pila_torre1.push(disco)

    return (pila_torre1, pila_torre2, pila_torre3)

def solve(tablero, n, inicial, auxiliar, final):
    if n == 1:
        # caso base que solo tenemos un disco y lo pasamos directamente al palo final
        disco = inicial.pop()
        final.push(disco)
        print("Disco", disco, "de Torre", inicial, "a Torre", final)
    else:
        # llevamos nuestro discos del palo inicial al palo auxiliar usando el palo final para ayudarnos
        solve(tablero, n - 1, inicial, final, auxiliar)

        
        disco = inicial.pop()
        final.push(disco)
        print("Disco", disco, "de Torre", inicial, "a Torre", final)

        # movemos los discos de auxiliar a final usando el palo inicial como ayuda
        solve(tablero, n - 1, auxiliar, inicial , final)

if __name__ == "__main":
    n = 5  
    tablero = getTablero(n)
    torre1, torre2, torre3 = tablero

    print("Incialmente:")
    print("Torre 1",torre1)
    print("Torre 2",torre2)
    print("Torre 3",torre3)

    print("Resolviendo...:")
    solve(tablero, n, torre1, torre2, torre3)

    print("Listo!:")
    print("Torre 1",torre1)
    print("Torre 2",torre2)
    print("Torre 3",torre3)
