# ==========================================
# PASSO 6: ENTRADA DE DADOS (GRAMÁTICA)
# ==========================================
def definir_gramatica_usuario():
    print("\n" + "="*50)
    print(" PASSO 6: DEFINIÇÃO DA GRAMÁTICA G = (N, T, P, S)")
    print("="*50)
    
    inicial = input("Qual o Símbolo Inicial (ex: S)? ").strip().upper()
    regras = {}
    
    print("\n[Digite as regras de produção. Digite 'SAIR' no Não-Terminal para finalizar]")
    while True:
        nao_terminal = input("\nNão-Terminal (ex: S, A, B): ").strip().upper()
        if nao_terminal == 'SAIR':
            break
            
        # Pede as regras separadas por vírgula
        entrada_regras = input(f"Regras para {nao_terminal} (separe por vírgula, use '-' para vazio): ")
        producoes = entrada_regras.split(',')
        
        # Monta o dicionário
        regras[nao_terminal] = {}
        for i, prod in enumerate(producoes):
            regras[nao_terminal][f"r{i+1}"] = prod.strip()
            
    print("\n[!] Gramática salva na memória com sucesso!")
    return {
        "inicial": inicial,
        "regras": regras,
    }

# 2. Adicione esta função de "Ponte" para gerar o formato solicitado
def formatar_para_processamento(dados_entrada):
    regras_brutas = dados_entrada['regras']
    v_g = set(regras_brutas.keys())
    t_g = set()
    p_g = {}

    for nt, producoes_dict in regras_brutas.items():
        lista_limpa = []
        for p in producoes_dict.values():
            valor = 'ε' if p == '-' else p
            lista_limpa.append(valor)
            for char in valor:
                if char.islower() and char != 'ε':
                    t_g.add(char)
        p_g[nt] = lista_limpa
    
    return v_g, t_g, p_g, dados_entrada['inicial']

#Verifica se a gramática é linear ou não
def verificar_tipo_gramatica(regras_gramaticais_P):
    print("-"*50)
    print("Verificação se a gramática é GL ou GLC:")
    for regras in regras_gramaticais_P.values():
        e_gramatica_linear = False
        for regra in regras:
            if regra == '-':
                continue
            else:
                regra_str = str(regra)
                cont = 0
                for char in regra_str:
                    if char.isupper():
                        cont += 1
                if cont > 1:
                   print(f"Regra: {regra_str} prova que é uma GLC")
                   break
                else: 
                    e_gramatica_linear = True
                cont = 0
    if e_gramatica_linear:
        print("\nResultado: Gramática Regular (GR)")
        return 'GR'
    else:
        print("\nResultado: Gramática Não Linear (GLC)")
        return 'GLC'  

# ==========================================
# PASSO 9: ÁRVORE DE DERIVAÇÃO (ERICK)
# ==========================================
def imprimir_arvore_visual(simbolo, lista_regras, prefixo="", ultimo=True, raiz=True):
    # funcao recursiva que desenha a arvore no terminal
    # condicao 1 -> imprime o no atual com os galhos corretos
    if raiz:
        print(simbolo)
    else:
        marcador = "└── " if ultimo else "├── "
        print(prefixo + marcador + simbolo)

    # condicao 2 -> se for uma letra maiusucla (variavel) e tivermos regras na memoria
    if simbolo.isupper() and len(lista_regras) > 0:
        # puxa a proxima regra que a varredura descobriu para usar
        # pop(0) por conta da derivacao a esquerda
        variavel, producao = lista_regras.pop(0)

        # condicao 3 -> calcula o espaco para os filhos do no
        if raiz:
            novo_prefixo = ""
        else:
            # se esse no for o ultimo filho o espaco dele é vazio
            # se ele ter irmao abaixo, desce uma linha reta
            novo_prefixo = prefixo + ("    " if ultimo else "│   " )

        # condicao 4 -> recursao para desenhar os fihos
        for i, char in enumerate(producao):
            filho_ultimo = (i == len(producao) - 1)
            imprimir_arvore_visual(char, lista_regras, novo_prefixo, filho_ultimo, False)

