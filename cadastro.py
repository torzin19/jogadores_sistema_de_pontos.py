# ==============================================================================
# 1. FUNÇÕES DE PERSISTÊNCIA E LÓGICA
# ==============================================================================

def salvar_jogador(nome, pontuacao):
    """Grava o nome em uma linha e a pontuação na linha seguinte."""
    # Garante que não salve valores vazios
    if not nome.strip() or not pontuacao.strip():
        print("❌ Erro: Nome ou pontuação não podem ser vazios.\n")
        return
        
    with open("jogadores.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome.strip()}\n{pontuacao.strip()}\n")
    print("▶ Jogador salvo com sucesso!\n")


def buscar_melhor_jogador():
    """Lê o arquivo tratando possíveis quebras de linha e erros de índice."""
    try:
        with open("jogadores.txt", "r", encoding="utf-8") as arquivo:
            # Lê todas as linhas e remove linhas puramente vazias do final/meio
            linhas = [linha.strip() for linha in arquivo.readlines() if linha.strip()]
    except FileNotFoundError:
        print("❌ Nenhum jogador cadastrado ainda (arquivo não encontrado).\n")
        return

    if not linhas:
        print("❌ O arquivo de jogadores está vazio.\n")
        return

    maior_pontuacao = -1  # Começa em -1 para aceitar pontuações de 0 para cima
    melhor_jogador = ""

    # Avança de 2 em 2 dentro da lista limpa
    for i in range(0, len(linhas), 2):
        # Verifica se existe a linha do par (pontuação) correspondente
        if i + 1 < len(linhas):
            nome = linhas[i]
            pts_str = list(linhas)[i+1]

            # Try/Except interno: se os pontos não forem número, não trava o loop
            try:
                pts = int(pts_str)
                if pts > maior_pontuacao:
                    maior_pontuacao = pts
                    melhor_jogador = nome
            except ValueError:
                # Ignora linhas corrompidas que não possuem números válidos nos pontos
                continue

    # Exibe o resultado final de forma segura
    if melhor_jogador:
        print(f"🏆 Melhor jogador: {melhor_jogador} com {maior_pontuacao} pontos!\n")
    else:
        print("❌ Nenhum dado válido de pontuação foi encontrado no arquivo.\n")


# ==============================================================================
# 2. FLUXO PRINCIPAL DO PROGRAMA (MENU)
# ==============================================================================

def menu():
    while True:
        print("=== SISTEMA DE JOGADORES ===")
        print("1 - Cadastrar Novo Jogador")
        print("2 - Ver Melhor Jogador")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        print()  # Salto de linha estético

        if opcao == "1":
            nome = input("Digite o nome do jogador: ")
            
            # Validação para garantir que a pontuação seja apenas números
            while True:
                pontuacao = input("Digite a pontuação inicial: ").strip()
                if pontuacao.isdigit():
                    break
                print("❌ Erro: A pontuação deve conter apenas números. Tente novamente.")

            salvar_jogador(nome, pontuacao)

        elif opcao == "2":
            buscar_melhor_jogador()

        elif opcao == "3":
            print("Saindo do programa. Até logo!")
            break
            
        else:
            print("❌ Opção inválida! Tente novamente.\n")


# Executa o programa
if __name__ == "__main__":
    menu()





























