# utils.py
import os
import tkinter as tk
from tkinter import filedialog

def select_file(entry_file, update_output_entry):
    print("Apertura finestra di dialogo per la selezione del file...")
    file_path = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)
    update_output_entry(file_path)
    print(f"File selezionato: {file_path}")

def update_output_entry(entry_output, input_file):
    print("Aggiornamento del campo di output...")
    filename = os.path.basename(input_file)
    name, ext = os.path.splitext(filename)
    output_filename = f"{name}.mp3"
    entry_output.delete(0, tk.END)
    entry_output.insert(0, output_filename)
    print(f"Nome del file di output impostato su: {output_filename}")

def select_folder(entry_folder):
    print("Apertura finestra di dialogo per la selezione della cartella...")
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folder_path)
    print(f"Cartella selezionata: {folder_path}")
