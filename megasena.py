import random

def gerar_jogo_megasena():
    """
    Gera 6 números únicos para a MegaSena (1 a 60)
    """
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()  # Ordena os números
    return numeros

if __name__ == "__main__":
    print("Números da MegaSena:")
    jogo = gerar_jogo_megasena()
    print(" - ".join(f"{num:02d}" for num in jogo))