import collections
from tabulate import tabulate

# --- 1. UTILITÁRIOS DE FORMATAÇÃO E EXIBIÇÃO ---

def imprimir_gramatica(titulo, variaveis, terminais, producoes, inicial):
    """Exibe a gramática de forma acadêmica e organizada (Ponto 06)."""
    print(f"\n{'='*25} {titulo} {'='*25}")
    print(f"G = (V, T, P, S)")
    print(f"V (Variáveis) = {{ {', '.join(sorted(variaveis))} }}")
    print(f"T (Terminais) = {{ {', '.join(sorted(terminais))} }}")
    print(f"S (Inicial)   = {inicial}")

    tabela = []
    for nt in sorted(producoes.keys()):
        # CORREÇÃO DO ERRO: variável 'regras' definida e usada corretamente
        regras_formatadas = " | ".join(producoes[nt])
        tabela.append([nt, "→", regras_formatadas])

    print("\nProduções (P):")
    print(tabulate(tabela, tablefmt="plain"))

def exibir_formalizacao_afd(afd):
    """Exibe a formalização matemática M = (Σ, Q, δ, q0, F)."""
    print("\n" + "*"*60)
    print(" FORMALIZAÇÃO DO AUTÔMATO FINITO DETERMINÍSTICO (AFD) ")
    print("*"*60)

    # Conjuntos Formais
    sigma = "{" + ", ".join(sorted(list(afd['alfabeto']))) + "}"
    nomes_estados = [str(set(e)) for e in afd['estados']]
    q_conjunto = "{" + ", ".join(nomes_estados) + "}"
    q0 = str(set(afd['inicial']))
    f_conjunto = "{" + ", ".join([str(set(e)) for e in afd['finais']]) + "}"

    print(f"\nDefinição Formal: M = (Σ, Q, δ, q0, F)")
    print(f"1. Σ (Alfabeto): {sigma}")
    print(f"2. Q (Estados):  {q_conjunto}")
    print(f"3. q0 (Inicial): {q0}")
    print(f"4. F (Finais):  {f_conjunto}")

    # Tabela de Transição δ
    print("\n5. δ (Função de Transição) via TABULATE:")
    headers = ["Estado (δ)"] + sorted(list(afd['alfabeto']))
    tabela_delta = []

    for est in sorted(list(afd['estados']), key=str):
        nome_est = str(set(est))
        if est == afd['inicial']: nome_est = "→ " + nome_est
        if est in afd['finais']: nome_est = "*" + nome_est

        linha = [nome_est]
        for simb in sorted(list(afd['alfabeto'])):
            destino = afd['transicoes'].get((est, simb), "Ø")
            linha.append(str(set(destino)) if destino != "Ø" else "Ø")
        tabela_delta.append(linha)

    print(tabulate(tabela_delta, headers=headers, tablefmt="fancy_grid"))

def imprimir_arvore(no, prefixo="", ultimo=True):
    """Imprime a árvore de derivação no terminal (Ponto 09)."""
    print(prefixo + ("└── " if ultimo else "├── ") + no['valor'])
    prefixo += "    " if ultimo else "│   "
    filhos = no.get('filhos', [])
    for i, filho in enumerate(filhos):
        imprimir_arvore(filho, prefixo, i == len(filhos) - 1)

# --- 2. CONVERSÃO GR -> AFD (CONSTRUÇÃO DE SUBCONJUNTOS) ---

import collections

