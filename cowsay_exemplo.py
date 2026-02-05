import cowsay

def usar_cowsay():
    """
    Exemplo de uso da biblioteca cowsay
    """
    print("=== Exemplo com Cow ===")
    cowsay.cow("Olá! Eu sou uma vaca falante!")
    
    print("\n=== Exemplo com Turtle ===")
    cowsay.turtle("Eu sou uma tartaruga!")
    
    print("\n=== Exemplo com Dragon ===")
    cowsay.dragon("ROAR! Eu sou um dragão!")
    
    print("\n=== Exemplo com Beavis ===")
    try:
        cowsay.beavis("huh huh huh, yeah!")
    except:
        print("Beavis não está disponível em todas as versões")

if __name__ == "__main__":
    usar_cowsay()