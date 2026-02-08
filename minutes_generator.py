import whisper
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

AUDIO_FILE = "test_audio.wav"
MODEL_NAME = "google/flan-t5-base"


def transcribe_audio(audio_path):
    print("Loading Whisper model...")
    whisper_model = whisper.load_model("base")

    print("Transcribing audio...")
    result = whisper_model.transcribe(audio_path)
    return result["text"]


def generate_meeting_minutes(transcript):
    print("Loading meeting minutes model...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    prompt = f"""
You are an assistant that creates professional meeting minutes.

From the transcript below, extract:

1. Agenda
2. Key Discussion Points
3. Action Items (with responsible person if implied)
4. Decisions Made

Transcript:
\"\"\"{transcript}\"\"\"

Return the output in this exact format:

Agenda:
-

Key Discussion Points:
-

Action Items:
-

Decisions:
-
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=False
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == "__main__":
    print("\n--- STARTING MEETING MINUTES GENERATOR ---\n")

    transcript = transcribe_audio(AUDIO_FILE)

    print("\n--- TRANSCRIPTION OUTPUT ---\n")
    print(transcript)

    minutes = generate_meeting_minutes(transcript)

    print("\n--- GENERATED MEETING MINUTES ---\n")
    print(minutes)
