import sounddevice as sd
import soundfile as sf
from tkinter import *
from V2V import V2V
from playsound import playsound


def Voice_rec():
    fs = 48000

    # seconds
    duration = 3
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    # Save as FLAC file at correct sampling rate
    file_path = 'recording.flac'
    sf.write(file_path, recording, fs)

    print(f"File saved at {file_path}")

    v2v = V2V(file_path=file_path)
    result = v2v.process()

    playsound(result)

    return result


master = Tk()

Label(master, text=" Voice Recoder : ").grid(row=0, sticky=W, rowspan=5)

b = Button(master, text="Start", command=Voice_rec)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()
