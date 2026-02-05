import calculadora

def main():
    print("=== CALCULADORA ===")
    
    # Usando a função soma da calculadora
    resultado_soma = calculadora.soma(10, 5)
    print(f"10 + 5 = {resultado_soma}")
    
    # Usando a função subtração da calculadora
    resultado_subtracao = calculadora.subtracao(10, 5)
    print(f"10 - 5 = {resultado_subtracao}")
    
    # Usando operações extras
    resultado_multi = calculadora.multiplicacao(10, 5)
    print(f"10 × 5 = {resultado_multi}")
    
    resultado_div = calculadora.divisao(10, 5)
    print(f"10 ÷ 5 = {resultado_div}")

if __name__ == "__main__":
    main()