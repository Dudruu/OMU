from prettytable import PrettyTable  # Importa PrettyTable para exibir dados em tabelas

# Define a função y(x)
def y(x):
    return (8*x**3 - x - 13) / (x + 5)

# Define a função para verificar se um número é primo
def is_prime(n):
    if n <= 1:  # Checa se n é menor ou igual a 1
        return False
    if n <= 3:  # Checa se n é menor ou igual a 3
        return True
    if n % 2 == 0 or n % 3 == 0:  # Checa se n é divisível por 2 ou 3
        return False
    i = 5
    while i * i <= abs(n):  # Loop para verificar divisibilidade
        if abs(n) % i == 0 or abs(n) % (i + 2) == 0:
            return False
        i += 6
    return True

# Menu para o usuário escolher opções
print("Escolha uma opção:")
print("1. Usar divisores padrões")
print("2. Inserir dois valores para x e y")
print("3. Inserir um valor para x e obter o valor correspondente de y")
opcao = int(input())

if opcao == 1:
    divisores = [1, 2, 3, 4, 6, 7, 8, 9, 12, 14, 16, 18, 21, 24, 28, 36, 42, 48, 56, 63, 72, 84, 112, 126, 144, 168, 252, 336, 504, 1008]  # Lista de divisores de 1008

    # Adiciona os divisores negativos à lista
    divisores += [-d for d in divisores]

    solucoes = []  # Lista para armazenar soluções
    solucoes_negativas = []  # Lista para soluções com números negativos
    solucoes_primas = []  # Lista para soluções com números primos

    for d in divisores:
        x = d - 5
        yx = y(x)
        # Verifica se y(x) é um número inteiro
        if yx.is_integer():
            solucoes.append((x, yx))
            if x < 0 and yx < 0:
                solucoes_negativas.append((x, yx))
            if is_prime(x):
                solucoes_primas.append((x, yx))

    # Cria tabelas para exibir as soluções
    tabela_solucoes = PrettyTable(['x', 'y'])
    tabela_solucoes_negativas = PrettyTable(['x', 'y'])
    tabela_solucoes_primas = PrettyTable(['x', 'y'])

    # Adiciona as soluções às tabelas
    for solucao in solucoes:
        tabela_solucoes.add_row(solucao)
    for solucao in solucoes_negativas:
        tabela_solucoes_negativas.add_row(solucao)
    for solucao in solucoes_primas:
        tabela_solucoes_primas.add_row(solucao)

    # Imprime todas as soluções
    print("\nTodas as soluções:")
    print(tabela_solucoes)

    # Imprime o número de soluções
    print(f"\nNúmero total de soluções: {len(solucoes)}")

    # Imprime as soluções onde x e y são inteiros negativos
    print("\nSoluções onde x e y são inteiros negativos:")
    print(tabela_solucoes_negativas)

    # Imprime o número de soluções onde x e y são inteiros negativos
    print(f"\nNúmero de soluções onde x e y são inteiros negativos: {len(solucoes_negativas)}")

    # Imprime as soluções onde x é primo
    print("\nSoluções onde x é primo:")
    print(tabela_solucoes_primas)

    # Imprime o número de soluções onde x é primo
    print(f"\nNúmero de soluções onde x é primo: {len(solucoes_primas)}")

elif opcao == 2:
    # Solicita que o usuário insira dois valores para x e y
    x = int(input("Insira um valor para x: "))
    y_user = int(input("Insira um valor para y: "))
    yx = y(x)
    if yx.is_integer() and yx == y_user:
        print(f"A solução (x, y) = ({x}, {y_user}) é válida para a equação.")
    else:
        print(f"A solução (x, y) = ({x}, {y_user}) não é válida para a equação.")

elif opcao == 3:
    # Solicita que o usuário insira um valor para x
    x = int(input("Insira um valor para x: "))
    print(f"O valor de y para x = {x} é: {y(x)}")

else:
    print("Opção inválida.")
