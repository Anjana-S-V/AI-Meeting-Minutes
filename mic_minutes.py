import sounddevice as sd
import soundfile as sf
import whisper
import numpy as np
from transformers import pipeline

# ---------------- CONFIG ----------------
SAMPLE_RATE = 16000
CHANNELS = 1
AUDIO_FILE = "live_meeting.wav"
MIC_DEVICE_ID = None  # set to 1 or 4 if needed
# ----------------------------------------

print("\n--- STARTING LIVE MEETING MINUTES GENERATOR ---\n")

# -------- RECORD AUDIO --------
print("Recording... Speak now. Press ENTER to stop.\n")

audio_chunks = []

def callback(indata, frames, time, status):
    if status:
        print(status)
    audio_chunks.append(indata.copy())

with sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    device=MIC_DEVICE_ID,
    callback=callback
):
    input()  # wait for ENTER

# ✅ FIXED PART
audio = np.concatenate(audio_chunks, axis=0)
sf.write(AUDIO_FILE, audio, SAMPLE_RATE)

print(f"\nAudio saved as {AUDIO_FILE}")

# -------- TRANSCRIPTION --------
print("\nLoading Whisper model...")
whisper_model = whisper.load_model("base")

print("Transcribing audio...")
result = whisper_model.transcribe(AUDIO_FILE)

transcript = result["text"]
print("\n--- TRANSCRIPTION OUTPUT ---\n")
print(transcript)

# -------- SUMMARIZATION --------
print("\nGenerating meeting minutes...")

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

summary = summarizer(
    transcript,
    max_length=150,
    min_length=60,
    do_sample=False
)

print("\n--- MEETING MINUTES ---\n")
print(summary[0]["summary_text"])

print("\n--- DONE ---\n")
