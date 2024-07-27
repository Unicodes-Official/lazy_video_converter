import os
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import *

def convert_to_mp3(input_file, output_file):
    print(f"Inizio della conversione del file {input_file} in MP3.")
    try:
        print("Caricamento del file video...")
        video = VideoFileClip(input_file)
        print("Estrazione della traccia audio...")
        audio = video.audio
        print(f"Scrittura del file audio in {output_file}...")
        audio.write_audiofile(output_file, codec='mp3')
        print("Chiusura del file video e audio...")
        video.close()
        audio.close()
        print(f"Conversione completata. File salvato in: {output_file}")
    except Exception as e:
        print(f"Si è verificato un errore durante la conversione: {str(e)}")

def select_file():
    print("Apertura finestra di dialogo per la selezione del file...")
    file_path = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)
    update_output_entry(file_path)
    print(f"File selezionato: {file_path}")

def update_output_entry(input_file):
    print("Aggiornamento del campo di output...")
    filename = os.path.basename(input_file)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}.mp3"
    entry_output.delete(0, tk.END)
    entry_output.insert(0, output_filename)
    print(f"Nome del file di output impostato su: {output_filename}")

def select_folder():
    print("Apertura finestra di dialogo per la selezione della cartella...")
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folder_path)
    print(f"Cartella selezionata: {folder_path}")

def convert():
    input_file = entry_file.get()
    output_folder = entry_folder.get()
    output_file = os.path.join(output_folder, entry_output.get())
    print("Controllo dei campi input...")
    
    if input_file and output_folder:
        print(f"Avvio della conversione del file {input_file} in {output_file}...")
        convert_to_mp3(input_file, output_file)
    else:
        print("Per favore, seleziona un file di input e una cartella di output.")

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Convertitore Video to MP3")

label_file = tk.Label(root, text="Seleziona il file video:")
label_file.pack()

entry_file = tk.Entry(root, width=50)
entry_file.pack()

button_browse_file = tk.Button(root, text="Sfoglia", command=select_file)
button_browse_file.pack()

label_output = tk.Label(root, text="Nome del file di output (con estensione .mp3):")
label_output.pack()

entry_output = tk.Entry(root, width=50)
entry_output.pack()

label_folder = tk.Label(root, text="Seleziona la cartella di destinazione:")
label_folder.pack()

entry_folder = tk.Entry(root, width=50)
entry_folder.pack()

button_browse_folder = tk.Button(root, text="Sfoglia", command=select_folder)
button_browse_folder.pack()

button_convert = tk.Button(root, text="Converti", command=convert)
button_convert.pack()

root.mainloop()
