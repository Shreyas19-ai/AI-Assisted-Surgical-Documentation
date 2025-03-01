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

Prerequisites

Before running this application, you need to install FFmpeg and add it to the system PATH variable.

Installing FFmpeg

Windows Users:

Download FFmpeg from https://ffmpeg.org/download.html.

Extract the ZIP file to a location like C:\ffmpeg.

Inside the extracted folder, go to the "bin" directory (e.g., C:\ffmpeg\bin).

Add this path to the System PATH variable:

Press Win + R, type sysdm.cpl, and press Enter.

Go to the Advanced tab → Click Environment Variables.

Under System Variables, find Path, click Edit, then New, and add C:\ffmpeg\bin.

Click OK and close all windows.

Verify installation by running this command in Command Prompt:

ffmpeg -version

If FFmpeg is installed correctly, it will display the version details.

Linux/Mac Users:

Run the following command in the terminal:

sudo apt install ffmpeg  # For Ubuntu/Debian
brew install ffmpeg  # For macOS (using Homebrew)

Now, your system is ready to run the application! 🚀

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
- Implement **real-time transcription**
- Support **multi-language** medical transcriptions
- Improve **data visualization** for structured outputs

## License
This project is licensed under the MIT License.

---
## Contributors
- [Shreyas Ghadigaonkar](https://github.com/Shreyas19-ai)
- [Pankaja Raut](https://github.com/pankajaraut)
- [Sakshi Bandbe](https://github.com/Sakshi4Med)
- [Anoushka Joshi](https://github.com/02Anoushka)

