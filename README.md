# Trabalho Final de Teoria da Computação - Autômatos e Gramáticas

Este repositório contém o desenvolvimento de um software capaz de processar Autômatos Finitos (Determinísticos e Não-Determinísticos) e Gramáticas Formais (Regulares e Livres de Contexto). 
O software foi desenvolvido em **Python**
O foco do projeto é a demonstração detalhada e passo a passo de cada etapa de processamento, conforme solicitado pelo docente.

👥 Equipe/Desenvolvedores
  --> Camille Vitória Vieira de Souza
  --> Erick Francys Portilho Paz
  --> Keven Kauê Gonçalves Pinto

# Objetivo do Projeto
• Definir um autômatos (ANFD e AFD) a partir da entrada do usuário
• Minimizar um AFD
• Validar palavras nos autômatos
• Definir uma gramática qualquer
• Gerar árvores de derivação
• Gerar pseudocódigos do reconhecedor

# Autômatos Finitos
São formalizados por uma determinada Máquina de Estados Finitos (MEF):
--> **M = (Q,Σ,δ,q0,F)**

Onde:
• Q: Conjunto de estados
• Σ: alfabeto inserido
• δ: função de transição do autômato
• q₀: estado inicial
• F: conjunto de estados finais

# Gramáticas Formais
A Gramática Regular (GR) e Gramática Livre de Contexto (GLC) também são implementadas pelo projeto.
A formalização de uma determinada gramática pode ser definida como:
--> **G =(V,Σ,P,S)**

Sendo: 
• V: variáveis (não-terminais)
• Σ: terminais
• P: conjunto de produções
• S: símbolo inicial

# Estrutura do Projeto
1. Autômatos (/automatos)
Contém a implementação de Máquinas de Estados Finitos requisitados do passo 1 ao 5.
menu_automato.py: Contém as funções de interface e suporte que devem ser importadas. 
automato.py: Arquivo principal que executa a lógica de estados (necessita importar menu_automato).

Funcionalidades inclusas:
Definição de AFD
Conversão AFND para AFD
Minimização de AFD
Validação de Palavras

2. Gramáticas (/gramaticas)
Contém scripts independentes para o processamento de gramáticas formais G=(N,T,P,S).
- Conversao_da_GR_em_AFD_e_Simplificacao_da_GLC.py: passos 7 e 8
Conversão de GR: Transforma Gramáticas Regulares em seus AFDs equivalentes.
Simplificação de GLC: Analisa Gramáticas Livres de Contexto e realiza a simplificação, passo a passo, para aproximá-las de uma Gramática Linear.

- gerando_arvore.py: passos 6 e 9
Classificação: Identifica se a gramática é Regular (GR) ou Livre de Contexto (GLC).
Árvore de Derivação: Gera a árvore para uma palavra w específica.
Pseudocódigo: Gera o código do reconhecedor baseado na gramática fornecida.

- pseudocodigo_do_reconhecedor.py: passo 10
  Gera o Pseudo-código do reconhecedor da linguagem.

# Como Executar

Linguagem: Certifique-se de ter o ambiente da linguagem Python instalado

# Execução:

Para Autômatos: Execute o arquivo automato.py dentro da pasta /automatos.

Para Gramáticas: Escolha um dos dois arquivos na pasta /gramaticas e execute-o de forma independente.

# Interface: O software funciona via console, exibindo o passo a passo de cada requisito solicitado.
