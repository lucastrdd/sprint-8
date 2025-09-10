Projeto 4 – Chatbot Jurídico com RAG e AWS Bedrock

Sprint 7 e 8 – Scholarship Compass UOL – Formação em Inteligência Artificial para AWS
Visão Geral

Este projeto consiste na implementação de um chatbot jurídico utilizando a arquitetura RAG (Retrieval-Augmented Generation).
O sistema realiza consultas em uma base de documentos jurídicos armazenada no Amazon S3, gera embeddings com Amazon Bedrock, indexa com ChromaDB e expõe a interface de interação via Telegram.

Toda a orquestração é feita a partir de uma instância EC2 com Docker, utilizando LangChain para o fluxo RAG e python-telegram-bot para a interface com o usuário.
 Arquitetura

Fluxo principal:

    Usuários enviam mensagens ao chatbot pelo Telegram

    A aplicação na EC2 (rodando em Docker) processa a requisição utilizando:

        Leitura de documentos jurídicos armazenados no S3 (bucket: chatbot-lucas-dataset-202509)

        Criação de embeddings utilizando Amazon Bedrock (modelos Titan Embeddings v2)

        Indexação dos embeddings no ChromaDB para recuperação eficiente

        Execução do mecanismo de RAG com LangChain

    A resposta é enviada de volta ao usuário via Telegram



bot -  @lucas_squad6_assistente_bot
