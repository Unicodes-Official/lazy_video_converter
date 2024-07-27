
# Video to MP3 Converter

Questo progetto è un semplice convertitore di video in MP3 basato su Python. Utilizza `moviepy` per estrarre la traccia audio dai file video e `tkinter` per fornire una semplice interfaccia grafica.

## Struttura del Progetto

```
video_to_mp3_converter/
├── main.py
├── converter.py
├── gui.py
├── utils.py
└── requirements.txt
```

### File e Moduli

- `main.py`: Il punto di ingresso del programma. Esegue la funzione per creare l'interfaccia grafica.
- `converter.py`: Contiene la logica per la conversione del video in MP3.
- `gui.py`: Gestisce la creazione dell'interfaccia grafica e collega i vari componenti.
- `utils.py`: Contiene funzioni di utilità per la selezione dei file e delle cartelle e per l'aggiornamento dei campi di output.
- `requirements.txt`: Elenca le dipendenze necessarie per eseguire il progetto.

## Installazione

### Prerequisiti

Assicurati di avere Python 3.6 o versioni successive installato sul tuo sistema.

### Passaggi per l'Installazione

1. Clona il repository o scarica i file del progetto nella tua directory locale.

2. Apri un terminale e naviga nella directory del progetto.

3. Installa le dipendenze richieste eseguendo:

    ```bash
    pip install -r requirements.txt
    ```

## Utilizzo

1. Esegui il file `main.py` per avviare l'applicazione:

    ```bash
    python main.py
    ```

2. Utilizza l'interfaccia grafica per selezionare un file video che desideri convertire.

3. Seleziona la cartella di destinazione dove desideri salvare il file MP3 convertito.

4. Clicca su "Converti" per avviare il processo di conversione.

## Dipendenze

- `moviepy`: Utilizzato per l'elaborazione e la manipolazione dei file video.
- `tkinter`: Utilizzato per creare l'interfaccia grafica.

## Contributi

Se desideri contribuire a questo progetto, sentiti libero di fare un fork del repository e aprire una pull request con i tuoi miglioramenti.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.
