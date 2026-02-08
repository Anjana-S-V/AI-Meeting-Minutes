import streamlit as st
import whisper
import sounddevice as sd
import soundfile as sf
import numpy as np
import queue
import threading
from transformers import pipeline

# -----------------------------
# CONFIG
# -----------------------------
SAMPLE_RATE = 16000
AUDIO_FILE = "live_meeting.wav"

st.set_page_config(
    page_title="AI Meeting Minutes Generator",
    layout="centered"
)

# -----------------------------
# LOAD MODELS (CACHED)
# -----------------------------
@st.cache_resource
def load_models():
    whisper_model = whisper.load_model("base")

    summarizer = pipeline(
        "text-generation",
        model="google/flan-t5-base"
    )

    return whisper_model, summarizer


# -----------------------------
# AUDIO RECORDING
# -----------------------------
audio_queue = queue.Queue()
recording = False


def audio_callback(indata, frames, time, status):
    if recording:
        audio_queue.put(indata.copy())


def record_audio():
    global recording
    recording = True
    audio_data = []

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        callback=audio_callback
    ):
        while recording:
            try:
                audio_data.append(audio_queue.get(timeout=0.1))
            except queue.Empty:
                pass

    audio_np = np.concatenate(audio_data, axis=0)
    sf.write(AUDIO_FILE, audio_np, SAMPLE_RATE)


# -----------------------------
# UI
# -----------------------------
st.title("🎙 AI Meeting Minutes Generator")
st.write(
    "Record a meeting, transcribe it, and generate structured minutes."
)

whisper_model, summarizer = load_models()

if "is_recording" not in st.session_state:
    st.session_state.is_recording = False

# -----------------------------
# RECORD BUTTONS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Start Recording", disabled=st.session_state.is_recording):
        st.session_state.is_recording = True
        audio_queue.queue.clear()

        thread = threading.Thread(target=record_audio)
        thread.start()

with col2:
    if st.button("⏹ Stop Recording", disabled=not st.session_state.is_recording):
        st.session_state.is_recording = False
        st.success("Recording stopped.")

# -----------------------------
# PROCESS AUDIO
# -----------------------------
if not st.session_state.is_recording and st.button("🧠 Generate Meeting Minutes"):
    st.info("Transcribing audio...")
    result = whisper_model.transcribe(AUDIO_FILE)
    transcript = result["text"]

    st.subheader("📝 Transcript")
    st.write(transcript)

    st.info("Generating meeting minutes...")

    prompt = f"""
Create professional meeting minutes from the transcript below.

Transcript:
{transcript}

Output format (follow exactly):

Agenda:
-

Key Discussion Points:
-

Action Items:
-

Decisions:
-
"""

response = summarizer(
    prompt,
    max_new_tokens=250,
    do_sample=False,
    temperature=0.0
)[0]["generated_text"]

# 🔧 SAFETY: remove prompt echo if model repeats it
if "Agenda:" in response:
    response = response[response.index("Agenda:"):]

st.subheader("📋 Meeting Minutes")
st.text(response)


    