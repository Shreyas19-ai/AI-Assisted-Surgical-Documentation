# Medical Speech-to-Text Transcription

This project solves the **double summary problem** and the **rerun problem** by using **session state** to store the summary and PDF file path. It leverages the **Crystalcareai/Whisper-Medicalv1** model for accurate medical speech-to-text transcription and integrates with **Google Gemini** for structured summarization.

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

