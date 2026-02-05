import cowsay

def desenho_simples_garantido():
    """
    Versão super simples que não corta no terminal
    """
    
    desenho_mini = r"""
      ____  
     /    \ 
    |Sabor |
    |Python|
     \____/ 
      \  /  
       \/   
    """
    
    print("\n" + "=" * 40)
    print("SABOR PYTHON - MINI")
    print("=" * 40)
    
    cowsay.draw("Delicioso!", desenho_mini)

def desenho_apenas_texto():
    """
    Apenas mostra texto ASCII sem usar cowsay.draw()
    """
    print("\n" + "=" * 40)
    print("SABOR PYTHON - TEXTO DIRETO")
    print("=" * 40)
    
    print(r"""
    ┌──────────────────────┐
    │   SABOR  PYTHON      │
    └──────────────────────┘
         \   
          \  
           \ 
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
    """)

if __name__ == "__main__":
    # Escolha uma das opções:
    
    # Opção 1: Mini desenho
    desenho_simples_garantido()
    
    # Opção 2: Texto direto (nunca corta)
    desenho_apenas_texto()