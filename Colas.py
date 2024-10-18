from abc import ABC, abstractmethod

# Clase Pedido
class Pedido:
    def __init__(self, cantidad, cliente):
        self.cliente = cliente
        self.cantidad = cantidad

    def imprimir_pedido(self):
        print(f"     Cliente: {self.get_cliente()}")
        print(f"     Cantidad: {self.get_cantidad()}")
        print("     ------------")

    def get_cantidad(self):
        return self.cantidad

    def get_cliente(self):
        return self.cliente


# Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# Interfaz ColaInterface
class ColaInterface(ABC):
    @abstractmethod
    def tamaño(self):
        pass

    @abstractmethod
    def esta_vacia(self):
        pass

    @abstractmethod
    def frente(self):
        pass

    @abstractmethod
    def agregar(self, info):
        pass

    @abstractmethod
    def eliminar(self):
        pass


# Clase Cola que implementa la interfaz ColaInterface
class Cola(ColaInterface):
    def __init__(self):
        self.nodo_frente = None
        self.nodo_final = None
        self.contador = 0

    def tamaño(self):
        return self.contador

    def esta_vacia(self):
        return self.nodo_frente is None

    def frente(self):
        if not self.esta_vacia():
            return self.nodo_frente.dato
        return None

    def agregar(self, info):
        nuevo_nodo = Nodo(info)
        if self.nodo_final is not None:
            self.nodo_final.siguiente = nuevo_nodo
        self.nodo_final = nuevo_nodo
        if self.nodo_frente is None:
            self.nodo_frente = nuevo_nodo
        self.contador += 1

    def eliminar(self):
        if self.esta_vacia():
            return None
        dato_eliminado = self.nodo_frente.dato
        self.nodo_frente = self.nodo_frente.siguiente
        if self.nodo_frente is None:
            self.nodo_final = None
        self.contador -= 1
        return dato_eliminado

    def imprimir_cola(self):
        nodo = self.nodo_frente
        indice = 1
        
        while nodo is not None:
            print(f"   ** Elemento {indice}")
            nodo.dato.imprimir_pedido()
            indice += 1
            nodo = nodo.siguiente


# Ejemplo de uso de la cola con pedidos
if __name__ == "__main__":
    cola = Cola()
    
    # Agregar pedidos a la cola
    cola.agregar(Pedido(20, "cliente1"))
    cola.agregar(Pedido(30, "cliente2"))
    cola.agregar(Pedido(40, "cliente3"))
    cola.agregar(Pedido(50, "cliente4"))

    # Imprimir el estado de la cola
    print("********* DUMP DE LA COLA *********")
    print(f"   Tamaño: {cola.tamaño()}")
    
    cola.imprimir_cola()
    
    print("******************************")