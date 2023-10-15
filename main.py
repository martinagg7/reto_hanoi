from pilahanoi import *

def getTablero(n):
    pila_torre1 = Pila()
    pila_torre2 = Pila()
    pila_torre3 = Pila()

    for disco in range(n, 0, -1):
        pila_torre1.push(disco)

    return (pila_torre1, pila_torre2, pila_torre3)

def solve(tablero, n, inicial, auxiliar, final):
    if n == 1:
        disco = inicial.pop()
        final.push(disco)
        print(f"Disco {disco} de Torre {inicial.num} a Torre {final.num}")
    else:
        solve(tablero, n - 1, inicial, final, auxiliar)
        disco = inicial.pop()
        final.push(disco)
        print(f"Disco {disco} de Torre {inicial.num} a Torre {final.num}")
        solve(tablero, n - 1, auxiliar, inicial, final)

if __name__ == "__main__":
    n = 5
    tablero = getTablero(n)
    torre1, torre2, torre3 = tablero

    torre1.num = 1
    torre2.num = 2
    torre3.num = 3

    print("Inicialmente:")
    print(f"Torre 1 {torre1}")
    print(f"Torre 2 {torre2}")
    print(f"Torre 3 {torre3}")

    print("Resolviendo...:")
    solve(tablero, n, torre1, torre2, torre3)

    print("Listo!:")
    print(f"Torre 1 {torre1}")
    print(f"Torre 2 {torre2}")
    print(f"Torre 3 {torre3}")

