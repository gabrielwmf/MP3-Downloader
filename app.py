from flask import Flask, render_template, request, jsonify, send_file
from utils import is_valid_youtube_link
from downloader import downloader
import os

app = Flask(__name__)

# Caminho da pasta temporária
TMP_SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")

# Garantir que a pasta temporária existe
if not os.path.exists(TMP_SAVE_PATH):
   os.makedirs(TMP_SAVE_PATH)

# Rota principal para renderizar o HTML
@app.route("/")
def home():
   return render_template("index.html")

# Rota para processar o download via formulário
@app.route("/download", methods=["POST"])
def process_download():
   data = request.form
   link = data.get("link")

   # Verificar link
   if not is_valid_youtube_link(link):
      return jsonify({"error": "O link fornecido não é válido."}), 400

   try:
      # Fazer o download
      file_name = downloader(link, TMP_SAVE_PATH)

      # Retornar link para o usuário solicitar o download
      return jsonify({"message": "Download concluído!", "download_url": f"/tmp/{file_name}.mp3", "filename": f"{file_name}.mp3"}), 200
   except Exception as e:
      return jsonify({"error": str(e)}), 500

# Rota para servir o arquivo MP3 temporário e excluí-lo após o download
@app.route("/tmp/<filename>")
def serve_and_delete_file(filename):
   file_path = os.path.join(TMP_SAVE_PATH, filename)

   if not os.path.exists(file_path):
      return jsonify({"error": "Arquivo não encontrado."}), 404

   # Enviar o arquivo e programar exclusão
   try:
      response = send_file(file_path, as_attachment=True)
      os.remove(file_path)  # Excluir após envio
      return response
   except Exception as e:
      return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
   app.run(host="10.0.0.104", port=3000)