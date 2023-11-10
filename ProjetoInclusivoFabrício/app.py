# Importando as bibliotecas necessárias do Flask
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from video_processor import extract_text_from_video  # Importando a função de processamento de vídeo
import os

app = Flask(__name__)

# Configuração da pasta de uploads
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Rota principal que renderiza o formulário de upload (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rota acionada quando um arquivo de vídeo é enviado através do formulário
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']  # Obtendo o arquivo enviado
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(video_path)  # Salvando o arquivo de vídeo na pasta de uploads
        text = extract_text_from_video(video_path)  # Processando o texto do vídeo

        # Renderizando a página de resultado com o texto extraído
        return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)  # Iniciando o aplicativo Flask em modo de depuração
