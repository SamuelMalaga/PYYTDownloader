from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
import os

def convert_audio(input_path, output_path, sample_width, bitrate, sample_rate):
    # Aumentando os parâmetros de análise do ffmpeg
    parameters = ["-analyzeduration", "1000000", "-probesize", "1000000"]

    try:
        audio = AudioSegment.from_file(input_path, format="mp4", parameters=parameters)

        # Configurando os parâmetros desejados
        audio = audio.set_sample_width(sample_width)
        audio = audio.set_frame_rate(sample_rate)
        audio = audio.set_channels(1)  # Configura para mono (1 canal) para 16-bit linear

        # Convertendo para o formato desejado
        audio.export(output_path, format="mp3", bitrate=f"{bitrate}k")

        print(f'Conversão concluída: {output_path}')
    except CouldntDecodeError as e:
        print(f"Erro na decodificação: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Diretório de entrada e saída
input_directory = "C:/Users/SamuelMendesMalaga/Documents/PYYTDownloader/PYYTDownloader/input"
output_directory = "C:/Users/SamuelMendesMalaga/Documents/PYYTDownloader/PYYTDownloader/output"


# Iterando sobre os arquivos na pasta de entrada
for filename in os.listdir(input_directory):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_directory, filename)

        # Criando um nome de arquivo de saída com base nas configurações desejadas
        output_file = f"{os.path.splitext(filename)[0]}_converted.mp3"
        output_path = os.path.join(output_directory, output_file)

        # Configurando os parâmetros de conversão desejados
        sample_width = 2  # 16-bit linear
        bitrate = 128     # Escolha a taxa de bits desejada (64 / 96 / 128 / 160 / 192 / 224 / 256 / 320)
        sample_rate = 44100  # Escolha a taxa de amostragem desejada

        # Convertendo o arquivo
        convert_audio(input_path, output_path, sample_width, bitrate, sample_rate)
