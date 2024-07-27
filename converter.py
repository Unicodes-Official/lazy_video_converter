# converter.py
from moviepy.editor import VideoFileClip

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
