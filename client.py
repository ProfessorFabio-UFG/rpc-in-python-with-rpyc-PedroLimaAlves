import rpyc
from constRPYC import *  # Módulo com as constantes (porta, servidor, etc.)

class Client:
    conn = rpyc.connect(SERVER, PORT)  # Conecta ao servidor

    # Testa o método exposed_value da lista
    print("Valor inicial da lista:", conn.root.exposed_value())

    # Testa o método exposed_append
    conn.root.exposed_append(5)       
    conn.root.exposed_append(6)
    print("Lista após adicionar 5 e 6:", conn.root.exposed_value())

    # Testa as novas funções remotas
    print("Soma de 5 e 3:", conn.root.exposed_add(5, 3))  # Soma
    print("Subtração de 5 e 3:", conn.root.exposed_subtract(5, 3))  # Subtração
    print("Multiplicação de 5 e 3:", conn.root.exposed_multiply(5, 3))  # Multiplicação
    print("Divisão de 5 por 5:", conn.root.exposed_divide(5, 5))  # Divisão
    print("Divisão de 5 por 1:", conn.root.exposed_divide(5, 1))  # Testa divisão por zero
