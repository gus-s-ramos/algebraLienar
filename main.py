# Pede ao usuário para inserir a primeira matriz
linhas1 = int(input("Digite o número de linhas da primeira matriz: "))
colunas1 = int(input("Digite o número de colunas da primeira matriz: "))

matriz1 = []
for i in range(linhas1):
    linha = []
    for j in range(colunas1):
        valor = int(input(f"Digite o valor da posição ({i+1}, {j+1}) da primeira matriz: "))
        linha.append(valor)
    matriz1.append(linha)

# Pede ao usuário para inserir a segunda matriz
linhas2 = int(input("Digite o número de linhas da segunda matriz: "))
colunas2 = int(input("Digite o número de colunas da segunda matriz: "))

matriz2 = []
for i in range(linhas2):
    linha = []
    for j in range(colunas2):
        valor = int(input(f"Digite o valor da posição ({i+1}, {j+1}) da segunda matriz: "))
        linha.append(valor)
    matriz2.append(linha)

# Pede ao usuário para escolher a operação
operacao = input("Digite a operação que deseja realizar entre as matrizes (+ para soma, * para multiplicação): ")

if operacao == "+":
    # Verifica se a soma entre as matrizes pode ser realizada
    if linhas1 != linhas2 or colunas1 != colunas2:
        print("A soma entre as matrizes não pode ser realizada.")
    else:
        # Cria uma matriz resultado vazia
        resultado = []
        for i in range(linhas1):
            linha = []
            for j in range(colunas1):
                linha.append(matriz1[i][j] + matriz2[i][j])
            resultado.append(linha)

        # Imprime o resultado
        print("Resultado da soma:")
        for linha in resultado:
            print(linha)
elif operacao == "*":
    # Verifica se a multiplicação entre as matrizes pode ser realizada
    if colunas1 != linhas2:
        print("A multiplicação entre as matrizes não pode ser realizada.")
    else:
        # Cria uma matriz resultado vazia
        resultado = []
        for i in range(linhas1):
            linha = []
            for j in range(colunas2):
                linha.append(0)
            resultado.append(linha)

        # Calcula o resultado da multiplicação
        for i in range(linhas1):
            for j in range(colunas2):
                for k in range(colunas1):
                    resultado[i][j] += matriz1[i][k] * matriz2[k][j]

        # Imprime o resultado
        print("Resultado da multiplicação:")
        for linha in resultado:
            print(linha)
else:
    print("Operação inválida. Digite + para soma ou * para multiplicação.")
