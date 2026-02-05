def soma(a, b):
    """Retorna a soma de dois números"""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de dois números"""
    return a - b

def multiplicacao(a, b):
    """Operação extra: multiplicação"""
    return a * b

def divisao(a, b):
    """Operação extra: divisão"""
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"