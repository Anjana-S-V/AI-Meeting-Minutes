import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000
CHANNELS = 1
OUTPUT_FILE = "live_meeting.wav"
DEVICE_ID = None  # set to a number like 1 or 4 if needed

print("Recording... Press ENTER to stop.")

recording = []

def callback(indata, frames, time, status):
    if status:
        print(status)
    recording.append(indata.copy())

with sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    device=DEVICE_ID,
    callback=callback
):
    input()  # waits for ENTER

audio = b"".join(recording)
sf.write(OUTPUT_FILE, audio, SAMPLE_RATE)

print(f"Saved recording as {OUTPUT_FILE}")
