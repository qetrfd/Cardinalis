import time
import numpy as np
import sounddevice as sd
from openwakeword.model import Model
from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
CHANNELS = 1
WAKE_THRESHOLD = 0.5
WAKE_COOLDOWN_SEC = 1.2
UTTERANCE_SEC = 3.5


def rms_db(x: np.ndarray) -> float:
    x = x.astype(np.float32)
    v = np.sqrt(np.mean(x * x) + 1e-12)
    return 20.0 * np.log10(v + 1e-9)


def record_seconds(seconds: float) -> np.ndarray:
    frames = int(seconds * SAMPLE_RATE)
    audio = sd.rec(frames, samplerate=SAMPLE_RATE, channels=CHANNELS, dtype="int16")
    sd.wait()
    return audio.reshape(-1)


def run_voice(core):

    ow = Model(
        wakeword_models=["hey_jarvis_v0.1"],
        inference_framework="onnx"
    )

    stt = WhisperModel("small", device="cpu", compute_type="int8")

    wake_label = "hey_jarvis_v0.1"

    last_wake = 0.0

    block = int(0.5 * SAMPLE_RATE)

    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16",
        blocksize=block
    )

    stream.start()

    while True:

        data, _ = stream.read(block)

        buf = data.reshape(-1).astype(np.int16)

        scores = ow.predict(buf)

        score = float(scores.get(wake_label, 0.0))

        now = time.time()

        if score >= WAKE_THRESHOLD and (now - last_wake) > WAKE_COOLDOWN_SEC:

            last_wake = now

            utt = record_seconds(UTTERANCE_SEC)

            if rms_db(utt) < -45:
                continue

            segments, _ = stt.transcribe(
                utt.astype(np.float32) / 32768.0,
                language="es"
            )

            text = " ".join([seg.text.strip() for seg in segments]).strip()

            if text:
                print("Escuché:", text)
                core.handle_text(text)