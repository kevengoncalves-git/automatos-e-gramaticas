# Trabalho Final de Teoria da Computação

Este repositório contém o desenvolvimento de um software capaz de processar Autômatos Finitos (Determinísticos e Não-Determinísticos) e Gramáticas (Regulares e Livres de Contexto). O foco do projeto é a demonstração detalhada e passo a passo de cada etapa de processamento conforme pedido pelo docente.

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

O Gemini disse
Aqui está o conteúdo formatado em Markdown, pronto para ser copiado e colado no seu arquivo README.md do GitHub.

Projeto de Desenvolvimento de Software - Teoria da Computação
Este projeto consiste em um software desenvolvido para a disciplina de Teoria da Computação, focado no processamento de Autômatos e Gramáticas. O sistema prioriza a demonstração detalhada de cada etapa do processamento (entradas → processamento → saídas) via console.
+2

2. Gramáticas (/gramaticas)
Contém scripts independentes para o processamento de gramáticas formais G=(N,T,P,S).
- Conversao_da_GR_em_AFD_e_Simplificacao_da_GLC.py: passos 7 e 8
Conversão de GR: Transforma Gramáticas Regulares em seus AFDs equivalentes.
Simplificação de GLC: Analisa Gramáticas Livres de Contexto e realiza a simplificação passo a passo para aproximá-la de uma Gramática Linear.

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

👥 Equipe
  --> Camille Vitória Vieira de Souza
  --> Erick Francys Portilho Paz
  --> Keven Kauê Gonçalves Pinto
