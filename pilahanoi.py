"Clase NodoPila"
"Explicacion:en nuestro reto torres de hanoi, cada nodo de la pila representa una configuración de los discos en las torres. Por lo tanto, cada nodo debe guardar el número de discos que hay en cada torre. Yd tener una referencia al siguiente nodo, para poder ir pasando los discos de un nodo a otro."
class NodoPila:
    def __init__(self, numero_de_discos):
        self.numero_de_discos = numero_de_discos
        self.siguiente = None 

"Clase Pila"
"Explicacion: La clase Pila debe tener una referencia a la cima de la pila y un contador de la altura de los discos que se van almacenando."
class Pila:
    def __init__(self):
        self.cima = None 
        self.altura = 0
    
    def push(self, nuevo_numero_de_discos):
        nuevo_nodo = NodoPila(nuevo_numero_de_discos)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo
        self.altura += 1

    def pop(self):
        if self.cima is None:
            return None
        else:
            numero_de_discos = self.cima.numero_de_discos
            self.cima = self.cima.siguiente
            self.altura -= 1
            return numero_de_discos
     
    def __str__(self):
        if self.cima is None:
            return "Vacía"
        else:
            contenido = []
            nodo_actual = self.cima
            while nodo_actual:
                contenido.append(nodo_actual.numero_de_discos)
                nodo_actual = nodo_actual.siguiente
            return str(contenido)
