"Clase NodoPila"
class NodoPila:
    "ATRIBUTOS DE LA CLASE NODOPILA"
    def __init__(self,numero_discos):
        self.numero_discos = numero_discos
        self.siguiente = None #sirve para unir los nodos

"Clase Pila"
class Pila:
    "ATRIBUTOS DE LA CLASE PILA"
    def __init__(self):
        self.cima = None 
        self.altura = 0
    
    " MÉTODO:apilar discos "
    def push(self,nuevo_numero_discos):
        nuevo_nodo = NodoPila(nuevo_numero_discos)
        if self.cima is None:
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo
        self.altura += 1
    "METODO: desapilar discos"
    def pop(self):
     if self.cima is None:
        return None
     else:
        numero_de_discos = self.cima.numero_de_discos
        self.cima = self.cima.siguiente
        self.tamano -= 1
        return numero_de_discos
     
    "METODO: informacion de cada pila"
    def __str__(self):
        if self.cima is None:
            return "Pila vacía"
        else:
            valores=[]
            nodo_actual = self.cima
            while nodo_actual:
                valores.append(nodo_actual.numero_discos)
                nodo_actual = nodo_actual.siguiente
            return str(valores)


