'''
this code solves the double summary problem and the rerun problem by using session state to store the summary and pdf file path
with Crystalcareai/Whisper-Medicalv1 model
'''

import streamlit as st
import json
from fpdf import FPDF
import google.generativeai as genai
from dotenv import load_dotenv
import os
import torch
import soundfile as sf
from pydub import AudioSegment
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Whisper Medical Model
@st.cache_resource
def load_whisper_medical_model():
    processor = AutoProcessor.from_pretrained("Crystalcareai/Whisper-Medicalv1")
    model = AutoModelForSpeechSeq2Seq.from_pretrained("Crystalcareai/Whisper-Medicalv1")
    model.eval()  # Set model to evaluation mode
    return processor, model

processor, model = load_whisper_medical_model()

# Function to convert audio files to WAV format
def convert_to_wav(input_file, output_file="converted.wav"):
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_channels(1)  # Convert to mono
    audio = audio.set_frame_rate(16000)  # Set sample rate to 16kHz
    audio.export(output_file, format="wav")
    return output_file

# Function to transcribe the audio with chunking
def transcribe_audio(file_path, chunk_size=30):
    converted_file = convert_to_wav(file_path)
    waveform, sample_rate = sf.read(converted_file, dtype="float32")
    
    # Ensure multi-channel audio is averaged to mono
    if waveform.ndim > 1:
        waveform = waveform.mean(axis=1)
    
    chunk_length = chunk_size * sample_rate  # Convert seconds to samples
    num_chunks = len(waveform) // chunk_length + (len(waveform) % chunk_length != 0)
    
    transcription = ""
    for i in range(num_chunks):
        start = i * chunk_length
        end = start + chunk_length
        chunk = waveform[start:end]
        inputs = processor(chunk, sampling_rate=sample_rate, return_tensors="pt")
        
        with torch.no_grad():
            predicted_ids = model.generate(**inputs, max_new_tokens=200)  # Reduce max tokens for each chunk
        
        transcription += processor.batch_decode(predicted_ids, skip_special_tokens=True)[0] + " "
    
    return transcription.strip()

# Function to summarize the transcribed text using Google Gemini
def summarize_text_with_gemini(text):
    prompt = f"""
    Extract the key details from the following medical transcription and provide a structured summary:
    
    Transcription: "{text}"
        
    If any of these parameters are not available then omit them from the summary.
    
    - Patient’s Condition: (Summarize the patient's overall health condition using appropriate medical terminology.)
    - Diagnosis: (Specify the medical diagnosis based on the transcription.)
    - Affected Organ/System: (Mention the specific organ or body system impacted by the condition.)
    - Time taken: (Indicate the duration of the medical condition or treatment mentioned in the transcription.)
    - Treatment: (Describe the treatment or medical intervention provided to the patient.)
    - Medications used during the procedure
    - Surgeon's orders
    - Anesthetist and anesthesia used
    - Any specific symptoms reported
    - postoperative instructions
    - if numrerical data is present, provide it in a structured forrmat
    - any other relevent information
    Ensure that the extracted details are concise, medically accurate, and formatted clearly.
    
    """
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

def generate_pdf(summary):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Use built-in Helvetica font (supports Latin-1)
    pdf.set_font("Helvetica", size=12)

    pdf.cell(200, 10, "Medical Transcription Summary", ln=True, align='C')
    pdf.ln(10)

    # Replace Unicode characters with ASCII equivalents
    summary = summary.encode("latin-1", "ignore").decode("latin-1")

    pdf.multi_cell(0, 10, summary)

    pdf_file = "transcription_summary.pdf"
    pdf.output(pdf_file, "F")
    return pdf_file

st.title("Medical Speech-to-Text Transcription")

uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac"])

if uploaded_file is not None:
    file_path = "temp_audio." + uploaded_file.name.split('.')[-1]
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())  # Save uploaded file as temp file

    st.audio(file_path, format="audio/wav")  # Play uploaded audio
    
    if st.button("Generate Transcription & Summary"):
        st.write("Transcribing...")
        transcription = transcribe_audio(file_path)
        st.session_state.transcription = transcription  # Store in session state
        
        st.subheader("Transcription:")
        st.write(transcription)
        
        st.write("### Generating Summary with Gemini...")
        structured_summary = summarize_text_with_gemini(transcription)
        
        try:
            structured_summary_json = json.loads(structured_summary)
            st.session_state.summary = json.dumps(structured_summary_json, indent=4)
        except json.JSONDecodeError:
            st.session_state.summary = structured_summary
        
        # Generate PDF only after generating summary
        st.session_state.pdf_file = generate_pdf(st.session_state.summary)

    if "summary" in st.session_state:
        st.write("### Summary:")
        try:
            st.json(json.loads(st.session_state.summary))
        except json.JSONDecodeError:
            st.markdown(st.session_state.summary)
    
    if "pdf_file" in st.session_state:
        with open(st.session_state.pdf_file, "rb") as file:
            st.download_button(
                label="Download Summary as PDF",
                data=file,
                file_name="transcription_summary.pdf",
                mime="application/pdf"
            )