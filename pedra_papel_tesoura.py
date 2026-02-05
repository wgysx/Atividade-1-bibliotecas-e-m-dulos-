import random

def jogo_jo_ken_po():
    """
    Simula o jogo Pedra, Papel e Tesoura (Jo Ken Po)
    Retorna uma jogada aleatória
    """
    opcoes = ["Pedra", "Papel", "Tesoura"]
    jogada = random.choice(opcoes)
    return jogada

if __name__ == "__main__":
    print("Jo Ken Po!")
    print(f"Musto escolheu: {jogo_jo_ken_po()}")