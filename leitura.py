while True:
    # 1. Menu Interativo (Estrutura Condicional)
    print("\n=== MENU DE JOGADORES ===")
    print("1 - Ver Jogadores Cadastrados")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Lista de Jogadores ---")
        # 2. Ler dados armazenados no arquivo TXT
        arquivo = open("jogadores.txt", "r")  # 'r' significa read (Ler)
        conteudo = arquivo.read()

        # 3. Exibir informações no terminal
        if conteudo == "":
            print("Nenhum jogador cadastrado ainda.")
        else:
            print(conteudo)

        arquivo.close()

    elif opcao == "2":
        print("Sindo do programa...")
        break
    else:
        print("X Opção inválida! Escolha 1 ou 2.")
































        