# 1. Abre o arquivo jogadores.txt para leitura
arquivo = open("jogadores.txt", "r", encoding="utf-8")
linhas = arquivo.readlines()
arquivo.close()

# 2. Inicializa as variáveis para a busca
maior_pontuacao = 0
melhor_jogador = ""

# 3. Percorre todas as linhas do arquivo
for linha in linhas:
    # Separa o nome da pontuação
    nome, pts = linha.strip().split(",")

    # Remove espaços extras
    nome = nome.strip()
    pts = pts.strip()

    # 4. Compara as pontuações
    if int(pts) > maior_pontuacao:
        maior_pontuacao = int(pts)
        melhor_jogador = nome

# 5. Exibe o resultado final no terminal
print(f'Melhor jogador: {melhor_jogador} com {maior_pontuacao} pontos')