from pytube import YouTube
import os
import tkinter as tk
from tkinter import filedialog

def download_audio():
    url = url_entry.get()
    destination = destination_entry.get() or '.'

    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()

        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'

        os.rename(out_file, new_file)

        result_label.config(text=f'{yt.title} foi baixado com sucesso.')
    except Exception as e:
        result_label.config(text=f'Ocorreu um erro: {str(e)}')

# Função para selecionar o diretório de destino
def select_destination_dir():
    directory = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, directory)

# Interface gráfica
root = tk.Tk()
root.title("YouTube Audio Downloader")

# Label e entrada para a URL
url_label = tk.Label(root, text="URL do YouTube:")
url_label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack()

# Label e entrada para o diretório de destino
destination_label = tk.Label(root, text="Diretório de Destino:")
destination_label.pack()

destination_entry = tk.Entry(root, width=40)
destination_entry.pack()

select_dir_button = tk.Button(root, text="Selecionar Diretório", command=select_destination_dir)
select_dir_button.pack()

# Botão para iniciar o download
download_button = tk.Button(root, text="Baixar Áudio", command=download_audio)
download_button.pack()

# Label para exibir o resultado
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
