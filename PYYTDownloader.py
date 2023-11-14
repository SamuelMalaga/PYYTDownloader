from pytube import YouTube
import os
import sys

# Verifica se um argumento (URL) foi fornecido
if len(sys.argv) < 2:
    print("Por favor, forneça o URL como argumento.")
    sys.exit(1)

# Obtém o URL a partir do argumento de linha de comando
url = sys.argv[1]

try:
    video = YouTube(url)
    print('Title:', video.title)
    print('Downloading.....')

    out_path = video.streams.filter(only_audio=True).first().download()
    new_name = os.path.splitext(out_path)

    # Renomeia o arquivo para ter a extensão .mp3
    os.rename(out_path, new_name[0] + '.mp3')

    print('Done.....')
except Exception as e:
    print(f"Ocorreu um erro: {e}")