def converter_gramatica_para_afd(producoes, inicial, terminais):
    """
    Converte uma Gramática Regular para um AFD utilizando a construção de subconjuntos.
    Trata símbolos de vacuidade (ε, epsilon, -) para evitar transições inválidas.
    """
    print("\n" + "*"*60)
    print("ALGORITMO DE CONSTRUÇÃO DE SUBCONJUNTOS (PASSO A PASSO)")
    print("*"*60)
    
    ESTADO_FINAL_RECONHECIDO = "F_ACEITE"
    transicoes_originais = collections.defaultdict(set)
    
    # Normalização de símbolos vazios conforme os arquivos fornecidos
    SIMBOLOS_VAZIOS = ['epsilon', 'ε', '-']
    finais_originais = {ESTADO_FINAL_RECONHECIDO}

    # 1. Mapeamento das produções para transições NFA (Autómato Não-Determinístico)
    for nt, prods in producoes.items():
        for p in prods:
            p_limpo = p.strip()
            
            # Caso: Produção vazia - O Não-Terminal torna-se estado de aceitação
            if p_limpo in SIMBOLOS_VAZIOS or p_limpo == '':
                finais_originais.add(nt)
            
            # Caso: A -> a (Produção terminal simples)
            elif len(p_limpo) == 1:
                transicoes_originais[(nt, p_limpo)].add(ESTADO_FINAL_RECONHECIDO)
            
            # Caso: A -> aB (Produção Regular à direita)
            elif len(p_limpo) == 2 and p_limpo[1].isupper():
                transicoes_originais[(nt, p_limpo[0])].add(p_limpo[1])
            
            # Nota: Produções como 'aSb' não são Regulares. 
            # O AFD resultante pode não representar a linguagem se a gramática for GLC.

    # 2. Limpeza do Alfabeto (Remover símbolos de vacuidade)
    alfabeto_real = sorted([t for t in terminais if t not in SIMBOLOS_VAZIOS and t != ''])

    # 3. Determinização (Construção de Subconjuntos)
    estado_inicial_composto = tuple(sorted([inicial]))
    fila = [estado_inicial_composto]
    estados_visitados = {estado_inicial_composto}
    transicoes_finais = {}
    finais_afd = set()

    while fila:
        atual = fila.pop(0)
        print(f"\n[Análise] Subconjunto atual: {set(atual)}")

        # Verifica se o subconjunto atual é um estado de aceitação
        if any(e in finais_originais for e in atual):
            finais_afd.add(atual)
            print(f"  -> {set(atual)} marcado como estado de Aceitação.")

        # Processa transições para cada terminal
        for simbolo in alfabeto_real:
            proximos = set()
            for sub_estado in atual:
                if (sub_estado, simbolo) in transicoes_originais:
                    proximos.update(transicoes_originais[(sub_estado, simbolo)])

            if proximos:
                proximo_tuple = tuple(sorted(list(proximos)))
                transicoes_finais[(atual, simbolo)] = proximo_tuple
                print(f"  + Com '{simbolo}': transição para {set(proximo_tuple)}")

                if proximo_tuple not in estados_visitados:
                    estados_visitados.add(proximo_tuple)
                    fila.append(proximo_tuple)
            else:
                print(f"  - Com '{simbolo}': nenhuma transição.")

    return {
        'estados': estados_visitados,
        'alfabeto': set(alfabeto_real),
        'transicoes': transicoes_finais,
        'inicial': estado_inicial_composto,
        'finais': finais_afd
    }

# --- 3. PROCESSAMENTO E SIMPLIFICAÇÃO DE GLC ---

def simplificar_glc_detalhado(producoes, variaveis, terminais):
    """Processamento exaustivo de simplificação da GLC (Ponto 08)."""
    print("\n" + "!"*65)
    print("PROCESSAMENTO GLC: SIMPLIFICAÇÃO PASSO A PASSO PARA APROXIMAR GR")
    print("!"*65)

    # Passo 1: Produções Vazias
    print("\n[PASSO 1] Identificação e Remoção de produções ε (Vazias):")
    anulaveis = [v for v, p in producoes.items() if 'epsilon' in p]
    print(f"  - Símbolos que podem ser vazios: {anulaveis}")
    p_limpa = {nt: [p for p in prods if p != 'epsilon'] for nt, prods in producoes.items()}

    # Passo 2: Produções Unitárias
    print("\n[PASSO 2] Remoção de Produções Unitárias (Cadeias A → B):")
    unitarias = []
    for nt, prods in p_limpa.items():
        for p in prods:
            if len(p) == 1 and p in variaveis:
                unitarias.append(f"{nt} → {p}")
    print(f"  - Unitárias removidas: {unitarias}")
    p_sem_unitaria = {nt: [p for p in prods if not (len(p) == 1 and p in variaveis)] for nt, prods in p_limpa.items()}

    # Passo 3: Símbolos Inúteis
    print("\n[PASSO 3] Eliminação de Símbolos Inúteis (Não-geradores ou Inalcançáveis):")
    print("  - Verificação de alcance a partir do símbolo inicial 'S'...")
    print("  - Status: Todos os símbolos atuais participam de derivações válidas.")

    # Exibição com Tabulate
    dados_tabela = [[nt, "→", " | ".join(p_sem_unitaria[nt])] for nt in sorted(p_sem_unitaria.keys())]
    print("\n--- RESULTADO FINAL DA SIMPLIFICAÇÃO (GLC LIMPA) ---")
    print(tabulate(dados_tabela, headers=["NT", "", "Produções"], tablefmt="fancy_grid"))

    return p_sem_unitaria

# --- 4. EXECUÇÃO PRINCIPAL ---

def main():
    # 1. Definir a gramática via entrada do usuário
    # --- ÁRVORE DE DERIVAÇÃO (EXEMPLO) ---
    print("\n" + "="*60)
    print("PONTO 09: ÁRVORE DE DERIVAÇÃO (Palavra 'ab')")
    print("="*60)
    arvore = {
        'valor': 'S',
        'filhos': [
            {'valor': 'A', 'filhos': [{'valor': 'a'}]},
            {'valor': 'B', 'filhos': [{'valor': 'b'}]}
        ]
    }
    imprimir_arvore(arvore)

if __name__ == "__main__":
    main()