def gerar_arvore_derivacao(gramatica, palavra_alvo):
    print("\n" + "="*40)
    print(f"Arvore de derivacao para: '{palavra_alvo}'")
    print("="*40)

    inicial = gramatica["inicial"]
    regras = gramatica["regras"]

    # funcao recursiva que faz o backtracking 
    def derivar(forma_atual, passos_str, regras_usadas):
        # condicao 1 -> sucesso na palavra alvo, agora varredura
        if forma_atual == palavra_alvo:
            # agora retorna a lista de regras usadas
            return passos_str, regras_usadas
        
        # condicao 2 -> parada p evitar o loop infinito
        if len(forma_atual) > len(palavra_alvo):
            return None, None
        
        # condicao 3 -> encontrar o primeiro nao-terminal p/ substituir
        nao_terminal_alvo = None
        indice_substituicao = -1

        for i, char in enumerate(forma_atual):
            if char.isupper():
                nao_terminal_alvo = char
                indice_substituicao = i
                break
                
        # tem minuscula, mas nao é a palavra alvo
        if nao_terminal_alvo is None:
            return None, None
        
        # condicao 4 -> tentar aplicar as regras para o nao-terminal
        if nao_terminal_alvo in regras:
            for nome_regra, producao in regras[nao_terminal_alvo].items():
                # cria a nova string p substituir a letra maiuscula pela producao
                nova_forma = forma_atual[:indice_substituicao] + producao + forma_atual[indice_substituicao + 1:]
                
                # novo passo a passo com a flechinha =>
                novo_passos_str = passos_str + [f" => {nova_forma} (usando {nao_terminal_alvo} -> {producao})"]

                # guarda a regra que esta tentando usar ('S', 'aA')
                nova_regras_usadas = regras_usadas + [(nao_terminal_alvo, producao)]

                # entrando na recursao
                res_passos, res_regras = derivar(nova_forma, novo_passos_str, nova_regras_usadas)

                # se retornar caminho valido o sucesso vai pra cima
                if res_passos is not None:
                    return res_passos, res_regras
                    
        # se deu ruim em todas as regras
        return None, None
    
    # recursao comecando pelo simbolo incial S
    caminho_sucesso, regras_sucesso = derivar(inicial, [f" {inicial} (Simbolo Inicial)"], [])
    
    # exibir o resultado final
    if caminho_sucesso is not None:
        print("1. Palavra gerada com sucesso. Gerando passo a passo: \n")
        for passo in caminho_sucesso:
            print(passo)
        
        print("\n2. Arvore Visual Gerada")
        # chama a def de imprimir a arvore visual passando o simbolo inicial e copia das regras encontradas
        imprimir_arvore_visual(inicial, list(regras_sucesso))
    else:
        print(f"A palavra '{palavra_alvo}' Nao pode ser gerada por esta gramatica")
    print("-" * 40)


# 1. O programa pede a gramática primeiro
gramatica_criada = definir_gramatica_usuario()

#Verificação (Use a sua função existente)
tipo = verificar_tipo_gramatica(gramatica_criada['regras'])
    
# Transformação para o formato acadêmico que você pediu
v_g, t_g, p_g, s_g = formatar_para_processamento(gramatica_criada)
    
    # Agora envia para o código de processamento (Código 2)
    # Exemplo:
if tipo == "GR":
    print("\n[Executando processamento de Gramática Regular...]")
    
else:
    print("\n[Executando processamento de GLC...]")
    # simplificar_glc_detalhado(p_g, v_g, t_g)
    
# ==========================================
# EXECUÇÃO DIRETA DO ARQUIVO
# ==========================================
if __name__ == "__main__":
  
  while True:
    # 2. Pede a palavra que você quer testar
    palavra_teste = input("\nDigite a palavra para gerar a árvore de derivação: ").strip()
    
    # 3. Roda a sua função mágica da árvore
    gerar_arvore_derivacao(gramatica_criada, palavra_teste)

    resposta = input("Deseja verificar outra palavra? (s/n): ").strip().lower()

    if resposta == 'n':
        print("Encerrando o programa. Obrigado por usar!")
        break

    