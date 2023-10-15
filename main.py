from pilahanoi import *

def getTablero(n):
    pila_palo1 = Pila()
    pila_palo2 = Pila()
    pila_palo3 = Pila()

    #metemos los discos con los que vamos a jugar en el palo incial pero de mayor a menor
    for disco in range(n, 0, -1):
        pila_palo1.push(disco)

    return (pila_palo1, pila_palo2, pila_palo3)

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

        # Mover n-1 discos de auxiliar a final usando el palo inicial como ayuda
        solve(tablero, n - 1, auxiliar, inicial , final)

if __name__ == "__main":
    n = 5  # Cantidad de discos
    tablero = getTablero(n)
    torre1, torre2, torre3 = tablero

    print("Estado inicial del tablero:")
    print(f"Torre 1: {torre1}")
    print(f"Torre 2: {torre2}")
    print(f"Torre 3: {torre3}")

    print("\nResolviendo el problema de las Torres de Hanoi:")
    solve(tablero, n, torre1, torre2, torre3)

    print("\nEstado final del tablero:")
    print(f"Torre 1: {torre1}")
    print(f"Torre 2: {torre2}")
    print(f"Torre 3: {torre3}")
