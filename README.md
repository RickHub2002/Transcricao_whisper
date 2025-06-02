# Transcricao_whisper

Beleza, meu dog! Mandou a braba! Se o Bark tá dando perrengue demais, a gente foca no que tá rodando liso: Whisper + Ollama! É um pipeline brabo por si só!

Aqui está o README.md pra sua aplicação, formal, estudantil, com uns emojis e destaques pra deixar a parada top, focando no que realmente tá funfando:

🚀 Projeto de Análise de Mídia com IA: Transcrição e Sumarização Inteligente
Este projeto implementa um pipeline de processamento de mídia utilizando Inteligência Artificial para converter conteúdo de áudio/vídeo em texto e, posteriormente, extrair e sumarizar os pontos mais importantes. É uma ferramenta eficaz para análise rápida de conteúdo falado.

🎯 Objetivo do Projeto
O principal objetivo é desenvolver uma aplicação capaz de:

Transcrever o conteúdo de arquivos de áudio ou vídeo (.mp3, .mp4, etc.) utilizando o modelo Whisper da OpenAI. 🎙️
Extrair os pontos-chave e sumarizar o texto transcrito, empregando um Modelo de Linguagem Grande (LLM) hospedado localmente via Ollama (especificamente o llama3.2:latest). 🧠
🛠️ Tecnologias Envolvidas
Python 3.11.x: A linguagem de programação principal para o projeto.
OpenAI Whisper: Um modelo de IA para transcrição automática de fala, reconhecido por sua alta precisão.
Ollama: Uma plataforma que permite a execução e gestão de LLMs diretamente em sua máquina, garantindo processamento local e privado.
LangChain: Um framework que facilita a orquestração e a interação com os LLMs.
FFmpeg: Uma ferramenta externa essencial para manipulação de arquivos de áudio e vídeo, utilizada pelo Whisper para extrair o áudio dos vídeos.
⚙️ Instalação e Execução
Para configurar e executar o projeto em seu ambiente, siga os passos cuidadosamente:

1. Preparação do Ambiente Python
Certifique-se de ter o Python 3.11.x instalado em seu sistema. Durante o processo de instalação, é fundamental marcar a opção "Add Python to PATH" para garantir que os comandos Python sejam facilmente acessíveis pelo terminal.

2. Instalação do FFmpeg (Passo Crucial!)
O FFmpeg é uma dependência externa vital para que o Whisper possa processar arquivos de mídia como MP4.

Baixe uma build pré-compilada para Windows do FFmpeg no site oficial ffmpeg.org/download.html. Recomenda-se procurar por links para Gyan.dev ou BtbN/FFmpeg-Builds e selecionar um arquivo .zip ou .7z que contenha _build no nome (ex: ffmpeg-...-essentials_build.7z).
Após o download, extraia o conteúdo do arquivo para um diretório seguro e de fácil acesso (ex: C:\ffmpeg\).
Adicione o caminho completo da subpasta bin (onde se encontra o ffmpeg.exe) às variáveis de ambiente Path do seu sistema Windows.
Reinicie o computador após adicionar ao PATH para que as alterações sejam efetivadas em todo o sistema.
Para confirmar a instalação, abra um novo terminal e execute o comando ffmpeg -version. ✅
3. Configuração do Ollama
O Ollama é a plataforma que permite a execução local dos modelos de linguagem.

Baixe e instale o Ollama do site oficial: ollama.com/download.
Após a instalação, utilize o terminal para baixar o modelo llama3.2:latest, que será usado para a sumarização:
Bash

ollama pull llama3.2:latest
Verifique se o serviço Ollama está ativo e em execução em segundo plano (geralmente indicado por um ícone na bandeja do sistema).
4. Configuração do Ambiente Python e Dependências
É altamente recomendável utilizar um ambiente virtual para este projeto, a fim de isolar suas dependências e evitar conflitos com outras instalações Python.

No terminal, navegue até o diretório raiz do seu projeto.
Crie e ative um ambiente virtual:
Bash

python -m venv venv
.\venv\Scripts\activate  # Para usuários Windows (CMD/PowerShell)
Com o ambiente virtual ativado, instale as bibliotecas Python necessárias:
Bash

pip install openai-whisper
pip install langchain langchain-community langchain-core
pip install pydantic==1.10.13 # Versão específica para garantir compatibilidade com o LangChain
Nota: Se você possui uma GPU NVIDIA, para otimizar o desempenho do Whisper, é aconselhável instalar a versão do PyTorch com suporte a CUDA após a configuração do CUDA Toolkit e cuDNN.
5. Execução do Script Principal
Posicione seu arquivo de áudio ou vídeo (ex: videoplayback.mp4) no mesmo diretório do seu script Python (Atividade_7.py).

Atenção: Se algum diretório no caminho do seu arquivo contiver caracteres especiais (como ç ou ã), é essencial renomeá-lo para remover esses caracteres (ex: Transcricao_aula7 em vez de Transcrição_aula7). Isso evita erros de "arquivo não encontrado" pelo FFmpeg.

Abra o arquivo Atividade_7.py em seu editor de código e ajuste a variável AUDIO_VIDEO_PATH para o caminho exato do seu arquivo de entrada.

Execute o script a partir do terminal (com o ambiente virtual ativado):

Bash

python Atividade_7.py
Dica para Exibição de Caracteres Especiais: Se caracteres como ç ou ã aparecerem corrompidos na saída do seu terminal, execute chcp 65001 (no CMD) ou $OutputEncoding = [System.Text.Encoding]::UTF8; chcp 65001 (no PowerShell) antes de executar o script. 💡

⚠️ Observação Importante: Modelos e Espaço em Disco
Este projeto utiliza modelos de IA que requerem um volume considerável de armazenamento em disco.

O modelo Whisper "small" (configurado no código para otimização) ocupa aproximadamente 461 MB de espaço.
O modelo Ollama llama3.2:latest (para sumarização) ocupa cerca de 2.0 GB.
Certifique-se de que seu Disco Local C: (ou o disco onde o cache dos modelos está configurado via variáveis de ambiente como XDG_CACHE_HOME) possui espaço livre suficiente para o download e a descompressão desses modelos. A falta de espaço pode causar erros de "No space left on device", impedindo a execução do projeto. 💾

