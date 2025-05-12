import rpyc
from constRPYC import *  # Módulo com constantes (porta, servidor, etc.)
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
    value = []

    # Função para adicionar um elemento à lista
    def exposed_append(self, data):
        self.value = self.value + [data]
        return self.value

    # Função para retornar a lista
    def exposed_value(self):
        return self.value

    # Novo procedimento remoto: Somar dois números
    def exposed_add(self, a, b):
        return a + b

    # Novo procedimento remoto: Subtrair dois números
    def exposed_subtract(self, a, b):
        return a - b

    # Novo procedimento remoto: Multiplicar dois números
    def exposed_multiply(self, a, b):
        return a * b

    # Novo procedimento remoto: Dividir dois números
    def exposed_divide(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero!"
        return a / b

if __name__ == "__main__":
    server = ThreadedServer(DBList(), port = PORT)  # Define a porta do servidor
    server.start()  # Inicia o servidor
