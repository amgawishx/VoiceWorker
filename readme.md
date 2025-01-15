![image](https://github.com/user-attachments/assets/371e52da-7614-408a-b6b7-5ef9890489d2)

# VoiceWorker

VoiceWorker is a Streamlit-based application for transcribing audio files or recordings using the Faster Whisper model. This app supports multiple languages and allows users to choose from various pre-trained model sizes for transcription tasks.

## Why Faster Whisper?

Faster Whisper is a highly optimized implementation of OpenAI's Whisper model. It offers:

1. **Enhanced Speed**: Faster Whisper processes audio data significantly faster than the original implementation, making it ideal for real-time or large-scale transcription tasks.
2. **Resource Efficiency**: It uses less memory and computational power, enabling transcription on devices with limited resources.
3. **Customizability**: The model provides more flexibility with compute types (e.g., float16), which further optimizes performance on compatible hardware.

### Difference Between Faster Whisper and Whisper

| Feature                | Faster Whisper                          | Original Whisper                     |
|------------------------|-----------------------------------------|---------------------------------------|
| **Speed**             | Faster processing and inference         | Slower inference                     |
| **Resource Usage**    | Lower memory and computational needs    | Higher memory and resource demand    |
| **Flexibility**       | Customizable compute types (e.g., float16) | Fixed compute type (float32)         |
| **Scalability**       | Suitable for real-time transcription    | Best for offline, batch processing   |

Faster Whisper is especially advantageous for interactive applications like VoiceWorker, where speed and efficiency are critical.

## Features

- Transcribe audio or video files.
- Record live audio for real-time transcription.
- Support for over 90 languages.
- GPU acceleration with CUDA (if available).
- Flexible model size selection.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/amgawishx/VoiceWorker.git
   cd VoiceWorker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the app with the command above.
2. Choose your desired Whisper model size and transcription language in the app interface.
3. Upload an audio/video file or use the built-in audio recorder.
4. View the transcription output directly in the app.

## Requirements

- Python 3.8+
- Streamlit
- Faster Whisper
- PyTorch
- GPU with CUDA support (optional but recommended for faster processing)

## Acknowledgments

- [Faster Whisper](https://github.com/openai/whisper) for providing the optimized transcription model.
- [Streamlit](https://streamlit.io/) for the interactive user interface framework.

---

VoiceWorker simplifies audio transcription tasks with speed and efficiency. Feel free to contribute or raise issues on the [GitHub repository](https://github.com/amgawishx/VoiceWorker).
