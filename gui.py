# gui.py
import os
import tkinter as tk
from converter import convert_to_mp3
from utils import select_file, select_folder, update_output_entry

def convert(entry_file, entry_folder, entry_output):
    input_file = entry_file.get()
    output_folder = entry_folder.get()
    output_file = os.path.join(output_folder, entry_output.get())
    print("Controllo dei campi input...")
    
    if input_file and output_folder:
        print(f"Avvio della conversione del file {input_file} in {output_file}...")
        convert_to_mp3(input_file, output_file)
    else:
        print("Per favore, seleziona un file di input e una cartella di output.")

def create_gui():
    root = tk.Tk()
    root.title("Convertitore Video to MP3")

    label_file = tk.Label(root, text="Seleziona il file video:")
    label_file.pack()

    entry_file = tk.Entry(root, width=50)
    entry_file.pack()

    button_browse_file = tk.Button(root, text="Sfoglia", command=lambda: select_file(entry_file, lambda path: update_output_entry(entry_output, path)))
    button_browse_file.pack()

    label_output = tk.Label(root, text="Nome del file di output (con estensione .mp3):")
    label_output.pack()

    entry_output = tk.Entry(root, width=50)
    entry_output.pack()

    label_folder = tk.Label(root, text="Seleziona la cartella di destinazione:")
    label_folder.pack()

    entry_folder = tk.Entry(root, width=50)
    entry_folder.pack()

    button_browse_folder = tk.Button(root, text="Sfoglia", command=lambda: select_folder(entry_folder))
    button_browse_folder.pack()

    button_convert = tk.Button(root, text="Converti", command=lambda: convert(entry_file, entry_folder, entry_output))
    button_convert.pack()

    root.mainloop()
