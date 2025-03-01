# AI-Assisted-Surgical-Documentation

AI-Assisted Surgical Documentation is an advanced system designed to automate and streamline the documentation process in surgical procedures. Using AI-driven speech-to-text transcription and structured summarization, the system captures key details from surgeons' conversations and generates accurate, structured medical reports.

## Features
- Converts medical speech to text using **Whisper-Medicalv1**
- Summarizes key points using **Google Gemini**
- Supports **multiple audio formats** (WAV, MP3, FLAC)
- Handles **chunked transcription** to ensure high accuracy
- Generates a **PDF report** with the summarized transcription
- Uses **session state** to avoid duplicate processing

## Technologies Used
- **Streamlit** (for UI)
- **Google Gemini API** (for summarization)
- **Crystalcareai/Whisper-Medicalv1** (for speech-to-text transcription)
- **PyDub** (for audio conversion)
- **FPDF** (for PDF generation)
- **SoundFile & Torch** (for handling audio files)

## Prerequisites
- You need to install ffmpeg on your device before running this script
- Also add it to the System Environment Variables Path

### Steps to Install ffmpeg and Set Up Environment Variables:

1. **Download ffmpeg:**
   - Visit the official ffmpeg website: [ffmpeg.org](https://ffmpeg.org/download.html)
   - Download the appropriate version for your operating system.

2. **Extract the files:**
   - Extract the downloaded ffmpeg ZIP file to a desired location (e.g., `C:\ffmpeg`).

3. **Add ffmpeg to System Environment Variables:**
   - Open **System Properties** → **Advanced** → **Environment Variables**.
   - In **System Variables**, find `Path` and click **Edit**.
   - Click **New** and add the path to the `bin` folder inside ffmpeg (e.g., `C:\ffmpeg\bin`).
   - Click **OK** to save changes.

4. **Verify Installation:**
   - Open **Command Prompt** and type:
     ```bash
     ffmpeg -version
     ```
   - If installed correctly, it will display the ffmpeg version details.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shreyas19-ai/AI-Assisted-Surgical-Documentation.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file and add your **Gemini API Key**:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage
1. **Run the application:**
   ```bash
   streamlit run primary2.py
   ```
2. **Upload an audio file** (WAV, MP3, FLAC).
3. Click **"Generate Transcription & Summary"**.
4. View the transcription and structured summary.
5. Download the **PDF report**.

## File Structure
```
|-- primary2.py  # Main Streamlit app
|-- requirements.txt  # Python dependencies
|-- .gitignore
|-- README.md  # Project documentation
```

## Future Enhancements
- Web App Deployment for seamless accessibility
- EHR Integration with custom APIs for structured data retrieval
- Enhanced AI Model for faster and more accurate medical transcription

## License
This project is licensed under the MIT License.

---
## Contributors
- [Shreyas Ghadigaonkar](https://github.com/Shreyas19-ai)
- [Pankaja Raut](https://github.com/pankajaraut)
- [Sakshi Bandbe](https://github.com/Sakshi4Med)
- [Anoushka Joshi](https://github.com/02Anoushka)

