def separar_pares_impares(valores):
    pares = []
    impares = []
    soma_pares = 0
    soma_impares = 0
    
    for valor in valores:
        if valor % 2 == 0:
            pares.append(valor)
            soma_pares += valor
        else:
            impares.append(valor)
            soma_impares += valor
    
    return pares, tuple(impares), len(pares), len(impares), soma_pares, soma_impares

def main():
    valores = []
    
    print("Digite 10 valores:")
    for i in range(10):
        valor = int(input(f"Digite o {i+1}º valor: "))
        valores.append(valor)
    
    pares, impares, qtde_pares, qtde_impares, soma_pares, soma_impares = separar_pares_impares(valores)
    
    print("\nNúmeros pares:", pares)
    print("Números ímpares:", impares)
    print("Quantidade de números pares:", qtde_pares)
    print("Quantidade de números ímpares:", qtde_impares)
    print("Soma de números pares:", soma_pares)
    print("Soma de números ímpares:", soma_impares)

if __name__ == "__main__":
    main()