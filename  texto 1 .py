# 1. Pede o nome e a pontuação do jogador usando input()
nome = input("Digite o nome do jogador: ")
pontuacao = input("Digite a pontuação do jogador: ")

# 2. Abre o arquivo 'jogadores.txt' no modo 'a' (append)
arquivo = open("jogadores.txt", "a")

# 3. Salva no arquivo usando write() com concatenação (+)
# O '\n' serve para pular uma linha para o próximo jogador
arquivo.write(nome + "," + pontuacao + "\n")

# 4. Fecha o arquivo usando close() como o slide pediu
arquivo.close()

print("Jogador salvo com sucesso!")



# 1. Abre o arquivo jogadores.txt para leitura
arquivo = open("jogadores.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

# 2. Inicializa as variáveis para a busca
maior_pontuacao = 0
melhor_jogador = ""

# 3. Avança de 2 em 2 linhas (uma linha é o nome, a próxima é a pontuação)
for i in range(0, len(linhas), 2):
    nome = linhas[i].strip()
    pts = linhas[i+1].strip()

    # Compara as pontuações diretamente sem precisar de split
    if int(pts) > maior_pontuacao:
        maior_pontuacao = int(pts)
        melhor_jogador = nome

# 4. Exibe o resultado final no terminal
print(f'Melhor jogador: {melhor_jogador} com {maior_pontuacao} pontos')

print ("jogador salvo com sucesso")

# 1. Abre o arquivo jogadores.txt para leitura
with open("jogadores.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# 2. Inicializa as variáveis para a busca
maior_pontuacao = 0
melhor_jogador = ""

# 1. Abre o arquivo jogadores.txt de forma segura
with open("jogadores.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# 2. Inicializa as variáveis para a busca
maior_pontuacao = 0
melhor_jogador = ""

# 3. Avança de 2 em 2 linhas (uma linha é o nome, a próxima é a pontuação)
for i in range(0, len(linhas), 2):
    nome = linhas[i].strip()
    pts = linhas[i+1].strip()

    # Compara as pontuações convertendo para inteiro
    if int(pts) > maior_pontuacao:
        maior_pontuacao = int(pts)
        melhor_jogador = nome  # CORREÇÃO: Atualiza o nome do melhor jogador

# Opcional: Exibe o resultado final encontrado
print(f"O melhor jogador é {melhor_jogador} com {maior_pontuacao} pontos.")


