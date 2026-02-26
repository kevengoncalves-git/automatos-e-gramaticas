def gerar_pseudocodigo_reconhecer(gramatica):
    print("\n" + "=" * 60)
    print(" GERADOR DE PSEUDOCÓDIGO DO RECONHECEDOR ".center(60, "="))
    print("=" * 60 + "\n")

    regras = gramatica["regras"]

    estado_inicial = gramatica["inicial"]

    print("=" * 60)
    print(" FUNÇÃO PRINCIPAL ".center(60, "="))
    print("=" * 60)

    print("\nfuncao principal():")
    print("    inicializar_leitura_da_palavra()")
    print(f"    chamar_{estado_inicial}()")
    print("    se fim_da_palavra():")
    print("        retornar SUCESSO()")
    print("    senão:")
    print("        retornar ERRO()")

    print("\n" + "=" * 60)
    print(" FUNÇÕES DOS NÃO-TERMINAIS ".center(60, "="))
    print("=" * 60)

    for nao_terminal, dict_producoes in regras.items():

        print("\n" + "=" * 60)
        print(f" NÃO-TERMINAL: {nao_terminal} ".center(60, "="))
        print("=" * 60)

        print(f"\nfuncao chamar_{nao_terminal}():")
        print("    cabeca = ler_simbolo_atual()")
        print("    escolha (cabeca):")

        for nome_da_regra, producao in dict_producoes.items():
            primeiro_simbolo = producao[0]

            print(f"\n        caso '{primeiro_simbolo}':  // {nao_terminal} → {producao}")

            for simbolo in producao:
                if simbolo.islower():
                    print(f"            casar('{simbolo}')")
                elif simbolo.isupper():
                    print(f"            chamar_{simbolo}()")

        print("\n        padrão:")
        print("            retornar ERRO_DE_SINTAXE")

    print("\n" + "=" * 60)
    print(" FIM DA GERAÇÃO ".center(60, "="))
    print("=" * 60 + "\n")

# simular codigo keven
gramatica_teste = {
    "inicial": "S",
    "regras": {
        "S": {"r1": "aA", "r2": "b"},
        "A": {"r1": "aS", "r2": "b"}
    }
}

gerar_pseudocodigo_reconhecer(gramatica_teste)