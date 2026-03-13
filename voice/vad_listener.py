import queue
import sounddevice as sd
import numpy as np
import torch
from silero_vad import load_silero_vad, get_speech_timestamps

samplerate = 16000
blocksize = 512

q = queue.Queue()

model = load_silero_vad()


def callback(indata, frames, time, status):
    q.put(indata.copy())


def listen_for_voice():

    with sd.InputStream(
        samplerate=samplerate,
        blocksize=blocksize,
        channels=1,
        callback=callback
    ):

        audio_buffer = []

        while True:

            data = q.get()

            audio_buffer.append(data)

            if len(audio_buffer) > 50:

                audio = np.concatenate(audio_buffer, axis=0)
                audio = torch.from_numpy(audio.flatten())

                speech = get_speech_timestamps(audio, model)

                if len(speech) > 0:
                    return True

                audio_buffer = []