# Importando as bibliotecas necessárias
from moviepy.editor import VideoFileClip  # Biblioteca para manipulação de vídeos
import speech_recognition as sr  # Biblioteca para reconhecimento de fala

# Função para extrair texto de um vídeo
def extract_text_from_video(video_path):
    try:
        clip = VideoFileClip(video_path)  # Carregando o arquivo de vídeo

        # Convertendo o áudio do vídeo para um arquivo WAV temporário
        clip.audio.write_audiofile("temp_audio.wav")

        recognizer = sr.Recognizer()  # Inicializando o reconhecedor de fala
        with sr.AudioFile("temp_audio.wav") as source:
            # Gravando o áudio para análise
            audio_data = recognizer.record(source)

            try:
                # Realizando o reconhecimento de fala usando o Google Speech Recognition
                text = recognizer.recognize_google(audio_data, language="pt-BR")
                print("Texto extraído do vídeo:", text)
                return text
            except sr.UnknownValueError:
                # Caso não seja possível entender o áudio do vídeo
                print("Não foi possível entender o áudio do vídeo.")
                return None
            except sr.RequestError as e:
                # Lidando com erros ao solicitar resultados do serviço de reconhecimento
                print(f"Não foi possível solicitar resultados do serviço de reconhecimento; {e}")
                return None
    except Exception as e:
        # Lidando com erros genéricos ao processar o vídeo
        print(f"Erro ao processar o vídeo: {e}")
        return None
