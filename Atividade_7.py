import whisper
import sys
from langchain_community.llms import Ollama

model = whisper.load_model("small")

# Faz a transcrição
result = model.transcribe("E:\Documentos\Estudos\If\I.A\Transcricao_aula7\Transcricao_whisper/videoplayback.mp4")
resultText = result['text'] # Armazena o texto transcrito aqui

# Instanciando o modelo Ollama
ollamaModel = Ollama(model="llama3.2:latest")

# --- MUDANÇA CRUCIAL AQUI, MEU DOG! ---
# Crie o prompt usando uma f-string ANTES de passar para o invoke()
ollamaPrompt = f"Retorne um resumo contendo os principais ponto-chaves do assunto: {resultText}"

# Agora, passe a string formatada para o invoke()
ollamaAnswer = ollamaModel.invoke(ollamaPrompt)
print(ollamaAnswer)

# Garante que a saída do terminal mostre caracteres especiais corretamente
sys.stdout.reconfigure(encoding='utf-8')