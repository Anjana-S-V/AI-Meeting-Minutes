
AI Meeting Minutes Generator
============================

An end-to-end Machine Learning pipeline that records live meeting audio, transcribes it, and automatically generates structured meeting minutes.

This project is designed to be:

-   Fully local

-   Privacy-safe

-   Free of cost

-   Offline-capable after initial model download

* * * * *

 Project Overview
-------------------

The AI Meeting Minutes Generator captures audio from a microphone, converts speech to text using a local speech recognition model, and transforms the transcript into structured, professional meeting minutes using a transformer-based language model.

The system integrates:

-   Live audio recording

-   Speech-to-text transcription

-   AI-based structured summarization

-   Interactive web UI

All processing runs locally on the user's machine.

* * * * *

 Core Functionalities
-----------------------

###  Live Audio Recording

-   Captures meeting audio via microphone

-   Records audio in real time

-   Saves audio locally in WAV format

-   Handles mono-channel reshaping and sampling alignment

###  Speech-to-Text Transcription

-   Uses OpenAI Whisper (local model)

-   Converts recorded audio into raw transcript

-   Works offline after initial model download

-   Handles conversational and natural speech

###  AI-Based Structured Minute Generation

-   Uses Google FLAN-T5 transformer model

-   Converts transcript into:

    -   Agenda

    -   Key Discussion Points

    -   Action Items

    -   Decisions Made

-   Uses prompt engineering for consistent formatting

###  Streamlit Web Interface

-   Simple one-click interface

-   Displays transcript output

-   Displays structured meeting minutes

-   Lightweight and responsive design

###  Local Processing & Privacy

-   No cloud APIs used

-   No external data storage

-   No meeting audio uploaded

-   Fully local execution

* * * * *

 Tech Stack
-------------

### Programming Language

-   Python 3.x

### Machine Learning Models

**OpenAI Whisper**

-   Speech recognition model

-   Converts audio to text

-   Runs locally

**Google FLAN-T5 (via Hugging Face)**

-   Transformer-based language model

-   Generates structured meeting minutes

-   Open-source and free

### Libraries & Tools

-   Transformers (Hugging Face)

-   PyTorch (Torch)

-   SoundDevice

-   SoundFile

-   FFmpeg

-   Streamlit

* * * * *

 System Architecture
----------------------

Microphone Input\
        ↓\
Audio Recording (SoundDevice)\
        ↓\
Local WAV File\
        ↓\
Whisper Transcription\
        ↓\
Raw Transcript\
        ↓\
FLAN-T5 Structured Generation\
        ↓\
Meeting Minutes Output\
        ↓\
Streamlit UI Display

* * * * *

 Project Structure
--------------------

AI_Meeting_Minutes/\
│\
├── app.py\
├── mic_record.py\
├── mic_test.py\
├── mic_minutes.py\
├── minutes_generator.py\
├── requirements.txt\
├── .gitignore\
└── README.md

* * * * *

 Installation & Setup
-----------------------

###  Clone the Repository

git clone https://github.com/your-username/AI-Meeting-Minutes.git\
cd AI-Meeting-Minutes

###  Create Virtual Environment

python -m venv venv\
venv\Scripts\activate

###  Install Dependencies

pip install -r requirements.txt

###  Run the Application

streamlit run app.py

The application will open in your default browser.

* * * * *

 System Requirements
----------------------

Minimum recommended:

-   8GB RAM

-   5GB free disk space

-   Windows / macOS / Linux

-   Python 3.8+

Note:\
The first run will download ML models (~500MB--1.5GB).

* * * * *

 Challenges Faced & Solutions
-------------------------------

**Microphone Detection Issues**

-   Inspected device list manually

-   Configured correct input device index

**Audio Shape Errors**

-   Fixed mono-channel reshaping before saving WAV

**Hugging Face Pipeline Error**

-   Corrected incorrect task usage

**Windows Execution Policy Issues**

-   Adjusted PowerShell execution permissions

**Git Merge Conflicts**

-   Resolved unrelated histories

-   Handled non-fast-forward push errors

* * * * *

 Privacy & Cost
-----------------

### Privacy

-   No cloud APIs used

-   No external server communication

-   All data remains on local machine

-   No personal information stored

### Cost

-   100% free

-   Open-source models

-   No API billing

-   No subscription services

* * * * *

 Learning Outcomes
--------------------

This project enabled:

-   Building an end-to-end ML pipeline

-   Integrating speech recognition with NLP models

-   Implementing structured AI prompting

-   Creating an interactive UI with Streamlit

-   Managing Git conflicts professionally

-   Understanding local ML resource constraints

* * * * *

 Future Improvements
----------------------

-   Real-time streaming transcription

-   Speaker diarization

-   Export minutes as PDF/Word

-   Lightweight model optimization

-   Multi-language support

-   Optional cloud deployment
