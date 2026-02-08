# AI-Meeting-Minutes


An end-to-end Machine Learning pipeline that records meeting audio, transcribes it, and generates structured minutes .This project is built to be entirely local, privacy-safe, and free of cost.

##  Project Overview
This tool records live audio from a microphone, transcribes it using OpenAI Whisper, and uses a transformer-based model to create structured meeting summaries. 

##  Components & Tools
* **Whisper:** Local, offline speech-to-text transcription.
* **Hugging Face Transformers (FLAN-T5):** Converts raw transcripts into structured minutes.
* ]**Streamlit:** Lightweight UI for recording and displaying results.
* **SoundDevice & SoundFile:** Used for live microphone recording.
* **FFmpeg:** Audio preprocessing support.

##  Workflow
1.**Record:** Audio is captured via the microphone.
2. **Save:** Audio is saved locally to the machine.
3. **Transcribe:** Whisper converts the local audio file to text.
4. **Generate:** FLAN-T5 generates meeting minutes from the transcript.
5. **Display:** Results are rendered in the Streamlit UI.

##  Challenges Overcome
* **Technical Errors:** Fixed microphone detection, audio shape errors, and Hugging Face pipeline mismatches.
* **Environment Issues:** Managed Windows PowerShell execution policies.
* **Version Control:** Resolved Git merge conflicts and pull/merge issues on GitHub.

##  Privacy & Cost
* **Free:** All tools used are free with no paid APIs.
* **Private:** No personal data is stored, and everything runs locally.

##  Learning Outcomes
* Developed an end-to-end ML pipeline.
* Gained experience in audio processing and model integration.
* Mastered Git conflict resolution and UI deployment.

---
*Developed as a privacy-focused solution for automated meeting documentation.*
